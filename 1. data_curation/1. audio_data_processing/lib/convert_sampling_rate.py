from pydub import AudioSegment
import os
from tqdm import tqdm
from glob import glob

def convert_sample_rate(src_folder:str, sample_rate:int):
    for audio in tqdm(glob(src_folder+"\\*.wav")):
        converted_audio = AudioSegment.from_file(audio).set_frame_rate(sample_rate)
        os.remove(audio)
        converted_audio.export(audio)


if __name__ == "__main__":
    convert_sample_rate("G:\\chunk_site\\testing", 16000)
    for aud in glob("G:\\chunk_site\\testing\\*"):
        print(AudioSegment.from_file(aud).frame_rate)