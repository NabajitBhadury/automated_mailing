import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from email.mime.image import MIMEImage

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sccse.aot@gmail.com'
# smtp_password = 'tzac lsku thtz czsi ' # gmail resourcio mail
# smtp_password = 'nfdt dovv zqnb qies ' # gmail sccssbs@gmail.com
# smtp_password = 'pbnt pdkt nzdy nbgv' # gmail nabajitbhadury@gmail.com
smtp_password = 'srmu hnqi dgnr psrs'



# Sender and subject configuration
sender = 'sccse.aot@gmail.com'
subject = "Attendence QR for Techquisitive 5.0"


with open('techquisitive_new.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        email = row[1]
        name = row[0]
        try:
            validate_email(email)
        except EmailNotValidError:
            print(f"Invalid email: {email}")
            continue

        # Create a new email message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = subject
        file_path = f'generated_qr/{name}.png'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as binary_file:
                payload = MIMEBase('application', 'octate-stream', Name=f'{name}.png')
                payload.set_payload(binary_file.read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment', filename=f'{name}.png')
                msg.attach(payload)

            body = f'''
            <html>
            <head>

                <title>Congratulations!</title>
                <style>
                    body {{
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
                    }}

                    .container {{
                            max-width: 600px;
    margin: auto;
    padding: 20px;
                    }}

                    h1, h2 {{
                            text-align: center;
                            color: black;
                    }}

                    p {{
                        margin-bottom: 20px;
                    }}

                    p{{
                        font-size: 18px;
                        color: black;
                    }}
                        .right-align {{
                        text-align: right;
                    }}

                </style>
            </head>

<body>
<div class="container">
<h2>Hello {name},</h2>

<p>As informed earlier, <strong>TechQuisitive 5.0</strong> is a Week long Event stretching from 19th to 23rd March.</p>

<p>So, We are sending a <strong>QR Verification Code</strong> which will be an Entry Pass for <strong>ALL Events</strong> under TechQuisitive.</p>

<p>The Team Leader <strong>MUST</strong> show this QR Code to the volunteer during the Entry for the Events, failing to do so will Restrict your Entry in that Event.</p>

<p><strong>This QR Code is also Necessary for providing Attendance/ECA to your Team.</strong></p>

<p><strong>EVERY QR Code is UNIQUE, so PLEASE DON'T SHARE it with other TEAMS.</strong></p>

<p>Note: Every Team Member <strong>MUST carry ID Card or Library Card</strong> for unforeseen Circumstances.</p>

<hr>

<p><strong>BELOW Attachment is Your UNIQUE QR CODE for ALL EVENTS.</strong></p>
<div class="right-align" style="font-size: 18px; color: black;">Regards, SCCSE</div>




</body>

</html>           
 '''

        msg_text = MIMEText(body, 'html')
        msg.attach(msg_text)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        print(f'Sent email to {email}')
