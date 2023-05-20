import io
import requests
from io import BytesIO
from pydub import AudioSegment

url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"

token="eyJhbGciOiJFUzI1NiIsImtpZCI6ImtleTEiLCJ0eXAiOiJKV1QifQ.eyJyZWdpb24iOiJlYXN0dXMiLCJzdWJzY3JpcHRpb24taWQiOiI0NjA2NzU0YmMwYTQ0OTJmYTkyYjU1YWVhMWE5MTdhMyIsInByb2R1Y3QtaWQiOiJTcGVlY2hTZXJ2aWNlcy5TMCIsImNvZ25pdGl2ZS1zZXJ2aWNlcy1lbmRwb2ludCI6Imh0dHBzOi8vYXBpLmNvZ25pdGl2ZS5taWNyb3NvZnQuY29tL2ludGVybmFsL3YxLjAvIiwiYXp1cmUtcmVzb3VyY2UtaWQiOiIvc3Vic2NyaXB0aW9ucy9jNzFiNjA1ZC1jMjlmLTQzMTgtYjY1Yy02MDU0YTg1ZTllYTQvcmVzb3VyY2VHcm91cHMvQXR1YmVyL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29nbml0aXZlU2VydmljZXMvYWNjb3VudHMvQXR1YmVyLXZvaWNlIiwic2NvcGUiOiJzcGVlY2hzZXJ2aWNlcyIsImF1ZCI6InVybjptcy5zcGVlY2hzZXJ2aWNlcy5lYXN0dXMiLCJleHAiOjE2ODQwNzk5NTcsImlzcyI6InVybjptcy5jb2duaXRpdmVzZXJ2aWNlcyJ9.-EIaxyENQCYFm3KCg2Yf0NA5qpsF4UJmniVE9hxWeb3mvWwj_A40MbTo2qf9sb7LzHTaOKWGzrTBPZsSf5d8RA"
headers = {
    "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    "Content-Type": "application/ssml+xml",
    "Host": "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1",
    "Authorization": "Bearer "+token,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
}
payload = "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Male' name='en-US-ChristopherNeural'>Microsoft Speech Service Text to speech API</voice></speak>"

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    # Read the audio data from the response
    audio_data = BytesIO(response.content)

    # Convert the audio data to an MP3 file
    audio_segment = AudioSegment.from_file(audio_data, format="wav")
    audio_segment.export("output.mp3", format="mp3")

    print("Successfully saved audio to output.mp3!")
else:
    print(f"Error: {response.status_code} - {response.text}")