import csv
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from email.mime.image import MIMEImage

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'ieee.sb@aot.edu.in'
# smtp_password = 'tzac lsku thtz czsi '
# smtp_password = 'nfdt dovv zqnb qies ' -- SCCSBS
smtp_password = 'ntbc ksnm nhyp ramc'


# Sender and subject configuration
sender = 'ieee.sb@aot.edu.in'
subject = "IEEE SB AOT Membership Offer"


with open('common_emails.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        # email = row[1]
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
        # with open('IEEE.png', 'rb') as img:
        #     mime_img = MIMEImage(img.read())
        # mime_img.add_header('Content-ID', '<header>')
        # msg.attach(mime_img)

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

    <body>
  <div>
    <p>Dear {name},</p>
    <p>I hope this message finds you well. On behalf of the <b>IEEE Student Branch at Academy of Technology (IEEE SB AOT)</b>, we are thrilled to extend a special offer to the top 10 teams of the <b>Uxopia</b> event hosted by the <b>Students' Chapter of CSBS</b> at AOT.</p>
    <p>We understand the dedication and excellence demonstrated by participants in Uxopia, and we believe that fostering connections and providing opportunities for growth within our IEEE community is essential. Therefore, we are delighted to offer a <b>50% discount on IEEE membership fees</b> to members of the <b>Top 10 Teams of Uxopia</b>.</p>
    <p>As part of our commitment to convenience, we have streamlined the registration process for availing this exclusive offer. Here's how you can redeem your discount:</p>
    <p>We are pleased to announce that we are now open to designers who were part of the top 10 teams of Uxopia. Whether you're a graphic designer, UX/UI designer, or any other design enthusiast, we welcome you to join IEEE and explore the vast resources and opportunities available to you.</p>
    <p>To avail of this special offer, please fill out the Google Form provided below:</p>
    <a href="https://forms.gle/s19chUStvgogj5yLA"><font size="4">Click Here</font></a>
    <p>We have simplified the registration process for your convenience. The Google Form will capture your details securely, and upon submission, our team will verify your participation in the top 10 teams of Uxopia and provide you with further instructions on how to proceed with your IEEE membership application at a discounted rate.</p>
    <p>Please note that the registration process will be hidden from public view to ensure the confidentiality and exclusivity of this offer.</p>
    <p><b>This offer is valid till tomorrow 12 pm.</b> Don't miss this opportunity to join IEEE and unlock a world of possibilities in technology and innovation.</p>
    <p>Should you have any questions or require further assistance, please do not hesitate to contact us at <a href="mailto:ieee.sb@aot.edu.in">ieee.sb@aot.edu.in</a>.</p>
    <p>Thank you for your participation in Uxopia, and we look forward to welcoming you to the IEEE community.</p>
    <p>Warm regards,</p>
    <p>IEEE Students Branch<br>Academy of Technology</p>
  </div>
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
