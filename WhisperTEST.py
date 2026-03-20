from datetime import timedelta
import os
import whisper
from stringedit import srtnamefrompathname, txtfrompathname

#./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/AlJazeera.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/ArchitektLangsam.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/ArchitektSchnell.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/LernvideoSchule.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/Tire.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/Werbevideo.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3.bin -osrt -l ar


./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/Werbevideo.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/ArchitektLangsam.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/ArchitektSchnell.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/AlJazeera.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/LernvideoSchule.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar
./build/bin/whisper-cli -f /Users/anisheit/Documents/Python/Videomodul/Tire.mp3 -m /Users/anisheit/Documents/Python/Videomodul/whisper.cpp/models/ggml-large-v3-turbo.bin -osrt -l ar



pathnames = ['/Users/anisheit/Documents/Python/Videomodul/AlJazeera.mp3', 
             '/Users/anisheit/Documents/Python/Videomodul/ArchitektLangsam.mp3', 
             '/Users/anisheit/Documents/Python/Videomodul/ArchitektSchnell.mp3',
             '/Users/anisheit/Documents/Python/Videomodul/LernvideoSchule.mp3',
             '/Users/anisheit/Documents/Python/Videomodul/Werbevideo.mp3',
             '/Users/anisheit/Documents/Python/Videomodul/Tire.mp3']
pathi = ['/Users/anisheit/Documents/Python/Videomodul/AlJazeeraTeil2.mp3', '/Users/anisheit/Documents/Python/Videomodul/Tire.mp3']




def transcribe_audio(path, pathname):
    model = whisper.load_model("turbo") #<------ Model hier ändern
    print("Whisper model loaded. for: " + path)
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

        filename = os.path.join("SrtFiles", pathname)
        with open(filename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return filename



for i in range(len(pathnames)):
    #print(pathnames[i] +  " " + srtnamefrompathname(pathnames[i]))
    #for srt
    #transcribe_audio(pathi[i], srtnamefrompathname(pathi[i]))
    #for txt
    transcribe_audio(pathnames[i], srtnamefrompathname(pathnames[i]))


