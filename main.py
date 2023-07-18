import pyttsx3
import smtplib, ssl
import speech_recognition as sr

def text():
    r = sr.Recognizer()
    #set microphone
    with sr.Microphone() as source:
        #waiting time
        r.pause_threshold = 0.5
        #report that recording has begun
        print("You can now speak")
        #save what you hear as audio
        audio = r.listen(source)
        try:
            # Search on google
            request = r.recognize_google(audio, language="en-gb")

            # test in text
            print("You said " + request)

            # return request
            return request

            # in case it doesn't understand the audio
        except sr.UnknownValueError:

            # show proof that it didn't understand the audio
            print("Ups! Didn't understand the audio")

            # return error
            return "I am still waiting"
            # in case the request cannot be resolved
        except sr.RequestError:
            # show proof that it didn't understand the audio
            print("Ups! there is no service")

            # return error
            return "I am still waiting"
            # Unexpected Error
        except:
            # show proof that it didn't understand the audio
            print("Ups! Something went wrong")

            # return error
            return "I am still waiting"



def speech(message):
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',
                        voices[1].id)  # Voice used is female, for male voice speaker.setProperty('voice', voices[0].id)
    rate = speaker.getProperty('rate')  # getting details of current speaking rate
    speaker.setProperty('rate', 125)
    speaker.say(message)
    speaker.runAndWait()


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
to_add="Provide the complete mail address of the person to whom you want to send the mail like for abcd@gmail.com say abcd"
from_add="Provide your mail id like for abcd@gmail.com say abcd"
password1="Your mail id Password"
mess="What is your message"
speech(from_add)
sender_email = text().lower() +"@gamil.com"
speech(to_add)
receiver_email = text().lower() +"@gmail.com" # Enter receiver address
speech(password1)
password = text().lower()
speech(mess)
message = text().lower()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
