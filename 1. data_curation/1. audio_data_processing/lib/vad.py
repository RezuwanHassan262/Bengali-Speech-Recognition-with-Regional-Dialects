import os 
import torch
import numpy as np
import librosa
from tqdm import tqdm
from typing import Iterable


class VAD:
    def __init__(self):
        self.DUR_MIN=15
        self.DUR_MAX=25
        self.DUR_THRESH=10
        self.SAMPLING_RATE = 16000
        self.USE_ONNX = False # change this to True if you want to test onnx model
        self.model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                                    model='silero_vad',
                                    force_reload=True,
                                    onnx=self.USE_ONNX)
        self.DATA_DICTS=[]
        (self.get_speech_timestamps,
        self.save_audio,
        self.read_audio,
        self.VADIterator,
        self.collect_chunks) = utils
    
    def create_dir(self, base,ext):
        _path=os.path.join(base,ext)
        if not os.path.exists(_path):
            os.makedirs(_path)
        return _path

    def load_data(self, path):
        """loads a wav"""
        wave,_= librosa.load(path, sr=self.SAMPLING_RATE, mono=True)
        wave=np.trim_zeros(wave)
        return wave
    
    def normalize_signal(self, signal):
        """Normailize signal to [-1, 1] range"""
        gain = 1.0 / (np.max(np.abs(signal)) + 1e-9)
        return signal * gain
    
    def split_by_duration(self, speech_timestamps):
    # calculate duration
        stamps=[]
        for ts in speech_timestamps:
            dur=(ts["end"]-ts["start"])/self.SAMPLING_RATE
            ts["duration"]=dur
            stamps.append(ts)
        
        # split by big audios
        data_split=[]
        big_audios=[]
        temp=[]
        for ts in stamps:
            dur=ts["duration"]
            if dur<self.DUR_MAX:
                temp.append(ts)
            else:
                data_split.append(temp)
                big_audios.append(ts)
                temp=[]
        if len(temp)>1:
            data_split.append(temp)
        return data_split,big_audios

    def sequence_stamps(self, stamps):
        sequence=[]
        ts_2=None
        for idx in range(len(stamps)-1):
            ts_1=stamps[idx]
            ts_1["type"]="voice"
            ts_2=stamps[idx+1]
            ts_2["type"]="voice"
            
            ns={}
            ns["start"]=ts_1["end"]
            ns["end"]=ts_2["start"]
            dur=(ns["end"]-ns["start"])/self.SAMPLING_RATE
            ns["duration"]=dur
            ns["type"]="noise"
            
            sequence.append(ts_1)
            sequence.append(ns)
        if ts_2 is not None:
            sequence.append(ts_2)
        return sequence
    

    def create_audio_stamps(self, seq):
        data=[]
        audio=[]
        dur=0
        for s in seq:
            dur+=s["duration"]
            if dur>=self.DUR_MIN and dur<=self.DUR_MAX:
                audio.append(s)
                data.append(audio)
                audio=[]
                dur=0
            elif dur<self.DUR_MIN:
                audio.append(s)
            elif dur>self.DUR_MAX:
                data.append(audio)
                audio=[]
                audio.append(s)
                dur=s["duration"]
        if len(audio)>1:
            data.append(audio)
        return data
    

    def crop_data(self, src_audio:str, data_path:str, big_audio_path:str, small_audio_path:str):
        # load and normalize
        wave=self.normalize_signal(self.load_data(src_audio))
        wav=torch.tensor(wave)
        #-------noise----------------
        # get speech stamps
        speech_timestamps = self.get_speech_timestamps(wav, self.model, sampling_rate=self.SAMPLING_RATE)
        data_splits,big_audios = self.split_by_duration(speech_timestamps)
        # create sequences of from data_splits
        crops=[]
        for ds in data_splits:
            seq=self.sequence_stamps(ds)
            crops+=self.create_audio_stamps(seq)
            
        iden=os.path.basename(src_audio).split(".")[0]
        
        # save big audios
        for idx,ba in enumerate(big_audios):
            audio=self.collect_chunks([ba],wav)
            src_audio=os.path.join(big_audio_path,f"{iden}_big_audio_{idx}.wav")
            self.save_audio(src_audio,audio)
            self.DATA_DICTS.append({"path":src_audio,
                            "length":(ba["end"]-ba["start"])/self.SAMPLING_RATE,
                            "classification":"big"})
        # save audios
        sidx=0
        idx=0
        for crop in tqdm(crops):
            try:
                audio=self.collect_chunks(crop,wav)
                dur=(crop[-1]["end"]-crop[0]["start"])/self.SAMPLING_RATE
                if dur<self.DUR_THRESH:
                    src_audio=os.path.join(small_audio_path,f"{iden}_small_audio_{sidx}.wav")
                    self.save_audio(src_audio,audio)
                    sidx+=1
                    self.DATA_DICTS.append({"path":src_audio,
                                    "length":dur,
                                    "classification":"small"})
                else:
                    src_audio=os.path.join(data_path,f"{iden}_audio_{idx}.wav")
                    self.save_audio(src_audio,audio)
                    idx+=1
                    self.DATA_DICTS.append({"path":src_audio,
                                    "length":dur,
                                    "classification":"good"})
            except Exception as e:
                print(iden,crop)

    
    