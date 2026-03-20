from os import listdir
from os.path import isfile, join
import pysrt
import webvtt

#originalFilename, projectFilename, YTLinks, Dialekt, Länge
eckdaten = [['تعرف على حجم الأضرار في خربتي حلاوة والفخيت عقب هجوم المستوطنين بمسافر يطا جنوبي الخليل','AlJazeera','https://www.youtube.com/watch?v=OQVm0pKuhSo&list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&index=3&t=1s','MSA','04:15'],
            ['ثلاثة اختراعات رائعة صنعت في العام الماضي 🙂💚','Werbevideo','https://www.youtube.com/watch?v=8J4Z50P5M3A','MSA','03:23'],
            ['محادثة عربية / التعارف للناطقين بغير العربية','LernvideoSchule','https://www.youtube.com/watch?v=okOOqKv1mfE&list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&index=7','MSA','01:43'],
            ['Levantine Arabic Listening Practice With English Subtitles | Palestinian Documentary Part 1','ArchitektSchnell','https://www.youtube.com/watch?v=GZbj89jma64&list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&index=15','Levantine (Gaza)','00:58'],
            ['Levantine Arabic Listening Practice With English Subtitles | Palestinian Documentary Part 1','ArchitektLangsam','https://www.youtube.com/watch?v=GZbj89jma64&list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&index=15','Levantine (Gaza)','00:44'],
            ['موسم التوت في الطيرة شي من الخيال','Tire','https://www.youtube.com/watch?v=oNWQNJxNeH4&list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&index=9','Levantine (Israel)','04:42']]


"""
    Die Funktionen loadTranskripton_srt, loadTranskripton_vtt und loadTranskripton_txt laden die
    die generierten Files aus den jeweiligen Ordnern und bereiten die Daten in einer Tupel-Liste auf. 
    Das erste Element der Tupel dient dabei als 'Schlüssel' um die Texte in den Folgenden Schritten einander zuordnen zu können.
"""


def loadTranskription_srt(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    #print(files)
    return_list= []
    for i in range(len(files)):
        transkript_list= []
        #print(files[i])
        #f = open(path + files[i])
        #print(f.read()[::-1])
        transkript = pysrt.open(path + files[i], encoding='utf-8')
        for x in transkript:
            #print(x.text)
            #print()
            transkript_list.append(x.text)
        transkript_list = " ".join(transkript_list)
        transkript_list = transkript_list.replace('.', '')
        transkript_list = transkript_list.replace(',', '')
        transkript_list = transkript_list.replace('?', '')
        transkript_list = transkript_list.replace('؟', '')
        return_list.append(transkript_list)
    files_no_type = []
    for l in range(len(files)):
        files_no_type.append(files[l][:-4])
    return_list = list(zip(files_no_type, return_list))
    return return_list

def loadTranskription_vtt(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    #print(files)
    return_list= []
    for i in range(len(files)):
        transkript_list= []
        #print(files[i])
        #f = open(path + files[i])
        #print(f.read()[::-1])
        for x in webvtt.read(path + files[i]):
            #print(x.text)
            #print()
            transkript_list.append(x.text)
        transkript_list = " ".join(transkript_list)
        transkript_list = transkript_list.replace('.', '')
        transkript_list = transkript_list.replace(',', '')
        transkript_list = transkript_list.replace('?', '')
        transkript_list = transkript_list.replace('؟', '')

        return_list.append(transkript_list)
    files_no_type = []
    for l in range(len(files)):
        files_no_type.append(files[l][:-4])
    return_list = list(zip(files_no_type, return_list))
    return return_list

def loadTranskription_txt(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    #print(files)
    return_list= []
    for i in range(len(files)):
        transkript_list= []
        #print(files[i])
        f = open(path + files[i], encoding='utf-8')
        #transkript_list.append(f.read)
        for x in f.read():
            transkript_list.append(x)
        transkript_list = "".join(transkript_list)
        transkript_list = transkript_list.replace('.', '')
        transkript_list = transkript_list.replace(',', '')
        transkript_list = transkript_list.replace('?', '')
        transkript_list = transkript_list.replace('؟', '')
        return_list.append(transkript_list)
    
    files_no_type = []
    for l in range(len(files)):
        files_no_type.append(files[l][:-4])
    return_list = list(zip(files_no_type, return_list))
    return return_list   
    
#laden der manuellen transkriptionen
manuelleTranskriptionen = loadTranskription_srt('/Users/anisheit/Documents/Python/Videomodul/manuelleTranskription/')

#laden von Whisper Large
whisperLarge = loadTranskription_srt('/Users/anisheit/Documents/Python/Videomodul/Out/WhisperLarge/')

#laden von Whsiper Turbo
whisperTurbo = loadTranskription_srt('/Users/anisheit/Documents/Python/Videomodul/Out/WhisperTurbo/')

#laden von WhisperSmall
whisperSmall = loadTranskription_srt('/Users/anisheit/Documents/Python/Videomodul/Out/WhisperSmall/')

#laden von AzureSpeech_ar-IL
azureSpeech_ar_IL = loadTranskription_txt('/Users/anisheit/Documents/Python/Videomodul/Out/AzureSpeech_ar-IL/')

#laden von Gemini ara-IL
gemini_ara_IL = loadTranskription_txt('/Users/anisheit/Documents/Python/Videomodul/Out/Gemini ara-IL/')

#laden von Transkriptor
transkriptor = loadTranskription_txt('/Users/anisheit/Documents/Python/Videomodul/Out/Transkriptor/')

#laden von vosk-model-ar-022-linto-110
vosk_model_ar_022_linto_110 = loadTranskription_vtt('/Users/anisheit/Documents/Python/Videomodul/Out/vosk-model-ar-022-linto-110/')

#laden von vosk-model-ar-mgb2
vosk_model_ar_mgb2 = loadTranskription_vtt('/Users/anisheit/Documents/Python/Videomodul/Out/vosk-model-ar-mgb2/')

#laden von vosk-model-small-ar-tn-01-linto
vosk_model_ar_tn_01_linto = loadTranskription_txt('/Users/anisheit/Documents/Python/Videomodul/Out/vosk-model-small-ar-tn-01-linto/')
