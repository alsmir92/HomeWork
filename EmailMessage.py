from email.message import EmailMessage
import smtplib

my_email = EmailMessage()

my_email['from'] = 'Alex'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = "Hello from Python"
my_email.set_content()

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
