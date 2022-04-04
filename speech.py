import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(
                audio_data=audio, language="en-US")
            text = text.lower()

            print(f"Recognized: {text}")
            if text == 'stop':
                break

    except:
        recognizer = speech_recognition.Recognizer()
        continue
