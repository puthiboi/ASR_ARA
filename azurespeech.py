import  os
import  azure.cognitiveservices.speech  as  speechsdk
import time


from keys import speechkey, speechregion
from stringedit import txtfrompathname
pathnames = ['/Users/anisheit/Documents/Python/Videomodul/AlJazeera.wav', 
             '/Users/anisheit/Documents/Python/Videomodul/ArchitektLangsam.wav', 
             '/Users/anisheit/Documents/Python/Videomodul/ArchitektSchnell.wav',
             '/Users/anisheit/Documents/Python/Videomodul/LernvideoSchule.wav',
             '/Users/anisheit/Documents/Python/Videomodul/Werbevideo.wav',
             '/Users/anisheit/Documents/Python/Videomodul/Tire.wav']

"""
wav_file = path to file
taal = lang < ar-IL
key = key
regio = regio
outputfile = name (txttopathname)
"""

def wavtotxtazure(wav_file_path, taal, key, regio, outputfile):
    speech_config = speechsdk.SpeechConfig(subscription=key, region=regio)
    speech_config.speech_recognition_language=taal
    audio_config = speechsdk.audio.AudioConfig(filename=wav_file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    done = False
    output_file = open(outputfile, "w")

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
            # Close the output file and stop the continuous recognition session
        output_file.close()
        speech_recognizer.stop_continuous_recognition()
        print(outputfile)
        nonlocal done
        done = True
        
    def recognized_cb(evt: speechsdk.SpeechRecognitionEventArgs) :
        if speechsdk.ResultReason.RecognizedSpeech==evt.result.reason and len(evt.result.text) > 0 :
            print('RECOGNIZED:', evt.result.text)
            output_file.write(evt.result.text)
            output_file.flush()
            

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('{}'.format(evt)))
    speech_recognizer.recognized.connect(recognized_cb)
    speech_recognizer.session_started.connect(lambda evt: print('{}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('{}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
  
    
    while not done:
        time.sleep(.5)


for i in range(len(pathnames)):
    wavtotxtazure(pathnames[i], 'ar-IL', speechkey, speechregion, txtfrompathname(pathnames[i]))