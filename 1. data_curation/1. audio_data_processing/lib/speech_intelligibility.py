import librosa
from tqdm import tqdm
import os
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def contains_speech(audio_path):

    speech_array, sampling_rate = librosa.load(audio_path, sr=16000)
    input_values = processor(speech_array, return_tensors="pt", padding="longest", sampling_rate = sampling_rate).input_values
    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return bool(transcription.strip())



def check_speech_intelligibility(txt_report_path, *src_paths):
    """Checks intelligibility of speech and writes a name of audios that are unintelligible to a text file.
    
    Parameters:
        txt_report_path : Export path for the text file with unintelligible audio name
        src_paths : One or more paths to directory containing audios
    """
    unintelligible_auds = []

    for src_path in src_paths:
        auds = os.listdir(src_path)
        for audio in tqdm(auds):
            x = contains_speech(os.path.join(src_path, audio))
            if x == False:
                unintelligible_auds.append(audio)

    with open(txt_report_path, "w") as report:
        for i in unintelligible_auds:
            report.write(f'{i}\n')




if __name__ == "__main__":
    district = "Sylhet"
    check_speech_intelligibility(
        os.path.join("G:\\chunk_site\\vad_chunks", district, district+"_bad_aud.txt"),  # txt report export path
        os.path.join("G:\\chunk_site\\vad_chunks", district, "16kHz_audios"),           # src_paths
        os.path.join("G:\\chunk_site\\vad_chunks", district, "16kHz_big_audios"),       # src_paths 
        os.path.join("G:\\chunk_site\\vad_chunks", district, "16kHz_small_audios")      # src_paths
    )