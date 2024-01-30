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
            print("\nExiting the game. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

def user():
    """
    Save the user name
    """
    user_age = int(input("\nPlease enter your age to start the game: "))

    if user_age < 18:
        print("\nYou are to young to risk your life, wait until you are older")
        menu()
    else:
        pass
        
    user_name = input("\nPlease enter your name to start the game: ")
    print(f"\nWelcome, {user_name}! You are about to embark on a mission of utmost secrecy and importance.\n")

    # Pass the user_name to the email
    email(user_name)

    # Decryption challenges
    rotor_hint = rotor_position_challenge()
    ring_hint = ring_setting_challenge()
    plugboard_hint = plugboard_challenge()

def instructions():
    """
    User instructions of the game.
    """
    print("\nInstructions:")
    print("You will receive an encrypted email containing a secret message.")
    print("Your task is to decrypt the message using a decryption key.")
    print("Correctly decrypting the message will prevent WWIII and win the war.\n")

def rules():
    """
    Game rules.
    """

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

def encrypt_string(machine, plaintext):
    """
    Encrypts a string using the Enigma machine.
    """
    # Set the initial rotor position
    machine.set_display('WXC')  
    ciphertext = machine.process_text(plaintext)
    return ciphertext


def generate_email(user_name):
    """
    Generates a random email with encrypted parts.
    """
    # https://www.w3schools.com/python/ref_random_choice.asp
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    sender = "secretagent@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net" ])
    receiver = f"{user_name}@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net" ])
    subject = "Top Secret Mission"

    # Set up the Enigma machine for the email
    enigma = setup_enigma_machine()

    # Encrypt the body of the email
    body_plaintext = f"Hello {user_name}, your mission, should you choose to accept it, involves decrypting this message. Good luck."
    body_encrypted = encrypt_string(enigma, body_plaintext)

    return f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n \n{body_plaintext}\n\n{body_encrypted}"

def email(user_name):
    """
    Encrypted email.
    """
    email = generate_email(user_name)
    print("You've received an encrypted email:\n")
    print(email)
    #print("\nSome parts of this email are encrypted. Can you decrypt them to uncover the secret message and stop the WWIII?")


def rotor_position_challenge():
    """
    User Challenge to find initial rotor position
    """
    print("\nRotor Position Challenge:")
    print("Decrypt the following code to find the initial rotor positions: 'LXF'")

    # https://www.toppr.com/ask/
    print("Hint: It's a famous three-letter agency.")
    answer = input("\nYour answer: ").upper()

    attempts = 1
    while answer != "FBI":

        # Give the user 3 attempts
        if attempts >= 3:  
            print("Incorrect. The correct answer was 'FBI'. No hints for rotor positions.")
            return None
        print("Incorrect. Try again.")
        answer = input("Your answer: ").lower()
        attempts += 1
        
    print("Correct! The initial rotor positions are 'F', 'B', 'I'.")
    return "FBI"

def ring_setting_challenge():
    """
    User Challenge to find ring setting
    """
    print("\nRing Setting Challenge:")
    print("Solve this puzzle: I am always hungry, I must always be fed. The finger I touch will soon turn red. What am I?")
    answer = input("\nYour answer: ").lower()

    attempts = 1
    while answer != "fire" or answer == "flame":
        if attempts >= 3:
            print("Incorrect. The correct answer was 'fire'. No hints for ring settings.")
            return None
        print("Incorrect. Try again.")
        answer = input("Your answer: ").lower()
        attempts += 1
    
    print("Correct! The ring settings are '05', '18', '21'.")
    return [5, 18, 21]

def plugboard_challenge():
    """
    User Challenge to plugboard enigma 
    """
    print("\nPlugboard Challenge:")
    print("What 5-letter word becomes shorter when you add two letters to it?")
    answer = input("\nYour answer: ").lower()

    attempts = 1
    while answer != "shorter":
        if attempts >= 3:
            print("Incorrect. The correct answer was 'short'. No hints for plugboard settings.")
            return None
        print("Incorrect. Try again.")
        answer = input("Your answer: ").lower()
        attempts += 1
    
    print("Correct! The plugboard setting hint is 'AD FG'.")
    return "AD FG"
    
def run_game():

    """
    Run program functions.
    """
    menu()
    

print("\nWelcome the russian enigme game\n") 
run_game()