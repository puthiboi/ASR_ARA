"""
    Gemini Speech To Text habe ich direkt über Google Cloud Shell gemacht um Zeit zu sparen.
    Nach dem Run, habe ich print ausgaben in txt Files kopiert.
    Hier der Code den ich dafür verwendet habe.
"""

from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://ansitranskriptbucket/Test 10 Seconds.mp3"
gcs_uris = ["gs://ansitranskriptbucket/test10sek.mp3", 
            "gs://ansitranskriptbucket/Arabic Content/AlJazeera.mp3", 
            "gs://ansitranskriptbucket/Arabic Content/ArchitektLangsam.mp3", 
            "gs://ansitranskriptbucket/Arabic Content/ArchitektSchnell.mp3",
            "gs://ansitranskriptbucket/Arabic Content/LernvideoSchule.mp3",
            "gs://ansitranskriptbucket/Arabic Content/Tire.mp3",
            "gs://ansitranskriptbucket/Arabic Content/Werbevideo.mp3"]

def transcribe_speech(file):
  audio = speech.RecognitionAudio(uri=file) #uri=gcs_uri

  config = speech.RecognitionConfig(
      #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      encoding=speech.RecognitionConfig.AudioEncoding.MP3,
      sample_rate_hertz=16000,
      language_code="ar-IL",
  )
  #encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

  # Detects speech in the audio file
  #response = client.recognize(config=config, audio=audio)
  # Detects speech in the audio file using long-running recognition
  operation = client.long_running_recognize(config=config, audio=audio)
  print(f"Waiting for operation to complete on {file}...")
  response = operation.result(timeout=900)

  for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))


#transcribe_speech()

for i in range(len(gcs_uris)):
    transcribe_speech(gcs_uris[i])
    print("\n")