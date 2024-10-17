# open the main file to make list containg all the email without new line
with open("emails.txt", "r") as f :
  emails = f.readlines()
  # this list will contain all the emails without new line
  new_emails_list = [email.strip() for email in emails]


# print all the emails (valid and invalid) -just for check-
for e_mail in new_emails_list :
  print(e_mail)


# make a fun to check if the email is valid or not
def check_email (email) :
  # import regex module 
  import re
  # this regex will check if the email is valid or not
  email_pattern = r"[^@]+@[^@]+\.[^@]+"
  match_email = re.match(email_pattern, email)
  # if the email is valid then return true else return false
  return bool(match_email)


# here we will loop in the new_emails_list and check if the email is valid or not -using check_email function-
for email in new_emails_list :
  if check_email(email) :
    # if the email is valid then we will open the valid_emails.txt file and write the email in it
    with open("valid_emails.txt", "a") as valid_emails :
      valid_emails.write(email + "\n")
  else:
    # if the email is not valid then we will open the invalid_emails.txt file and write the email in it
    with open("invalid_emails.txt", "a") as invalid_emails :
      invalid_emails.write(email + "\n")
