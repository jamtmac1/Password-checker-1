
# Ask user to input a password
 
password = input("Enter your password: ")

# Strength options 
if len(password) <8:
	print("Password is too weak")
elif len(password) <=12:
	print("Password is moderate. Please make it stronger")
else: 
	print("Password is strong")
