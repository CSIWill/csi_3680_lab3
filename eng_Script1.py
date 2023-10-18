# William Eng
# weng2@oakland.edu
# Password Strength Checker

# A valid password is at least 8 characters without any
# space. A valid password can be identified as three categories (STRONG, GOOD, WEAK):
# • A STRONG password is a combination of letter, number, and special characters.
# • A GOOD password is a combination of letter and number, or a combination of letter and special characters,
# or a combination of number and special characters.
# • A WEAK password has only of letters, or numbers, or special characters.

import re

def is_valid(password):
    # check for any spaces
    try:
       password_regex = re.compile(r'\s')
       mo = password_regex.search(password)
       mo.group()
       print("Password cannot contain spaces")
       return False
    except AttributeError:
        try:
            # check for at least 8 characters
            password_regex = re.compile(r'\w\w\w\w\w\w\w\w*')
            mo = password_regex.search(password)
            mo.group()
            # print("Password is valid with at least 8 characters long with no spaces")
            return True
        except AttributeError:
            print("Password must be at least 8 characters long")
            return False
    
def has_letter(password):
    # check for any letters
    try:
        password_regex = re.compile(r'[a-zA-Z]')
        mo = password_regex.search(password)
        mo.group()
        return True
    except AttributeError:
        return False
def has_digit(password):
    # check for any numbers
    try:
        password_regex = re.compile(r'\d')
        mo = password_regex.search(password)
        mo.group()
        return True
    except AttributeError:
        return False
def has_special(password):
    # check for any special characters
    try:
        password_regex = re.compile(r'\W|\_')
        mo = password_regex.search(password)
        mo.group()
        # print("Password has special characters")
        return True
    except AttributeError:
        return False
def is_strong(password):
    if has_letter(password) and has_digit(password) and has_special(password):
        return True
    else:
        return False
def is_good(password):
    if (has_letter(password) and has_digit(password)) or (has_letter(password) and has_special(password)) or (has_digit(password) and has_special(password)):
        return True
    else:
        return False
def is_weak(password):
    if has_letter(password) or has_digit(password) or has_special(password):
        return True
    else:
        return False
def check_pwd(password):
    if is_valid(password):
        if is_strong(password):
            print("Password is STRONG")
        elif is_good(password):
            print("Password is GOOD")
        elif is_weak(password):
            print("Password is WEAK")
       

print("Password Strength Checker")
password = input("Enter a password: ")
check_pwd(password)