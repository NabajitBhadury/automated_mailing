import csv

# Open the CSV file and read the email addresses
with open('participants.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    emails = [row[0] for row in reader]

# Step 1: Create an empty set to store the unique emails
unique_emails = set(emails)

# Step 3: After checking all emails, write the unique emails back to the CSV file
with open('participants.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])  # Write the header
    for email in unique_emails:
        writer.writerow([email])