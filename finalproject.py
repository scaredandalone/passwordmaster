import sys
import haveibeenpwned
import string
import random

def main():
    print("\nPASSWORD MASTER: check, generate or examine your password\n\n" "Type 'check' to check for your password in known database breaches\n" "Type 'generate' to generate a strong 10 character password\n"
          "Type 'examine' to examine your passwords strengths and weaknesses")
    uinput = input("What would you like to do?\n")
    if uinput.lower() == "check":
        check()
    elif uinput.lower() == "generate":
        print("Generated password:", generate())
    elif uinput.lower() == "examine":
        password = input("Whats your password?\n")
        strengths, weaknesses = examine(password)
        print("Results of your password's examination:")
        print("Strengths:\n" + strengths)
        print("Weaknesses:\n" + weaknesses)
    else:
        sys.exit("⁉ Invalid input\n Try 'check', 'generate' or 'examine'.")

def check():
    password = input("Enter the password to check: ")
    
    count = haveibeenpwned.pwnd_api_check(password)
    if count:
        print(f'❗The password "{password}" was found {count} times in data breaches. You should consider changing it.')
    else:
        print(f'✔ The password "{password}" was not found in data breaches. It seems secure')

def generate():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password by selecting characters randomly from all character sets 10 characters long
    password = ''.join(random.choice(all_characters) for _ in range(10))
    
    return password

def examine(password):
    strengths = ""
    weaknesses = ""
    
    if any(char.islower() for char in password):
        strengths += "✔ Password contains lowercase characters\n"
    else:
        weaknesses += "❗ Password does not contain lowercase characters\n"
    
    if any(char.isupper() for char in password):
        strengths += "✔ Password contains uppercase characters\n"
    else:
        weaknesses += "❗ Password does not contain uppercase characters\n"
    
    if any(char.isdigit() for char in password):
        strengths += "✔ Password contains numbers\n"
    else:
        weaknesses += "❗ Password does not contain numbers\n"
    
    if any(char in string.punctuation for char in password):
        strengths += "✔ Password contains special characters\n"
    else:
        weaknesses += "❗ Password does not contain special characters\n"
    
    if len(password) >= 8:
        strengths += "✔ Password length is at least 8 characters\n"
    else:
        weaknesses += "❗ Password length less than 8 characters\n"
    
    return strengths, weaknesses
if __name__ == "__main__":
    main()