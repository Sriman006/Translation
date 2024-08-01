import pyaudio
import wave
from google.cloud import speech, translate_v2 as translate, texttospeech
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
class AudioRecorder:
    def __init__(self, filename="output.wav", format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024, record_seconds=10):
        self.filename = filename
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.record_seconds = record_seconds
        self.frames = []

    def record_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.format, channels=self.channels,
                            rate=self.rate, input=True,
                            frames_per_buffer=self.chunk)

        print("Recording...")
        for _ in range(0, int(self.rate / self.chunk * self.record_seconds)):
            data = stream.read(self.chunk)
            self.frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

    def save_audio(self):
        with wave.open(self.filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b"".join(self.frames))

        print(f"Audio saved as {self.filename}")

    def transcribe_audio(self):
        """Transcribes the recorded audio using Google Cloud Speech-to-Text."""
        client = speech.SpeechClient()

        with open(self.filename, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.rate,
            language_code="en-US",  # Change to the appropriate language
        )

        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            print("Transcript:", result.alternatives[0].transcript)


    def transcribe_and_translate(self, target_languages):
        """Transcribes audio, translates, and synthesizes speech for each translation."""
        speech_client = speech.SpeechClient()
        translate_client = translate.Client()
        texttospeech_client = texttospeech.TextToSpeechClient()

        with open(self.filename, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.rate,
            language_code="en-US",  # Change to the appropriate source language
        )

        response = speech_client.recognize(config=config, audio=audio)

        for result in response.results:
            text = result.alternatives[0].transcript
            print("Original Text:", text)

            for target_language in target_languages:
                translation = translate_client.translate(text, target_language=target_language)
                translated_text = translation["translatedText"]
                print(f"Translation ({target_language}):", translated_text)

                # Text-to-Speech
                synthesis_input = texttospeech.SynthesisInput(text=translated_text)
                voice = texttospeech.VoiceSelectionParams(
                    language_code=target_language + "-IN", 
                    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                )
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3
                )

                response = texttospeech_client.synthesize_speech(
                    input=synthesis_input, voice=voice, audio_config=audio_config
                )

                output_audio_file = f"translated_{target_language}.mp3"
                with open(output_audio_file, "wb") as out:
                    out.write(response.audio_content)
                    print(f"Audio content written to file: {output_audio_file}")

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.record_audio()
    recorder.save_audio()

    target_languages = ["ta"]  
    recorder.transcribe_and_translate(target_languages)

  























    
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