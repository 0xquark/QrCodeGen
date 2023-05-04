import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = ''
smtp_password = ''

# read email addresses and image filenames from CSV file
with open('recipients.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # extract recipient email address and image filename
        recipient = row[0]
        image_filename = row[1]
        
        # check if the image file exists
        if not os.path.isfile(image_filename):
            print(f'Image file {image_filename} not found. Skipping recipient {recipient}.')
            continue
        
        # set up the email message
        subject = 'Your OSDHack passes'
        body = 'Hi, Say hello to your OSDHack passes! The QR Code attached to this email is unique only to you and will act as your pass throughout the event. Youll be using this QR code for checking-in and marking your attendance at the opening ceremony and during the hacking period.'
        sender = smtp_username
        recipients = [recipient]

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # attach image file to email
        with open(image_filename, 'rb') as f:
            img_data = f.read()
        img = MIMEImage(img_data, name=os.path.basename(image_filename))
        msg.attach(img)

        # send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipients, msg.as_string())
        
        print(f'Email sent to {recipient} with image {image_filename} attached.')

print('All emails sent successfully!')
