# REQUIREMENTS
# >= 8 characters
# Atleast one uppercase & one lowercase
# Atleast one special: ! @ # $ % ^ * - _ = + [ { ] } / ; : , . ?

import re
import random
import string
import time
import os
from colorama import Fore
from colorama import Style

specialChar = "£$&()*+[]@#^-_!?";

def validate(password):
    checks = []
    if len(password) < 8:
        checks.append("pswdLength")
    if not any(char.isdigit() for char in password):
        checks.append("noNums")
    if not any(char.isupper() for char in password):
        checks.append("noUppers")
    if not any(char.islower() for char in password):
        checks.append("noLowers")
    if not any(char in specialChar for char in password):
        checks.append('noSpecials')
    return checks



def validateDialogue():
    os.system("cls")
    print(f"{Fore.LIGHTYELLOW_EX}Please input the password to check: {Style.RESET_ALL}")
    pswd = input()
    check = validate(pswd)
    if not check:
        print(f"{Fore.GREEN}Your password is secure! Great job.{Style.RESET_ALL}")
    else:
        print("Your password is not safe enough. These are the typical guidelines:")
        if "pswdLength" in check:
            print(f"1. {Fore.RED}Atleast 8 characters long{Style.RESET_ALL}")
        else:
            print(f"1. {Fore.GREEN}Atleast 8 characters long{Style.RESET_ALL}")
        if "noUppers" in check or "noLowers" in check:
            print(f"2. {Fore.RED}Atleast 1 uppercase and 1 lowercase character{Style.RESET_ALL}")
        else:
            print(f"2. {Fore.GREEN}Atleast 1 uppercase and 1 lowercase character{Style.RESET_ALL}")
        if "noNums" in check:
            print(f"3. {Fore.RED}Atleast one number{Style.RESET_ALL}")
        else:
            print(f"3. {Fore.GREEN}Atleast one number{Style.RESET_ALL}")
        if "noSpecials" in check:
            print(f"4. {Fore.RED}Atleast one special character. Allowed chars: @$!%*?&{Style.RESET_ALL}")
        else:
            print(f"4. {Fore.GREEN}Atleast one special character. Allowed chars: @$!%*?&{Style.RESET_ALL}")
        e = input(f"{Fore.LIGHTYELLOW_EX}Press enter to try another password.{Style.RESET_ALL}")
        validateDialogue()

def generatePassword(length):
    password = ""
    for char in range(length):
        choice = round(abs(random.random() * (4-1)))
        if choice == 0:
            password += random.choice(string.ascii_uppercase)
        elif choice == 1:
            password += random.choice(string.ascii_lowercase)
        elif choice == 2:
            password += random.choice(string.digits)
        elif choice == 3:
            password += random.choice(specialChar)
    return password

while True:
    os.system("cls")
    print(f"{Fore.LIGHTYELLOW_EX}Type \"{Fore.WHITE}create{Fore.LIGHTYELLOW_EX}\" to generate a secure password, or \"{Fore.WHITE}validate{Fore.LIGHTYELLOW_EX}\" to check your password: {Style.RESET_ALL}")
    intro = input()

    if intro == "create":
        os.system("cls")
        print(f"{Fore.LIGHTYELLOW_EX}How long do you want your password? (minimum 8 characters):{Style.RESET_ALL}")
        length = input()
        print(f"{Fore.LIGHTYELLOW_EX}Generating password...{Style.RESET_ALL}")
        time.sleep(3)
        pswd = generatePassword(int(length))
        print(f"{Fore.GREEN}Done! Your new password is:{Style.RESET_ALL}")
        time.sleep(1)
        print(f"{Fore.LIGHTCYAN_EX}" + pswd + f"{Style.RESET_ALL}")
        time.sleep(1)
        break

    elif intro == "validate":
        validateDialogue()
        break
    else:
        print(f"{Fore.RED}Please enter \"create\" or \"validate\" to use this tool.{Style.RESET_ALL}")
        time.sleep(3)
        os.system("cls")