import os
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import boto3

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Voice Translator")

        self.translator = Translator()
        self.recognizer = sr.Recognizer()

        self.lang_codes = {
            "Portuguese Brazil": "pt",
            "English": "en",
            "Polish": "pl",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Dutch": "nl",
            "Russian": "ru",
            # Adicione outras línguas aqui
        }

        self.voice_map = {
            'en': {'male': 'Matthew', 'female': 'Joanna', 'neural': 'Matthew-Neural'},
            'pt': {'male': 'Ricardo', 'female': 'Vitoria', 'neural': 'Vitoria-Neural'},
            'de': {'male': 'Hans', 'female': 'Marlene', 'neural': 'Vicki-Neural'},
            'pl': {'male': 'Jan', 'female': 'Ewa', 'neural': 'Maja-Neural'},
            'es': {'male': 'Enrique', 'female': 'Conchita', 'neural': 'Mia-Neural'},
            'fr': {'male': 'Mathieu', 'female': 'Lea', 'neural': 'Celine-Neural'},
            # Adicione vozes para outras línguas aqui
        }

        self.black_hole_active = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Choose a TTS system:").pack()
        self.tts_choice = ttk.Combobox(self.root, values=["TTS-1", "TTS-2", "TTS-3'"])
        self.tts_choice.pack()

        ttk.Label(self.root, text="Choose the input language:").pack()
        self.lang_input_choice = ttk.Combobox(self.root, values=list(self.lang_codes.keys()))
        self.lang_input_choice.pack()

        ttk.Label(self.root, text="Choose the output language:").pack()
        self.lang_output_choice = ttk.Combobox(self.root, values=list(self.lang_codes.keys()))
        self.lang_output_choice.pack()

        ttk.Label(self.root, text="Choose a voice:").pack()
        self.voice_choice = ttk.Combobox(self.root, values=["Male", "Female"])
        self.voice_choice.pack()

        ttk.Label(self.root, text="Voice Type:").pack()
        self.voice_type_choice = ttk.Combobox(self.root, values=["Standard", "Neural"])
        self.voice_type_choice.pack()

        self.black_hole_toggle = ttk.Checkbutton(self.root, text="Activate Black Hole", variable=self.black_hole_active)
        self.black_hole_toggle.pack()

        self.translate_button = ttk.Button(self.root, text="Start Translation", command=self.start_translation)
        self.translate_button.pack()

        self.output_text = tk.Text(self.root, height=10, width=40)
        self.output_text.pack()

    def play_text_as_speech(self, text, lang='en'):
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save("temp.mp3")
            os.system("afplay temp.mp3")  # Ajuste para o seu sistema
            os.remove("temp.mp3")
        except Exception as e:
            print(f"Error in TTS: {e}")

    def play_text_with_tts(self, text, lang='en', gender='male'):
        try:
            voice_type = 'neural' if self.voice_type_choice.get() == "Neural" else 'standard'
            voice_id = self.voice_map[lang][gender if voice_type != 'neural' else 'neural']

            polly = boto3.client('polly')
            response = polly.synthesize_speech(Text=text, VoiceId=voice_id, OutputFormat='mp3', Engine=voice_type)

            with open("temp.mp3", "wb") as f:
                f.write(response['AudioStream'].read())

            os.system("afplay temp.mp3")
            
            if self.black_hole_active.get():
                # Suponhamos que o black hole seja um local para enviar o arquivo.
                # Altere a função 'send_to_black_hole' conforme necessário.
                self.send_to_black_hole("temp.mp3")
            else:
                os.remove("temp.mp3")
        except Exception as e:
            print(f"Error using TTS system: {e}")

    def send_to_black_hole(self, file_path):
        # Implemente o método de enviar o arquivo para o "black hole" aqui.
        pass

    def start_translation(self):
        self.translate_button["text"] = "Listening... Speak now!"
        self.root.update()

        tts_choice = self.tts_choice.get()
        lang_input = self.lang_codes.get(self.lang_input_choice.get(), 'en')
        lang_output = self.lang_codes.get(self.lang_output_choice.get(), 'en')
        gender = 'male' if self.voice_choice.get() == "Male" else 'female'

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio_data = self.recognizer.listen(source)

            try:
                recognized_text = self.recognizer.recognize_google(audio_data, language=lang_input)
                translation = self.translator.translate(recognized_text, src=lang_input, dest=lang_output).text

                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Original Text: {recognized_text}\nTranslated Text: {translation}")

                if tts_choice == "TTS-1":
                    self.play_text_as_speech(translation, lang_output)
                elif tts_choice == "TTS-2":
                    self.play_text_with_tts(translation, lang_output, gender)
                elif tts_choice == "TTS-3'":
                    os.system(f"say {translation}")

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

        self.translate_button["text"] = "Start Translation"

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
