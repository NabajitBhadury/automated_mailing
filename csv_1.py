import csv

# Step 1: Open the file containing the emails and read its contents
with open('participants.txt', 'r') as f:
    contents = f.read()

# Step 2: Split the contents by newline characters to get a list of emails
emails = contents.split('\n')

# Step 3: Open a new CSV file in write mode
with open('participants.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Step 4: Write the header to the CSV file
    writer.writerow(['Email'])

    # Step 5: Write each email to the CSV file as a new row
    for email in emails:
        writer.writerow([email])