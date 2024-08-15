import speech_recognition as sr
import webbrowser
import pyttsx3             # library for text_to_speech
import FvrtSong
import pyjokes             # library for telling jokes

class JarvisAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def process_command(self, command):
        # print("Command received: working on it..just wait")
        command = command.lower()

        if "open google" in command:
            webbrowser.open("https://google.com")
            self.speak("Opening Google.")
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            self.speak("Opening YouTube.")
        elif "open facebook" in command:
            webbrowser.open("https://facebook.com")
            self.speak("Opening Facebook.")
        elif "open instagram" in command:
            webbrowser.open("https://instagram.com")
            self.speak("Opening Instagram.")
        elif "open linkedin" in command:
            webbrowser.open("https://linkedin.com")
            self.speak("Opening linkedin.")    
        elif command.startswith("play"):
            song = command.split(" ", 1)[1]
            if song in FvrtSong.music:
                play = FvrtSong.music[song]
                webbrowser.open(play)
                self.speak(f"Playing {song}.")
            else:
                self.speak("Sorry, I couldn't find the song.")
        elif "joke" in command:
            joke = pyjokes.get_joke(language="en")        
            self.speak(joke)
        else:
            self.speak("Sorry, I didn't understand that command.")

    def listen_for_command(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                word = self.recognizer.recognize_google(audio)
                if word.lower() == 'jarvis':
                    self.speak("Ahaann")
                    # Listening for command now
                    with sr.Microphone() as source:
                        print("Jarvis activated...")
                        audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = self.recognizer.recognize_google(audio)
                        self.process_command(command)
        
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    jarvis = JarvisAssistant()
    jarvis.speak("Initializing Jarvis.")
    while True:
        jarvis.listen_for_command()
