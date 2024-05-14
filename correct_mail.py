import csv
from email_validator import validate_email, EmailNotValidError

def is_valid_email(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False

with open('participants.csv', 'r') as f, open('valid_emails.csv', 'w', newline='') as out_file:
    reader = csv.reader(f)
    writer = csv.writer(out_file)
    next(reader)  # Skip the header
    for row in reader:
        email = row[0]
        if is_valid_email(email):
            writer.writerow(row)
        else:
            print(f"Invalid email: {email}")