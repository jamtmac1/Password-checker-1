
import re
# Want to refresh on regex

# Ask user to input a password

# Starts Loop
while True:
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
			break #Learning that break is not the ideal way to exit a loop but okay sense this is a tiny loop
		else:
			print("Password must contain a numeric value and special character")

#Password attempts limit
attempts = 0
max_attempts = 5

while attemps < max_attempts:
	password =		


