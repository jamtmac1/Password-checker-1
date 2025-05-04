
import re
# Placeholder to refresh on regex since I saw that regex would be a better usecase here for more complex loops

# Starts Loop
while True:
	# Ask user to input password
	password = input("Enter your password: ")

	# Strength options 
	if len(password) <8:
		print("Password is too weak")
	elif len(password) <=12:
		print("Password is moderate. Please make it stronger")
	else: 
		has_number = any(char.isdigit() for char in password)
		has_special = any(not char.isalnum() for char in password)

		if has_number and has_special: 
			print("Password is strong") 
			break #Learning that break is not the ideal way to exit a loop but okay sense this is 
			a tiny loop
		else:
			print("Password must contain a numeric value and special character")

# Account creation

while True:
	new_password = input("Create password: ")
	confirm_password = input("Confirm new password: ")
	if new_password !=  confirm_password
		print ("Passwords do not match")
		continue


			


