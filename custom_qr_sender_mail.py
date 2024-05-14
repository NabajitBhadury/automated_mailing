import csv
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError
from email.mime.image import MIMEImage

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sccsbbs@gmail.com'
# smtp_password = 'tzac lsku thtz czsi '
smtp_password = 'nfdt dovv zqnb qies '


# Sender and subject configuration
sender = 'sccsbbs@gmail.com'
subject = "SCCSBS Inaugaration Invitation"


with open('SCCSBS_emails.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        email = row[1].strip()
        filename = f'generated_qr/{name}.png'

        try:
            validate_email(email)
        except EmailNotValidError:
            print(f"Invalid email: {email}")
            continue

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = subject
        with open('SCCSBS_img.png', 'rb') as img:
            mime_img = MIMEImage(img.read())
        mime_img.add_header('Content-ID', '<header>')
        msg.attach(mime_img)

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
                            color: black;
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
                        font-size: 16px;
                        color: black;
                    }}

                    ul{{
                        font-size: 16px;
                        color: black;
                    }}

                </style>
            </head>

<body>
    <div>
        <div class="container">
        <img src="cid:header" alt="Header Image" style="width: 100%;">
        <h1>🎉 Join Us for UXopia Event Tomorrow!</h1>
        <p>Come and join us on 2nd April, tomorrow! See your slot from those PDFs and join us with the unique QR code.</p>
        <p>📚 All the best for AOT's first UI/UX event, UXopia! Let's have fun together! 🎨 It's not just an event of study; it's an event of fun, like Nicco Park and Aquatica! 🎢 Remember that... Let's make it a memorable experience!</p>
        <p>Here is your submission form link - <a href="https://forms.gle/6vdiDR8vbGfAHwsN9">Submission Form</a> (We will open it when needed. It's currently not accepting any responses. 1 member from each team have to fill this form to submit their project)</p>
        <p>N.B.-</p>
        <ul>
            <li>To take your ECA (Extra Curricular Activities) scanning the QR for each participant is mandatory.</li>
            <li>For your clarity, we are also sharing the rules book.</li>
            <li>Also you can bring your own extension chord for power supply if possible.</li>
        </ul>
        <p>Thanks and Regards<br>SC CSBS</p>
    </div>
</body>
</html>           
 '''

        msg_text = MIMEText(body, 'html')
        msg.attach(msg_text)

        try:
            with open(filename, 'rb') as attachment_file:
                part1 = MIMEBase('application', 'octet-stream')
                part1.set_payload(attachment_file.read())
        except FileNotFoundError:
            print(f"No file found for {filename}")
            continue

        pdf_path1 = 'Slot 1.pdf'
        try:
            with open(pdf_path1, 'rb') as attachment_file:
                part2 = MIMEBase('application', 'octet-stream')
                part2.set_payload(attachment_file.read())
        except FileNotFoundError:
            print(f"No file found")
            continue

        pdf_path2 = 'Slot 2.pdf'
        try:
            with open(pdf_path2, 'rb') as attachment_file:
                part3 = MIMEBase('application', 'octet-stream')
                part3.set_payload(attachment_file.read())
        except FileNotFoundError:
            print(f"No file found")
            continue

        pdf_path3 = 'UXopia Rules.pdf'
        try:
            with open(pdf_path3, 'rb') as attachment_file:
                part4 = MIMEBase('application', 'octet-stream')
                part4.set_payload(attachment_file.read())
        except FileNotFoundError:
            print(f"No file found")
            continue

        encoders.encode_base64(part1)
        encoders.encode_base64(part2)
        encoders.encode_base64(part3)
        encoders.encode_base64(part4)

        part1.add_header('Content-Disposition',
                         f'attachment; filename= {filename}')
        msg.attach(part1)

        part2.add_header('Content-Disposition',
                         f'attachment; filename= {pdf_path1}')
        msg.attach(part2)

        part3.add_header('Content-Disposition',
                         f'attachment; filename= {pdf_path2}')
        msg.attach(part3)

        part4.add_header('Content-Disposition',
                         f'attachment; filename= {pdf_path3}')
        msg.attach(part4)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        print(f'Sent email to {email}')
