# Email Validator

## Description
The Email Validator is a Python program that reads a list of email addresses from a text file, validates each email, and categorizes them into valid and invalid lists. Valid emails are saved to `valid_emails.txt`, while invalid emails are saved to `invalid_emails.txt`.

## Features
- Reads email addresses from a file (`emails.txt`).
- Validates emails using a regular expression.
- Saves valid emails to `valid_emails.txt`.
- Saves invalid emails to `invalid_emails.txt`.

## How to Use
1. Create a text file named `emails.txt` in the same directory as the script.
2. Populate `emails.txt` with email addresses (one per line).
3. Run the program.
4. Check the `valid_emails.txt` and `invalid_emails.txt` files for results.

## Requirements
- Python 3.x

## How It Works
1. The program reads email addresses from `emails.txt`.
2. Each email is checked for validity using a regular expression pattern.
3. Valid emails are written to `valid_emails.txt`, and invalid emails are written to `invalid_emails.txt`.
