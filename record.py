# import pyaudio
# import wave
# from pydub import AudioSegment
# from pydub.playback import play
# from google.cloud import speech
# from google.cloud import translate_v2 as translate
# import os


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
# def record_audio(file_name, duration):
#     chunk = 1024
#     sample_format = pyaudio.paInt16
#     channels = 1  # Set channels to 1 for mono recording
#     fs = 44100

#     p = pyaudio.PyAudio()

#     stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=fs,
#                     frames_per_buffer=chunk,
#                     input=True)

#     frames = []

#     print("Recording...")
#     for i in range(0, int(fs / chunk * duration)):
#         data = stream.read(chunk)
#         frames.append(data)

#     print("Finished recording.")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     wf = wave.open(file_name, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(sample_format))
#     wf.setframerate(fs)
#     wf.writeframes(b''.join(frames))
#     wf.close()

#     return file_name
# def transcribe_audio(file_name):
#     # Instantiates a client
#     client = speech.SpeechClient()

#     # Loads the audio into memory
#     with open(file_name, "rb") as audio_file:
#         content = audio_file.read()
#         audio = speech.RecognitionAudio(content=content)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         language_code="en-US",  # Change language code as needed
#     )

#     # Detects speech in the audio file
#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
    
#     return response.results 


# def play_audio(file_name):
#     audio = AudioSegment.from_file(file_name)
#     play(audio)


# def translate_text(text, target_language):
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result["translatedText"]

# if __name__ == "__main__":
#     file_name = "recorded_audio.wav"
#     duration = 10 

#     while True:
#         recorded_file = record_audio(file_name, duration)
#         print(f"Audio recorded and saved as {recorded_file}")

#         print("Transcribing audio...")
#         transcript = transcribe_audio(recorded_file)

#         if transcript:
#             # Get the first transcript (assume single speaker for simplicity)
#             text = transcript[0].alternatives[0].transcript
#             print("Transcript:", text)

#             # Ask for target language
#             target_language = input("Enter target language code (e.g., 'es', 'fr', 'ja'): ")

#             # Translate and print the result
#             translated_text = translate_text(text, target_language)
#             print("Translation:", translated_text)

#         # Play the recorded audio
#         print("Playing recorded audio...")
#         play_audio(recorded_file)

#         # Add an option to break the loop
#         choice = input("Record again? (y/n): ")
#         if choice.lower() != 'y':
#             break
















# import pyaudio
# import wave
# from pydub import AudioSegment
# from pydub.playback import play
# from google.cloud import speech
# from google.cloud import translate_v2 as translate
# import os


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
# def record_audio(file_name, duration):
#     chunk = 1024
#     sample_format = pyaudio.paInt16
#     channels = 1  # Set channels to 1 for mono recording
#     fs = 44100

#     p = pyaudio.PyAudio()

#     stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=fs,
#                     frames_per_buffer=chunk,
#                     input=True)

#     frames = []

#     print("Recording...")
#     for i in range(0, int(fs / chunk * duration)):
#         data = stream.read(chunk)
#         frames.append(data)

#     print("Finished recording.")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     wf = wave.open(file_name, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(sample_format))
#     wf.setframerate(fs)
#     wf.writeframes(b''.join(frames))
#     wf.close()

#     return file_name
# def transcribe_audio(file_name):
#     # Instantiates a client
#     client = speech.SpeechClient()

#     # Loads the audio into memory
#     with open(file_name, "rb") as audio_file:
#         content = audio_file.read()
#         audio = speech.RecognitionAudio(content=content)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         language_code="en-US",  # Change language code as needed
#     )

#     # Detects speech in the audio file
#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
    
#     return response.results 


# def play_audio(file_name):
#     audio = AudioSegment.from_file(file_name)
#     play(audio)



# def translate_text(text, target_language):
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result["translatedText"]

# def save_transcript(file_name, text):
#     with open(file_name, "w", encoding="utf-8") as f:
#         f.write(text)

# def translate_file(input_file, output_file, target_language):
#     with open(input_file, "r") as f:
#         text = f.read()
#     translated_text = translate_text(text, target_language)
#     save_transcript(output_file, translated_text)

# if __name__ == "__main__":
#     audio_file_name = "recorded_audio.wav"
#     transcript_file_name = "transcript.txt"
#     translated_file_name = "translated_text.txt"
#     duration = 5

#     while True:
#         recorded_file = record_audio(audio_file_name, duration)
#         print(f"Audio recorded and saved as {recorded_file}")

#         print("Transcribing audio...")
#         transcript = transcribe_audio(recorded_file)

#         if transcript:
#             # Get the first transcript (assume single speaker for simplicity)
#             text = transcript[0].alternatives[0].transcript
#             print("Transcript:", text)

#             # Save the transcript to a file
#             save_transcript(transcript_file_name, text)
#             print(f"Transcript saved to {transcript_file_name}")

#             # Ask for target language
#             target_language = input("Enter target language code (e.g., 'es', 'fr', 'ja'): ")

#             # Translate the saved transcript file
#             translate_file(transcript_file_name, translated_file_name, target_language)
#             print(f"Translation saved to {translated_file_name}")

#         # Play the recorded audio
#         print("Playing recorded audio...")
#         play_audio(recorded_file)

#         # Add an option to break the loop
#         choice = input("Record again? (y/n): ")
#         if choice.lower() != 'y':
#             break




# import pyaudio
# import wave
# from pydub import AudioSegment
# from pydub.playback import play
# from google.cloud import speech
# from google.cloud import translate_v2 as translate
# import os


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
# def record_audio(file_name, duration):
#     chunk = 1024
#     sample_format = pyaudio.paInt16
#     channels = 1  # Set channels to 1 for mono recording
#     fs = 44100

#     p = pyaudio.PyAudio()

#     stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=fs,
#                     frames_per_buffer=chunk,
#                     input=True)

#     frames = []

#     print("Recording...")
#     for i in range(0, int(fs / chunk * duration)):
#         data = stream.read(chunk)
#         frames.append(data)

#     print("Finished recording.")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     wf = wave.open(file_name, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(sample_format))
#     wf.setframerate(fs)
#     wf.writeframes(b''.join(frames))
#     wf.close()

#     return file_name
# def transcribe_audio(file_name, language_code):
#     # Instantiates a client
#     client = speech.SpeechClient()

#     # Loads the audio into memory
#     with open(file_name, "rb") as audio_file:
#         content = audio_file.read()
#         audio = speech.RecognitionAudio(content=content)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         language_code=language_code,  # Change language code as needed
#     )

#     # Detects speech in the audio file
#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
    
#     return response.results 


# def play_audio(file_name):
#     audio = AudioSegment.from_file(file_name)
#     return audio



# def translate_text(text, target_language):
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result["translatedText"]

# def save_transcript(file_name, text):
#     with open(file_name, "w", encoding="utf-8") as f:
#         f.write(text)

# def translate_file(input_file, output_file, target_language):
#     with open(input_file, "r", encoding="utf-8") as f:  # Add encoding here
#         text = f.read()
#     translated_text = translate_text(text, target_language)
#     save_transcript(output_file, translated_text)

# if __name__ == "__main__":
#     audio_file_name = "recorded_audio.wav"
#     transcript_file_name = "transcript.txt"
#     translated_file_name = "translated_text.txt"
#     duration = 5

#     while True:
#         # Ask for source language
#         source_language = input("Enter source language code (e.g., 'en-US', 'es-ES', 'hi-IN'): ")

#         recorded_file = record_audio(audio_file_name, duration)
#         print(f"Audio recorded and saved as {recorded_file}")

#         print("Transcribing audio...")
#         transcript = transcribe_audio(recorded_file, source_language)

#         if transcript:
#             # Get the first transcript (assume single speaker for simplicity)
#             text = transcript[0].alternatives[0].transcript
#             print("Transcript:", text)

#             # Save the transcript to a file
#             save_transcript(transcript_file_name, text)
#             print(f"Transcript saved to {transcript_file_name}")

#             # Ask for target language
#             target_language = input("Enter target language code (e.g., 'es', 'fr', 'ja'): ")

#             # Translate the saved transcript file
#             translate_file(transcript_file_name, translated_file_name, target_language)
#             print(f"Translation saved to {translated_file_name}")

#         # Play the recorded audio
#         print("Playing recorded audio...")
#         play_audio(recorded_file)

#         # Add an option to break the loop
#         choice = input("Record again? (y/n): ")
#         if choice.lower() != 'y':
#             break






import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
from google.cloud import speech
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
import os
from pydub.utils import mediainfo
from pydub.utils import which 

# Specify the path to ffprobe (if not in your PATH)
ffprobe_path = r"C:\Users\ADMIN\Downloads\ffmpeg-7.0\bin"  # Replace with the actual path if needed

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"  # Replace with your service account key file path

def record_audio(file_name, duration):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    print("Recording...")
    for i in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    return file_name

def transcribe_audio(file_name, language_code):
    client = speech.SpeechClient()
    with open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code=language_code,
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
    return response.results

def play_audio(file_name):
    ffprobe_path = which("ffprobe")  # Find ffprobe using 'which'
    if ffprobe_path is None:
        print("ffprobe not found. Please install FFmpeg and ensure it's in your PATH.")
        return

    audio_info = mediainfo(file_name)
    audio = AudioSegment.from_file(file_name, format=audio_info["format_name"])
    play(audio)

def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result["translatedText"]

def save_transcript(file_name, text):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text)

def translate_file(input_file, output_file, target_language):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    translated_text = translate_text(text, target_language)
    save_transcript(output_file, translated_text)

def text_to_speech(text, output_file, language_code):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_file}"')


if __name__ == "__main__":
    audio_file_name = "recorded_audio.wav"
    transcript_file_name = "transcript.txt"
    translated_file_name = "translated_text.txt"
    duration = 5

    while True:
        source_language = input("Enter source language code (e.g., 'en-US', 'es-ES', 'hi-IN'): ")
        recorded_file = record_audio(audio_file_name, duration)
        print(f"Audio recorded and saved as {recorded_file}")
        print("Transcribing audio...")
        transcript = transcribe_audio(recorded_file, source_language)

        if transcript:
            text = transcript[0].alternatives[0].transcript
            print("Transcript:", text)
            save_transcript(transcript_file_name, text)
            print(f"Transcript saved to {transcript_file_name}")
            target_language = input("Enter target language code (e.g., 'es', 'fr', 'ja'): ")
            translate_file(transcript_file_name, translated_file_name, target_language)
            print(f"Translation saved to {translated_file_name}")

            # Read the translated text from the file
            with open(translated_file_name, "r", encoding="utf-8") as f:
                translated_text = f.read()

            # Get language code for text-to-speech from target language
            target_language_code = target_language.split("-")[0] 
            output_audio_file = "translated_audio.mp3"
            text_to_speech(translated_text, output_audio_file, target_language_code)

            print("Playing translated audio...")
            play_audio(output_audio_file)  # Using the modified play_audio function

        choice = input("Record again? (y/n): ")
        if choice.lower() != 'y':
            break 