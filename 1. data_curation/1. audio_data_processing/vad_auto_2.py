from lib.vad import VAD
from lib.force_chunk import force_chunk
from lib.convert_sampling_rate import convert_sample_rate
from lib.speech_intelligibility import check_speech_intelligibility
import os
from glob import glob
from tqdm import tqdm
import librosa

def filter_audio_on_seconds(seconds, path):
    with open("less_than_5_sec.txt", "w") as txt:
        for audio in tqdm(glob(os.path.join(path, "*.wav"))):
            if librosa.get_duration(path=audio) < seconds:
                txt.write(os.path.split(audio)[-1])
            # os.remove(audio)



def main():
    district = input("\nName of district: ")
    audios = os.path.join("vad_chunks", district, "audios")
    big_audios = os.path.join("vad_chunks", district, "big_audios")
    small_audios = os.path.join("vad_chunks", district, "small_audios")
    vad = VAD()

    os.makedirs(audios, exist_ok=True)
    os.makedirs(big_audios, exist_ok=True)
    os.makedirs(small_audios, exist_ok=True)

    print("\033[92mCropping data\033[0m")
    raw_audios = glob("data\\*.wav")
    for wav in tqdm(raw_audios):
        vad.crop_data(wav, audios, big_audios, small_audios)

    print("\033[92mforce_chunking\033[0m")
    force_chunk(audios)
    force_chunk(big_audios)
    print()


    print("\033[92mRemoving audios less than 5 seconds\033[0m")
    filter_audio_on_seconds(5, audios)
    filter_audio_on_seconds(5, big_audios)
    filter_audio_on_seconds(5, small_audios)
    print()

    print("\033[92mConverting sample rate\033[0m")
    convert_sample_rate(audios, 16000)
    convert_sample_rate(big_audios, 16000)
    convert_sample_rate(small_audios, 16000)
    print()

    print("\033[92mChecking speech intelligibility\033[0m")
    check_speech_intelligibility(
        os.path.join("vad_chunks", district, district+"_bad_aud.txt"),  # txt report export path
        audios,           # src_paths
        big_audios,       # src_paths 
        small_audios      # src_paths
    )

if __name__ == "__main__":
    main()


