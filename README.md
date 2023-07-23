# Voice based E-mail for the Blind


## About:

The voice-based email system for visually challenged users is implemented in this Python script. The programme makes use of the speech_recognition, pyttsx3, and smtplib libraries to perform voice recognition, text-to-speech, and email sending via the Gmail SMTP server, respectively.

The functionality of the code is listed here in brief:
- Text-to-Speech Output: To provide the user with synthesised speech, the programme makes use of the pyttsx3 package. The user is guided through each stage of sending an email by the spoken output.

- Information about the user's Gmail account is requested, including their email address and password. These credentials are used for email authentication.

- User Input for Recipient and Message: The user is asked for the recipient's full email address as well as the message they wish to send.

- The code creates the sender and receiver email addresses using the supplied username and the domain @gmail.com, which implies that the user's email address is linked to Gmail.

- Voice Feedback: The programme employs voice feedback and prompts to help the user through the process and let them know what activities are being taken.

With the use of this code, visually impaired people will be able to send emails using voice commands, making it simpler for them to use technology and communicate with others via email. Please be aware that using email credentials within a script could have security repercussions, and that it's crucial to handle sensitive information with care and make sure that the necessary security safeguards are in place.


### This code can be improved by uisng an AI model for speech to text conversion. Thus improving the results of the code.
