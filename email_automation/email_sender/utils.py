import csv

def parse_recipients(file):
    recipients = []
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipients.append({
                'email': row['Email'],
                'name': row['Name'],
                'company': row['Company']
            })
    return recipients