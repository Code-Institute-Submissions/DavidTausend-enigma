import random
# https://pypi.org/project/py-enigma/
from enigma.machine import EnigmaMachine


def menu():
    """
    Main menu
    """
    # https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
    while True:
        print("\nMain Menu:\n")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Rules")
        print("4. Exit\n")
        
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            user()
        elif choice == "2":
            instructions()
        elif choice == "3":
            rules()
        elif choice == "4":
            exit()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

def user():
    """
    Save the user name
    """
    user_name = input("Please enter your name to start the game: ")
    print(f"\nWelcome, {user_name}! You are about to embark on a mission of utmost secrecy and importance.\n")

def setup_enigma_machine():
    """
    Setting up Enigma machine with predefined settings.
    """
    # https://pypi.org/project/py-enigma/
    # Set up Enigma Machine with some initial settings
    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings=[1, 20, 11],
        plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
    )
    return machine

def encrypt_string():
    """

    """


def generate_email():
    """
    Generates a random email with encrypted parts.
    """
    # https://www.w3schools.com/python/ref_random_choice.asp
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    sender = "secretagent@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net" ])
    receiver = "{user_name}@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net" ])
    suject = "Operation " + "Confidential"


def email():
    """
    Encrypted email.
    """
    email = generate_email()
    print("You've received an encrypted email:\n")
    print(email)
    print("\nSome parts of this email are encrypted. Can you decrypt them to uncover the secret message and stop the WWIII?")

def instructions():
    """
    User instructions of the game.
    """
    print("\nInstructions:")
    print("You will receive an encrypted email containing a secret message.")
    print("Your task is to decrypt the message using a decryption key.")
    print("Correctly decrypting the message will prevent WWIII and win the war.\n")

def exit():
    """
    Exiting the game.
    """
    print("\nExiting the game. Goodbye!\n")

def main():
    """
    Run program functions.
    """
    menu()
    

print("\nWelcome the russian enigme game\n") 
main()