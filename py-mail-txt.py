# Script to help test SMTP servers/relays and spoof messages
# By hoek from 0ut3r.space

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# Setting the sender's e-mail address
from_email = sender@example.com

# Setting the recipient's e-mail address
to_email = recipient@kexample.com

# Setting an e-mail subject
subject = "Test Subject"

# Setting the e-mail content
body = "Test Body"

# Creation of a MIMEMultipart object
msg = MIMEMultipart()

# Setting the headings
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = Header(subject, "utf-8")

# Setting custom headers
msg.add_header("MIME-Version", "1.0")
msg.add_header("Content-Type", "application/ms-tnef; name=\"winmail.dat\"")
msg.add_header("Content-Transfer-Encoding", "binary")

# Create email content as MIMEText
body_content = MIMEText(body, "plain")

# Attaching the e-mail content to the message
msg.attach(body_content)

# Setting up the SMTP server
smtp_server = "example-smtp.server"
smtp_port = 25

# Establishing an SMTP connection
server = smtplib.SMTP(smtp_server, smtp_port)

# Sending an e-mail
server.send_message(msg)

# Closing the SMTP connection
server.quit()
