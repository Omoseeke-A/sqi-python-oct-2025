# Scenario:
# You are working as a data analyst for a marketing company. You have been given a large text document containing customer reviews and feedback. Your task is to extract all email addresses and phone numbers from this document for further analysis.

# Task:
# Write a Python script named `data_analyst.py` that:
# Reads the contents of a text file named reviews.txt.
# Extracts all email addresses and phone numbers from the text.
# Email addresses follow the standard format: username@domain.tld
# Phone numbers are in the format: +234 803 456 7890
# Writes the extracted email addresses to a file named emails.txt and the phone numbers to a file named phone_numbers.txt.

# Requirements:
# Use regular expressions to find the email addresses and phone numbers.
# Ensure that the extracted data is saved in separate files, one for emails and one for phone numbers.

import re

with open("reviews.txt", 'r') as file:
    content = file.read()
    convert_to_string =str(content)
    print(convert_to_string)

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+234\s\d{3}\s\d{3}\s\d{4}'
    email_match = re.findall(email_pattern, convert_to_string)
    phone_match = re.findall(phone_pattern,convert_to_string)

    for email in email_match:
        print("Email Address Found:\n", email)
        print()
    print("There are", len(email_match), "email addresses found in the document.")

    for phone in phone_match:
        print("Phone Number Found:\n", phone)
        print()
    print("There are", len(phone_match), "phone numbers found in the document.")


with open("emails.txt", 'w') as email_file:
    for email in email_match:
        email_file.write(email + '\n')
with open("phone_numbers.txt", 'w') as phone_file:
    for phone in phone_match:
        phone_file.write(phone + '\n')
        