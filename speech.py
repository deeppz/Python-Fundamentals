import speech_recognition as sr
import wolframalpha as w

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service" + format(e))

    Client = w.Client('Your APP ID')

    query = (text)
    res = Client.query(query)
    output = next(res.results).text
    print(output)
