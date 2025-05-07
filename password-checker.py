
import re
# Placeholder to refresh on regex since I saw that regex would be a better usecase here for more complex loops

# Starts Loop
while True:
	# Ask user to input password
	password = input("Create a password: ")
	confirm_password = input("Confirm your password: ")

	# Passwords Match?
	if password!= confirm_password:
		print("Passwords do not match")

	# Strength options 
	if len(password) <8:
		print("Password is too weak")
	elif len(password) <=11:
		print("Password is moderate. Please make it stronger")
	else: 
		has_number = any(char.isdigit() for char in password)
		has_special = any(not char.isalnum() for char in password)

		if has_number and has_special: 
			print("Password is strong and accepted") 
			break #Learning that break is not the ideal way to exit a loop but okay since this is a tiny loop
		else:
			print("Password must contain a numeric value and special character")
			continue
# Password Hint
while True:
	password_hint = input("Create a password hint: ")
	print("Your password hint has been saved.")
	break

# Login 
max_attempts = 5
show_hint = False
login_attempts = 0

print("Login")

while login_attempts < max_attempts:
	entered_password = input("Enter your password: ")
	login_attempts += 1
	
	if entered_password == password:
		print("Password Accepted")
		break
	else:
		print("Incorrect Password: Try Again.")
		
		if login_attempts == 3 and not show_hint:
			print(f"Hint: {password_hint}")
			show_hint = True
# Attempts calc
		attempts_left = max_attempts - login_attempts
		if attempts_left > 0:
			print(f"You have {attempts_left} attempts left.")
if login_attempts == max_attempts:
	print("Too many failed attempts. You have been locked out of the account. Please contact an administrator")
