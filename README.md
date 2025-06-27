# Password Strength Checker & Account Setup

A simple but realistic Python program that allows a user to:

- Create a password
- Confirm it matches
- Validate its strength based on common security requirements
- Set a password hint
- Attempt to log in, with a hint revealed after failed attempts

This is designed to simulate basic authentication logic in a command-line interface.

# Features
- Password must:
  - Be at least 12 characters long
  - Contain at least one number
  - Contain at least one special character
- Requires password confirmation before accepting
- Accepts and stores a user-defined password hint
- Login phase:
  - Up to 5 attempt MAX
  - Hint is shown after failed attempts
  - Lockout after 5 failed attempts

# Why?

I built this to work on my Python development. I needed a quick project to practice. This will help me show coding proficiency as I try to rotate into Cloud Engineering/DevOps. What I am trying to improve:

- Logic structuring
- Syntax
- User input validation
- Control flow with loops and conditionals
- CLI application design

# How to Run
- python password-checker.py
- Python 3.x installed
  
# Future Enhancements
- Hash password for added security
- Save credentials to a local file
- Integrate with AWS

Jamal Henderson
Cloud Engineer

```bash
python password_checker.py
