# AzReco Speech Recognition API Python example
Example python script to help you integrate with our speech recognition API.

This is an example python script for uploading audio(.wav , .mp3 , .opus, .m4a) or video(.mp4 , .mkv) file and saving the transcript into a .json file.
You can also transcribe youtube,facebook,twitter,dailymotion public video links. In this sample code we match if audio input is link or file. 
There are two different api to transcribe: [/transcribe] and [/transcribe_video_link]. We call [/transcribe] for audio or video files, [/transcribe_video_link] for video links.



# Supporting languages
AZERBAIJANI (az-AZ)

TURKISH  (tr-TR)

RUSSIAN  (ru-RU)

# Requirements

You will need to have the requests module installed in your Python environment.

pip install requests

# Usage example:

python client.py -a audio/example-ru.wav -l ru-RU -i api_user_id -k api_token -o example-ru.json  

In this example the script uploads 'example.wav', transcribes it using our ru-RU speech to text and saves the resulting transcription as 'example.json' when the transcribing process finished.

python client.py -a 'https://www.youtube.com/watch?v=dSJjkiuy' -l ru-RU -i api_user_id -k api_token -o example-ru.json

In this example the script sends link to the server, transcribes it using our ru-RU speech to text and saves the resulting transcription as 'example-ru.json' when the transcribing process finished.

# How to get user id and token?

To get user id and API token, send a request to info@azreco.az.
To confirm your request, we will ask you some details about your purpose in using API.
