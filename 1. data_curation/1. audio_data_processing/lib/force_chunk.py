from glob import glob
import os
import torchaudio
import librosa


def force_chunk(src_path):
    for audio in glob(os.path.join(src_path, "*.wav")):
        dur = librosa.get_duration(path=audio)

        if not (dur - 30 >= 1): # because 30.01 second is basically 30 seconds
            continue
        else:
            y, sr = torchaudio.load(audio)
            print(y.shape)

            chunk_id = 0
            while y.shape[1] >= sr * 30:
                y_ext = y[:, :sr *30]
                y = y[:, sr*30:]

                                # rec_01_chunk2.wav / rec_03_big_audio_2_chunk_1.wav
                new_audio_name = os.path.split(audio)[-1][:-4] + "_chunk_" + str(chunk_id) + ".wav" 
                torchaudio.save(os.path.join(src_path, new_audio_name), y_ext, sr)
                chunk_id += 1
            
            new_audio_name = os.path.split(audio)[-1][:-4] + "_chunk_" + str(chunk_id) + ".wav"
            torchaudio.save(os.path.join(src_path, new_audio_name), y, sr)

            os.remove(audio)


if __name__ == "__main__":
    force_chunk("vad_chunks\\Gazipur\\audios")