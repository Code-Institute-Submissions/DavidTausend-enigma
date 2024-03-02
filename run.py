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
    try:
        user_age = int(input("\nPlease enter your age to start the game: "))
    except ValueError:
        print("Please enter a valid number for age.")

        # Return to main menu
        return

    if user_age < 18:
        print("\nYou are to young to risk your life, wait until you are older")

        # Return to main menu
        return
        
    user_name = input("\nPlease enter your name to start the game: ")
    # print(f"\nWelcome, {user_name}! You are about to embark on a mission of utmost secrecy and importance.\n")
    print(f"\nHello {user_name}, your mission, should you choose to accept it, involves to pass 3 challenges and decrypt an email message. Good luck.\n")

    # Decryption challenges
    rotor_hint = rotor_position_challenge()
    ring_hint = ring_setting_challenge()
    plugboard_hint = plugboard_challenge()

    # Show encrypted email and get initial positions used
    initial_positions = email(user_name)

    # Decrypt with hints
    decrypt_email(user_name, rotor_hint, ring_hint, plugboard_hint, initial_positions)

def instructions():
    """
    User instructions of the game
    """
    print("\nInstructions:")
    print("1. Start the game by entering your name. You must be at least 18 years old to play.")
    print("2. You will face three challenges designed to test your decryption skills and provide hints for the final task:")
    print("   a. Rotor Position Challenge: Decrypt a code to find the initial rotor positions of the Enigma machine.")
    print("   b. Ring Setting Challenge: Solve a puzzle to discover the ring settings.")
    print("   c. Plugboard Challenge: Answer a riddle to get a hint for the plugboard settings.")
    print("3. After successfully completing the challenges, you will receive an encrypted email. The email contains a secret mission that you must decrypt using the Enigma machine.")
    print("4. Use the hints from the challenges to configure the Enigma machine for decryption:")
    print("   a. Enter the rotor positions as hinted by the Rotor Position Challenge (e.g., 'kab').")
    print("   b. Input the ring settings as three numbers separated by spaces, based on the Ring Setting Challenge (e.g., '0 0 7').")
    print("   c. Provide the plugboard settings as pairs of letters separated by spaces, as indicated by the Plugboard Challenge (e.g., 'dt fp').")
    print("5. Decrypt the message to uncover the secret mission. Correct decryption will reveal a coherent message congratulating you on completing your mission.")
    print("6. Completing the mission successfully will prevent WWIII and win the war.")
    print("\nGood luck, agent! The fate of the world rests in your hands.\n")
   

def rules():
    """
    Game rules
    """

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

def setup_enigma_machine():
    """
    Setting up Enigma machine with predefined settings.
    """

    # https://pypi.org/project/py-enigma/
    # Set up Enigma Machine with some initial settings
    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings=[5, 18, 21],
        plugboard_settings='AD FG'
    )
    return machine

def encrypt_string(machine, plaintext):
    """
    Encrypts a string using the Enigma machine.
    """
    initial_positions = "FBI"
    machine.set_display(initial_positions)
    ciphertext = machine.process_text(plaintext)
    return ciphertext, initial_positions


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
    body_plaintext = f"Hello{user_name}congratulationsyoucompletedyourmission"
    body_encrypted, initial_positions = encrypt_string(enigma, body_plaintext)
    email_content = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n \n{body_plaintext}\n\n{body_encrypted}"
    return email_content, initial_positions

def email(user_name):
    """
    Encrypted email
    """
    email_content, initial_positions = generate_email(user_name)
    print("You've received an encrypted email:\n")
    print(email_content)
    return initial_positions


def decrypt_email(user_name, rotor_hint, ring_hint, plugboard_hint, initial_positions):
    print(f"Rotor Positions (Hint): {initial_positions}")
    print(f"Ring Settings (Hint): {ring_hint}")
    print(f"Plugboard Settings (Hint): {plugboard_hint}")

    print("\nNow, attempt to decrypt the encrypted message using the hints you've gathered.")
    encrypted_message = input("\nEnter the encrypted part of the email you received: ")
    rotor_positions = input(f"Enter the rotor positions (Initial positions were {initial_positions}): ").upper()
    ring_settings_input = input(f"Enter the ring settings as three numbers separated by spaces (Hint: {ring_hint if ring_hint else 'No hint'}): ")
    plugboard_settings = input(f"Enter the plugboard settings as pairs of letters separated by spaces (Hint: {plugboard_hint if plugboard_hint else 'No hint'}): ")

    ring_settings = [int(n) for n in ring_settings_input.split()] if ring_settings_input else [1, 1, 1]
    enigma = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings=ring_settings,
        plugboard_settings=plugboard_settings
    )
    enigma.set_display(rotor_positions)

    # Decrypt the message
    decrypted_message = enigma.process_text(encrypted_message)
    print(f"\nDecrypted message: {decrypted_message}")

def run_game():

    """
    Run program functions
    """
    menu()
    
print("\nWelcome the russian enigme game\n") 
run_game()