from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Alex', 'date': 'tomorrow'})

my_email['from'] = 'Alex <bs@gmail.com'
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Email with image"
my_email.set_content(html_content, 'html')

with open('images/пикча.jpg', 'rb') as img:
    image_data = img.read()
    my_email. add_attachment(image_data, maintype='image',
                             subtype='jpg', filename='пикча.jpg')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
