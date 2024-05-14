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
smtp_username = 'resourciocommunity22@gmail.com'
smtp_password = 'tzac lsku thtz czsi '

# Sender and subject configuration
sender = 'resourciocommunity22@gmail.com'
subject = "🚀 Greetings this is a remainder mail for Apertre 24! 🚀"


with open('menteeList3.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        name = row[1]
        email = row[16]
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
        with open('img.png', 'rb') as img_file:
            # Create a MIMEImage object
            img1 = MIMEImage(img_file.read())
        img1.add_header('Content-ID', '<myimage1>')
        msg.attach(img1)

        with open('Contributor Card.png', 'rb') as img_file:
            img2 = MIMEImage(img_file.read())

        img2.add_header('Content-ID', '<myimage2>')
        msg.attach(img2)

        body = f'''
<html>
<head>

    <title>Congratulations!</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 20px;
        }}

        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}

        h1 {{
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }}

        p {{
            color: #0e0d0d;
            font-size: 16px;
            line-height: 1.5;
            margin-bottom: 10px;
        }}

        a {{
            color: #007bff;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>

<body>
    <div class="container">
        <img src="cid:myimage1" alt="Banner" style="width: 100%; height: auto;">
        <h1 style="color: #333; font-size: 24px; margin-bottom: 20px; text-align: center;"> 🚀Congratulations: You're In
            for an Epic Tech Adventure with Apertre'24 🚀</h1>
        <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Greetings {name},❤️</b></p>
        <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">We're over the moon to
            announce that you've been handpicked as a mentee/contributor for <i>Apertre'24
                - an electrifying 15-day-long open-source event powered by the dynamic collaboration of</i> <b>Resourcio Community</b> and <b>Google Developer Student Clubs - Academy Of
                Technology!</b></p>
       <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;"> 
    Now, buckle up for a 15-day rollercoaster of innovation in our open-source program! Brace yourself for skill-boosting opportunities in web development, mobile development, machine learning, and more. It's your chance to gain hands-on experience, sculpt an impressive portfolio, and soar towards your professional tech goals.📈
</p>
<p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Instructions: (All are
    mandatory)⚠️
</p>
<ul>
<li style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">
    We request you to join the given Discord server to get the latest details of the program. Join our
    Discord server - <a href="https://discord.com/invite/7vypmaSETr"
        style="color: #007bff; text-decoration: none;">here</a>
</li>
<li style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Once you join the
                <b>Discord</b> server, please check the <b><a href="https://discord.com/channels/1158734803231854722/1169892852776566925/1188037293001412609" style="color:  #007bff; text-decoration: none;">🍹・announcements</a></b> channel to stay updated and make sure you
                don't miss anything important throughout the program.</li>
    <li style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Sign Up here - <a
            href="https://quine.sh/?utm_source=apertre" style="color: #007bff; text-decoration: none;">Quine</a>
    </li>
    <li style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Don't forget to check
        our website - <a href="https://os.apertre.tech/"
            style="color: #007bff; text-decoration: none;">Apertre'24</a>
    </li>
</ul>
        <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Find the Mentor
            Card for <b>Apertre'24</b> We are super excited to see the tickets flying all over the social media
            platforms!
            So don't forget to tag us and post your tickets!🎟️
        <p>📍Tag us here
            - <a href="https://www.linkedin.com/showcase/apertre/"
                style="color: #007bff; text-decoration: none;">LinkedIn</a></p>
        <img src="cid:myimage2" alt="Mentee Card"
            style="display: block ;width: 50%; height: auto; margin: auto;margin-top: 60px; margin-bottom: 60px;">
        <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Stay in the loop with Apetre
            by connecting to our social media pages. They're not just platforms; they're your golden ticket to
            networking with fellow participants, mentors, and program organizers. Plus, you'll be the first to know
            about thrilling events, webinars, and contests in our vibrant community.<br>
            Congrats once again🥳!</p>
        <p style="color: #0e0d0d; font-size: 16px; line-height: 1.5; margin-bottom: 10px;">Best Regards,<br>Apertre'24
            Team
        </p>
    </div>
</body>

</html>
'''

        msg_text = MIMEText(body, 'html')
        msg.attach(msg_text)

        with open('Contributor Card.png', 'rb') as attachment_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_file.read())

        # Encode the attachment in base64
        encoders.encode_base64(part)

        # Add the attachment to the message
        part.add_header('Content-Disposition', f'attachment; filename= Contributor Card.png')
        msg.attach(part)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        print(f'Sent email to {email}')
