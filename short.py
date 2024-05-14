import csv

# Read the first CSV file into a set of tuples (name, email)
with open('SCCSBS_emails.csv', 'r') as f:
    reader = csv.DictReader(f)
    data1 = {(row['Name'].strip(), row['Email'].strip()) for row in reader}

# Read the second CSV file and extract emails into a set
with open('IEEE.csv', 'r') as f:  
    reader = csv.reader(f)
    data2 = {row[0].strip() for row in reader}  

# Find common emails between the two datasets
common_emails = {email for name, email in data1} & data2

# Filter data1 to keep only the entries with common emails
common_data = {(name, email) for name, email in data1 if email in common_emails}

# Write the common data (Name, Email) into a new CSV file
with open('common_emails.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email'])
    writer.writerows(common_data)
