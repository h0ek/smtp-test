# Script to help test SMTP servers/relays and spoof messages
# By hoek from 0ut3r.space

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Mail settings
smtp_server = 'example-smtp.server'
smtp_port = 25
sender_email = 'sender@example.com'
receiver_email = 'recipient@kexample.com'
subject = 'Test Subject'

# HTML message content
html_content = """
<html>
<body>
Test
</body>
</html>
"""

# Creating the message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Adding HTML content to the message
msg.attach(MIMEText(html_content, 'html'))

# Sending the message
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.sendmail(sender_email, receiver_email, msg.as_string())
