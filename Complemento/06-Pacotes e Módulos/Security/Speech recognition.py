import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak: ')
    audio = r.listen(source)

    try:
        output = r.recognize_google(audio)
        print('You said {}'.format(output))
    except:
        print('I cant ecognize what you said. Please speak clearly')

