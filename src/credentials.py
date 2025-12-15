
def encrypt(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + 2)
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - 2)
    return decrypted_text

def full_mask(text):
    return "*" * len(text)

def partial_mask(text):
    if len(text) <= 2:
        return "*" * len(text)
    else:
        decry=decrypt(text)
        return decry[0] + "*" * (len(decry) - 2) + decry[-1]

def view(view_option,name,psw):
    print("How do you want to view credentials?")
    print("1. Fully Masked")
    print("2. Partially Masked")
    print("3. Fully Decrypted")

    choice = input("Enter your choice (1/2/3): ")

    print("\n--- STORED CREDENTIALS ---")

    if choice == "1":
        print("Username:", full_mask(name))
        print("Password:", full_mask(psw))

    elif choice == "2":
        print("Username:", partial_mask(name))
        print("Password:", partial_mask(psw))
 

    elif choice == "3":
        print("Username:", decrypt(name))
        print("Password:", decrypt(psw))

    else:
        print("Invalid choice! ,choose your choice (1/2/3) ")



  #********************************************    main.py    ****************************************************************


from src.credentials import *

def main():
    username = encrypt(input("Enter Username: "))
    password = encrypt(input("Enter Password: "))

    print("\nCredentials saved securely!\n")

    view_option=input("Type 'y' for viewing your credentials ")

    if view_option=='y':
        name=username
        psw=password
        view(view_option,name,psw)
    else:
        print("Type valid key : 'y' ")

if __name__=="__main__":
    main()

     




