# Email Validation: Check if the email is valid and if it already exists in the list, if not add it to the list
emails = ["user1@algonex.com", "invalid",1,343434, "user2@domain.com","Nelamalli@algonex.com", "no_at_sign"]
Created_email = input("Enter new email")
for i in emails:
          if '@' in str(i):
                    print(i)
                    if Created_email in emails:
                              print("Email already exists")
                    else:
                              emails.append(Created_email)
          else:
                    print("Invalid email")