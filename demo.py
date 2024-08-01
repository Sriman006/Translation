# import os
# from google.cloud import speech

# def transcribe_file(file_path):
#     """Transcribes the audio file at the given file path."""

#     # Set environment variable for authentication
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"

#     client = speech.SpeechClient()

#     try:
#         with open(file_path, "rb") as audio_file:
#             content = audio_file.read()
#             audio = speech.RecognitionAudio(content=content)

#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=48000,  # Adjust based on your audio file
#             language_code="en-US",  # Change to your desired language code
#         )

#         response = client.recognize(config=config, audio=audio)

#         for result in response.results:
#             print(result)
#             print("Transcript:", result.alternatives[0].transcript)

#         with  open("samole.txt", "w") as file:
#             file.write(result.alternatives[0].transcript)

#     except FileNotFoundError:
#         print(f"Error: Audio file not found at {file_path}. Please check the path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")



# if __name__ == "__main__":
#     # Replace with your actual audio file path
#     audio_file_path = "Conference (1).wav" 
#     transcribe_file(audio_file_path)\



# from google.cloud import translate_v2 as translate
# import os


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
# def translate_file(input_file, output_file, target_language="ta"):
#     """Translates text in a file to the target language (default: Tamil)."""
#     translate_client = translate.Client()

#     with open(input_file, "r", encoding='utf-8') as f:
#         text = f.read()

#     result = translate_client.translate(text, target_language=target_language)
#     translated_text = result["translatedText"]

#     with open(output_file, "w", encoding='utf-8') as f:
#         f.write(translated_text)

#     print(f"Translation saved to: {output_file}")

# if __name__ == "__main__":
#     input_file = "samole.txt"  # Replace with your input file path
#     output_file = "tamil.txt"  # Replace with your desired output path
#     translate_file(input_file, output_file)




# from google.cloud import texttospeech
# import os 


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"

# from google.cloud import texttospeech

# def synthesize_speech_from_file(input_file, output_file="output.mp3"):
#     """Synthesizes speech from a text file and saves it to an output file."""
#     client = texttospeech.TextToSpeechClient()

#     with open(input_file, "r", encoding='utf-8') as f:
#         text = f.read()

#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="ta-IN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#     )
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )

#     with open(output_file, "wb") as out:
#         out.write(response.audio_content)
#         print(f"Audio content written to file: {output_file}")

# if __name__ == "__main__":
#     input_file = "tamil.txt"  # Replace with your Tamil text file path
#     synthesize_speech_from_file(input_file)














# import pyaudio
# import wave
# from google.cloud import speech, translate_v2 as translate, texttospeech
# import os


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"


# class AudioRecorder:

    
#     def __init__(self, filename="output.wav", format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024, record_seconds=10):
#         self.filename = filename
#         self.format = format
#         self.channels = channels
#         self.rate = rate
#         self.chunk = chunk
#         self.record_seconds = record_seconds
#         self.frames = []

#     def record_audio(self):
#         audio = pyaudio.PyAudio()
#         stream = audio.open(format=self.format, channels=self.channels,
#                             rate=self.rate, input=True,
#                             frames_per_buffer=self.chunk)

#         print("Recording...")
#         for _ in range(0, int(self.rate / self.chunk * self.record_seconds)):
#             data = stream.read(self.chunk)
#             self.frames.append(data)

#         print("Recording finished.")

#         stream.stop_stream()
#         stream.close()
#         audio.terminate()

#     def save_audio(self):
#         with wave.open(self.filename, "wb") as wf:
#             wf.setnchannels(self.channels)
#             wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
#             wf.setframerate(self.rate)
#             wf.writeframes(b"".join(self.frames))

#         print(f"Audio saved as {self.filename}")

#     def transcribe_audio(self):
#         """Transcribes the recorded audio using Google Cloud Speech-to-Text."""
#         client = speech.SpeechClient()

#         with open(self.filename, "rb") as audio_file:
#             content = audio_file.read()

#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=self.rate,
#             language_code="en-US",  # Change to the appropriate language
#         )

#         response = client.recognize(config=config, audio=audio)

#         for result in response.results:
#             print("Transcript:", result.alternatives[0].transcript)

    
#     def translate_and_synthesize(self, source_language, target_language):
#         """Translates and synthesizes speech for a given source and target language."""
#         speech_client = speech.SpeechClient()
#         translate_client = translate.Client()
#         texttospeech_client = texttospeech.TextToSpeechClient()

#         with open(self.filename, "rb") as audio_file:
#             content = audio_file.read()

#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=self.rate,
#             language_code=source_language,
#         )

#         response = speech_client.recognize(config=config, audio=audio)

#         for result in response.results:
#             text = result.alternatives[0].transcript
#             print(f"Original Text ({source_language}):", text)

#             translation = translate_client.translate(text, target_language=target_language)
#             translated_text = translation["translatedText"]
#             print(f"Translation ({target_language}):", translated_text)

#             # Text-to-Speech
#             synthesis_input = texttospeech.SynthesisInput(text=translated_text)
#             voice = texttospeech.VoiceSelectionParams(
#                 language_code=target_language ,
#                 ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#             )
#             audio_config = texttospeech.AudioConfig(
#                 audio_encoding=texttospeech.AudioEncoding.MP3
#             )

#             response = texttospeech_client.synthesize_speech(
#                 input=synthesis_input, voice=voice, audio_config=audio_config
#             )

#             output_audio_file = f"translated_{target_language}.mp3"
#             with open(output_audio_file, "wb") as out:
#                 out.write(response.audio_content)
#                 print(f"Audio content written to file: {output_audio_file}")

# if __name__ == "__main__":
#     recorder = AudioRecorder()
#     source_language = "en-US"  
#     target_language = "ta"    

#     while True:
#         recorder.record_audio()
#         recorder.save_audio()
#         recorder.translate_and_synthesize(source_language, target_language)

        
#         source_language, target_language = target_language, source_language

            






# import pyaudio
# import wave
# from google.cloud import speech, translate_v2 as translate, texttospeech
# import os
# import pygame

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"  # Replace with your JSON key file path

# class AudioRecorder:
#     def __init__(self, filename="output.wav", format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024, record_seconds=10):
#         self.filename = filename
#         self.format = format
#         self.channels = channels
#         self.rate = rate
#         self.chunk = chunk
#         self.record_seconds = record_seconds
#         self.frames = []

#     def record_audio(self):
#         audio = pyaudio.PyAudio()
#         stream = audio.open(format=self.format, channels=self.channels,
#                             rate=self.rate, input=True,
#                             frames_per_buffer=self.chunk)
#         print("Recording...")
#         for _ in range(0, int(self.rate / self.chunk * self.record_seconds)):
#             data = stream.read(self.chunk)
#             self.frames.append(data)
#         print("Recording finished.")
#         stream.stop_stream()
#         stream.close()
#         audio.terminate()

#     def save_audio(self):
#         with wave.open(self.filename, "wb") as wf:
#             wf.setnchannels(self.channels)
#             wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
#             wf.setframerate(self.rate)
#             wf.writeframes(b"".join(self.frames))
#         print(f"Audio saved as {self.filename}")

#     def transcribe_audio(self):
#         """Transcribes the recorded audio using Google Cloud Speech-to-Text."""
#         client = speech.SpeechClient()
#         with open(self.filename, "rb") as audio_file:
#             content = audio_file.read()
#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=self.rate,
#             language_code="en-US",  # Change to the appropriate language
#         )
#         response = client.recognize(config=config, audio=audio)
#         for result in response.results:
#             print("Transcript:", result.alternatives[0].transcript)
#             return result.alternatives[0].transcript  # Return the transcript

#     def translate_text(self, text, source_language, target_language):
#         """Translates text using Google Cloud Translate."""
#         translate_client = translate.Client()
#         translation = translate_client.translate(text, source_language=source_language, target_language=target_language)
#         translated_text = translation["translatedText"]
#         print(f"Translation ({target_language}):", translated_text)
#         return translated_text  # Return the translated text

#     def synthesize_speech(self, text, target_language):
#         """Synthesizes speech from text using Google Cloud Text-to-Speech."""
#         texttospeech_client = texttospeech.TextToSpeechClient()

#         synthesis_input = texttospeech.SynthesisInput(text=text)
#         voice = texttospeech.VoiceSelectionParams(
#             language_code=target_language,
#             ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#         )
#         audio_config = texttospeech.AudioConfig(
#             audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV format
#         )
#         response = texttospeech_client.synthesize_speech(
#             input=synthesis_input, voice=voice, audio_config=audio_config
#         )

#         # Save the synthesized audio as WAV
#         output_audio_file = f"translated_{target_language}.wav"
#         try: 
#             with open(output_audio_file, "wb") as out:
#                 out.write(response.audio_content)
#             print(f"Audio content written to file: {output_audio_file}")
#             return output_audio_file  # Return the output audio file path
#         except PermissionError:
#             print(f"Permission denied: Unable to write file to {output_audio_file}. "
#                 "Please check file permissions or choose a different location.")
#             return None  # Return None if there's an error

#     def play_audio(self, audio_file_path):
#         """Plays audio using Pygame."""
#         try:
#             pygame.mixer.init()
#             pygame.mixer.music.load(audio_file_path)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(100)
#         except Exception as e:
#             print(f"Error playing audio: {e}")

# if __name__ == "__main__":
#     recorder = AudioRecorder()
#     source_language = "en-US"
#     target_language = "ta"

#     while True:
#         recorder.record_audio()
#         recorder.save_audio()
#         transcript = recorder.transcribe_audio()
#         translated_text = recorder.translate_text(transcript, source_language, target_language)
#         if translated_text:
#             audio_file_path = recorder.synthesize_speech(translated_text, target_language)
#             if audio_file_path:
#                 recorder.play_audio(audio_file_path)
#         source_language, target_language = target_language, source_language








from google.cloud import speech, translate_v2 as translate, texttospeech
import os
import pygame
import time
import pyaudio
import threading

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"  # Replace with your JSON key file path

class RealTimeSpeechTranslator:
    def __init__(self):
        self.speech_client = speech.SpeechClient()
        self.translate_client = translate.Client()
        self.texttospeech_client = texttospeech.TextToSpeechClient()
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV format
        )
        pygame.mixer.init()

    def start_realtime_translation(self, user_id, audio_stream, source_language, target_language):
        print(f"User {user_id} started.")
        try:
            while True:
                data = audio_stream.read(1024)
                text = self.transcribe_audio(data, source_language)
                translated_text = self.translate_text(text, source_language, target_language)
                if translated_text:
                    self.synthesize_and_play(translated_text, target_language)
        except KeyboardInterrupt:
            print(f"User {user_id} stopped.")
            audio_stream.stop_stream()
            audio_stream.close()

    def transcribe_audio(self, audio_data, language_code):
        audio = speech.RecognitionAudio(content=audio_data)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,  # Adjust according to your audio sample rate
            language_code=language_code,
        )
        response = self.speech_client.recognize(config=config, audio=audio)
        for result in response.results:
            return result.alternatives[0].transcript

    def translate_text(self, text, source_language, target_language):
     if text:
        translation = self.translate_client.translate(
            text, source_language=source_language, target_language=target_language
        )
        return translation["translatedText"]
     else:
        print("No text provided for translation.")
        return None


    def synthesize_and_play(self, text, language_code):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        response = self.texttospeech_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=self.audio_config
        )
        pygame.mixer.music.load(response.audio_content)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

if __name__ == "__main__":
    translator = RealTimeSpeechTranslator()
    audio_stream_en = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    audio_stream_ta = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    thread_en = threading.Thread(target=translator.start_realtime_translation, args=(1, audio_stream_en, "en-US", "ta"))
    thread_ta = threading.Thread(target=translator.start_realtime_translation, args=(2, audio_stream_ta, "ta", "en-US"))

    thread_en.start()
    thread_ta.start()

    thread_en.join()
    thread_ta.join()
