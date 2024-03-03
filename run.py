import random

# https://pypi.org/project/py-enigma/
from enigma.machine import EnigmaMachine

# https://docs.python.org/3/library/time.html
import time

# https://www.toppr.com/ask/
challenges = {
    "rotor_position": [
        {"challenge": "Decrypt 'LXF' to find the initial rotor positions.",
         "hint": "It's a famous three-letter agency.",
         "solution": "FBI"},
        {"challenge": "Decrypt 'UGM' to find the initial rotor positions.",
         "hint": "A precious yellow metal.",
         "solution": "GLD"}
    ],
    "ring_setting": [
         {"challenge": "I am always hungry, I must always be fed. The finger I touch will soon turn red. What am I?",
         "hint": "I can be found in every home and am essential for cooking, but be careful not to get too close.",
         "text_solution": "fire",
         "solution": [5, 18, 21]},
        {"challenge": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
         "hint": "Think about communication devices.",
         "text_solution": "echo",
         "solution": [0, 5, 19]},
        {"challenge": "The more of this there is, the less you see. What is it?",
         "hint": "It's essential for life but can be dangerous in excess.",
         "text_solution": "darkness",
         "solution": [22, 1, 6]}
      ],
}

def menu():
    """
    Main menu
    """

    # https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
    while True:
        print("\nMain Menu:\n")
        print("1. Start Game - Begin your adventure and tackle the challenges.")
        print("2. Instructions - Learn how to play and what to expect.")
        print("3. About - Discover the story behind the game.")
        print("4. Exit - Leave the game. Your progress will be saved.")

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
    while True:
        try:
            user_age = int(input("\nPlease enter your age to start the game: "))
            if user_age < 18:
                print("\nYou are too young to risk your life, wait until you are older.\n")
                continue 
            break  
        except ValueError:
            print("Please enter a valid number for age.")

    while True:
        user_name = input("\nEnter your name to embark on a thrilling adventure filled with mystery and intrigue:").strip()
        if user_name: 
            break
        print("Name cannot be empty. Please enter a valid name.")
        return
        
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
   

def about():
    """
    Information about the game
    """

def get_random_challenge(challenge_type):
    """
    Randomly chosse a challenge question
    """
    challenge_pool = challenges[challenge_type]
    selected_challenge = random.choice(challenge_pool)
    return selected_challenge

def rotor_position_challenge():
    """
    User Challenge to find initial rotor position with a timer
    """
    challenge = get_random_challenge("rotor_position")
    print("\nRotor Position Challenge:")
    print(challenge["challenge"])
    print(f"Hint: {challenge['hint']}")

    # Start the timer
    start_time = time.time()

    answer = input("\nYour answer: ").upper()

    attempts, max_attempts = 0, 3
    while answer != challenge["solution"] and attempts < max_attempts:
        attempts += 1
        print("Incorrect. Try again.")
        answer = input("Your answer: ").upper()

    # Stop timer
    end_time = time.time()  

    # Calculate duration
    duration = end_time - start_time  
    print(f"Time taken: {duration:.2f} seconds") 

    if answer == challenge["solution"]:
        print("Correct! The initial rotor positions are derived from your answer.")
    else:
        print(f"Incorrect. The correct answer was '{challenge['solution']}'. No hints for rotor positions.")

def ring_setting_challenge():
    """
    User Challenge to find ring setting
    """
    challenge = get_random_challenge("ring_setting")
    print("\nRing Setting Challenge:")
    print(challenge["challenge"])
    print(f"Hint: {challenge['hint']}")

    # Start the timer
    start_time = time.time()

    attempts, max_attempts = 0, 3
    while attempts < max_attempts:
        answer = input("\nYour answer: ").lower()
        if answer == challenge["text_solution"]:
            print("Correct! The ring settings are derived from your answer.")
            break
        else:
            attempts += 1
            print(f"Incorrect. {max_attempts - attempts} attempts remaining.")
            if attempts < max_attempts:
                print("Try again. Hint: ", challenge["hint"])

    # Stop timer
    end_time = time.time()

    # Calculate duration
    duration = end_time - start_time
    print(f"Time taken: {duration:.2f} seconds")

    if attempts == max_attempts:
        print(f"Incorrect. The correct answer was '{challenge['text_solution']}'. No hints for ring settings.")
        return None
    else:
        return challenge["solution"]

def plugboard_challenge():
    """
    User Challenge to plugboard enigma 
    """
    print("\nPlugboard Challenge:")
    print("What 5-letter word becomes shorter when you add two letters to it?")

    # Start the timer
    start_time = time.time()

    answer = input("\nYour answer: ").lower()

    # Stop timer
    end_time = time.time()  

    # Calculate duration
    duration = end_time - start_time  
    print(f"Time taken: {duration:.2f} seconds") 

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
    """
    Decrypt email
    """
    print(f"\nRotor Positions (Hint): {rotor_hint if rotor_hint else 'No specific hint, refer to the challenge solution.'}")
    print(f"Ring Settings (Hint): {ring_hint if ring_hint else 'No specific hint, refer to the challenge solution.'}")
    print(f"Plugboard Settings (Hint): {plugboard_hint if plugboard_hint else 'No specific hint, refer to the challenge solution.'}")

    encrypted_message = input("\nEnter the encrypted part of the email you received: ")
    rotor_positions = input(f"Enter the rotor positions (Hint was {rotor_hint}): ").upper() if rotor_hint else initial_positions
    ring_settings_input = input(f"Enter the ring settings as three numbers separated by spaces (Hint: {ring_hint if ring_hint else 'No hint'}): ")
    plugboard_settings = input(f"Enter the plugboard settings as pairs of letters separated by spaces (Hint: {plugboard_hint if plugboard_hint else 'No hint'}): ")

    # Convert the ring settings input to list of integers
    ring_settings = [int(x) for x in ring_settings_input.split()]

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