# Automated VAD
- Remove white noise from audio by splitting it into smaller clips
- Force split the clips to 30 seconds or less
- Remove any audio less than 5 seconds
- Check intelligibility of speech using Wav2Vec2

# Folder structure
```bash
|- data #Raw data is stored here 
|- vad_chunks
|    |- <District> # District specific data is stored here
|        |- audios
|        |- big_audios
|        |- small_audios
|- lib
|- vad_auto_2.py
```

# Usage
After running the script, simply provide the name of the district when prompted and maintain the above file structure.