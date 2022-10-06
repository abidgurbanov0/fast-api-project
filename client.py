import os
from google.cloud import speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
speech_client = speech.SpeechClient()
def functionmain(media_file_name_mp3):

   

    
    with open(media_file_name_mp3, 'rb') as f1:
        byte_data_mp3 = f1.read()
    audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)
    config_mp3 = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='az-AZ'
    )
    config_wav = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='az-AZ',
        audio_channel_count=2
    )
    response_standard_mp3 = speech_client.recognize(
        config=config_mp3,
        audio=audio_mp3
    )
    results = response_standard_mp3.results[0]
    alts = results.alternatives[0]
    return(alts.transcript)

if __name__=="__main__":
   print( functionmain("C:/Users/abidq/OneDrive/Desktop/azreco-asr-python-master/Recording-_3_.mp3"))

