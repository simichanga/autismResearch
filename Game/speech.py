import speech_recognition
#pip install pipwin
#pipwin install pyaudio
#sudo apt-get install python3-pyaudio

def speech_test():
    recognizer = speech_recognition.Recognizer()
    while True:

        try:

            with speech_recognition.Microphone() as source:

                print("You can speak!")
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio)
                print('Recognized : {}'.format(text))

        except:
            #speech_recognition.UnknownValueError():
            print("Sorry could not recognize your voice! Try again to speak!")
            recognizer = speech_recognition.Recognizer()
            continue

speech_test()
