
# Ask user to input a password
 
password = input("Enter your password: ")
# Check for numbers
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

# Strength options 
if len(password) <8:
	print("Password is too weak")
elif len(password) <=12:
	print("Password is moderate. Please make it stronger")
else: 
	if has_number and has_special:
		print("Password is strong")
	else:
		print("Password must contain a numeric value and special character")


