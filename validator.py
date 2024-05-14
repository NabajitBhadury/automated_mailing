import csv
# from validator import validate_email, EmailNotValidError
from email_validator import validate_email, EmailNotValidError

# Step 2: Open the CSV file and read the email addresses
with open('participants.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) 
    emails = [row[0] for row in reader]

for email in emails:
    try:
        v = validate_email(email)
    except EmailNotValidError as e:
        print(f'{email} is not valid')