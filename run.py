import random

# https://pypi.org/project/py-enigma/
from enigma.machine import EnigmaMachine

# https://docs.python.org/3/library/time.html
import time

# https://github.com/Textualize/rich
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# https://docs.python.org/3/library/os.html
import os

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
    "plugboard_setting": [
    {"challenge": "What 5-letter word becomes shorter when you add two letters to it?",
     "hint": "It's not about length but semantics.",
     "text_solution": "short",
     "solution": "AD FG"},
    {"challenge": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
     "hint": "Often heard but not seen.",
     "text_solution": "echo",
     "solution": "EH CO"},
    {"challenge": "Forward I am heavy, but backward I am not. What am I?",
     "hint": "Think about direction and weight.",
     "text_solution": "ton",
     "solution": "TN ON"}
    ]
}

def menu():
    """
    Main menu
    """
    clear_screen()

    # https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
    while True:
        console.print("Main Menu:", style="bold blue underline")
        options = ["1. Start Game", "2. Instructions", "3. About", "4. Exit"]
        for option in options:
            console.print(option, style="bold yellow")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            user()
        elif choice == "2":
            instructions()
        elif choice == "3":
            about()
        elif choice == "4":
            console.print("\nExiting the game. Goodbye!\n", style="bold red")
            break
        else:
            console.print("\nInvalid choice. Please enter a number between 1 and 4.\n", style="bold red")

def user():
    """
    Save the user name
    """
    clear_screen()
    console.print("Welcome to the Adventure!", style="bold magenta")

    # Age Verification
    while True:
        user_age = input("\nPlease enter your age to start the game: ")
        if user_age.isdigit() and int(user_age) >= 18:
            break
        elif user_age.isdigit() and int(user_age) < 18:
            console.print("You are too young to risk your life, wait until you are older.\n", style="bold red")
            return
        else:
            console.print("Invalid input. Please enter a valid number for age.", style="bold red")

    # Name Input
    while True:
        user_name = input("\nEnter your name to embark on a thrilling adventure filled with mystery and intrigue: ").strip()
        if user_name:
            break
        console.print("Name cannot be empty. Please enter a valid name.", style="bold red")

    rotor_positions = rotor_position_challenge()
    if not rotor_positions:
        console.print("Failed to obtain rotor positions. Cannot proceed.")
        return

    ring_hint = ring_setting_challenge()
    if not ring_hint:
        console.print("Failed to obtain ring settings. Cannot proceed with email encryption.")
        return

    plugboard_hint = plugboard_challenge()
    email_content, encrypted_email = email(user_name, ring_hint, rotor_positions)
    console.print(email_content, style="bold green")
    
    # Decrypt with hints
    decrypt_email(user_name, rotor_positions, ring_hint, plugboard_hint, encrypted_email) 

def instructions():
    """
    User instructions of the game
    """
    clear_screen()
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
    Information about the game.
    """
    clear_screen()
    console.print("[bold magenta]About the Game[/bold magenta]\n", justify="center")
    console.print("In a world where secret communications can alter the course of history, one machine stood out for its complexity and effectiveness: the Enigma. Used during a tumultuous time in human history, it encrypted messages that, if fallen into the wrong hands, could have changed the outcome of significant events.", style="italic")
    console.print("\nIn this game, you step into the shoes of a cryptanalyst during a critical period. Tasked with decrypting crucial messages, your success or failure could very well determine the fate of nations. Armed with your wit, intuition, and an understanding of the Enigma machine, you'll face various challenges that will test your decoding skills to the utmost.")
    console.print("\nAs you navigate through the puzzles and riddles, remember that each solved challenge brings you one step closer to unveiling secrets meant for only a select few. The challenges you face are inspired by historical scenarios, although with a twist of fiction to enhance the gaming experience.")
    console.print("\n[bold green]Are you ready to embark on this thrilling adventure, unravel the mysteries, and perhaps alter the course of history? Welcome to 'The Enigma Challenge.'[/bold green]", justify="center")
    console.print("\nPress enter to return to the main menu.")
    input()
    menu()

def get_random_challenge(challenge_type):
    """
    Randomly chosse a challenge question
    """
    challenge_pool = challenges[challenge_type]
    selected_challenge = random.choice(challenge_pool)
    return selected_challenge

def rotor_position_challenge():
    """
    User Challenge to find initial rotor position with a timer.
    """
    clear_screen()
    challenge = get_random_challenge("rotor_position")
    console.print(f"\nRotor Position Challenge: {challenge['challenge']}\nHint: {challenge['hint']}", style="bold yellow")

    attempts, max_attempts = 0, 3

    # Start the timer
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().upper()
        if " " in answer:
            console.print("Spaces are not allowed. Please enter your answer without spaces.", style="bold red")
            continue

        if answer == challenge["solution"]:
            
            # Stop timer and calculate duration
            end_time = time.time()
            console.print(f"Correct! Time taken: {end_time - start_time:.2f} seconds", style="bold green")
            return challenge["solution"]

        attempts += 1
        remaining_attempts = max_attempts - attempts
        console.print(f"Incorrect. {remaining_attempts} {'attempt' if remaining_attempts == 1 else 'attempts'} remaining.", style="bold red")

    # Stop timer and calculate duration if max attempts reached
    end_time = time.time()
    console.print(f"Time taken: {end_time - start_time:.2f} seconds", style="bold red")
    console.print(f"The correct answer was '{challenge['solution']}'. No hints for rotor positions.", style="bold red")
    return None


def ring_setting_challenge():
    """
    User Challenge to find ring setting
    """
    clear_screen()
    challenge = get_random_challenge("ring_setting")
    console.print(f"\nRing Setting Challenge: {challenge['challenge']}\nHint: {challenge['hint']}", style="bold yellow")

    attempts, max_attempts = 0, 3

    # Start the timer
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().lower()

        if " " in answer:
            console.print("Spaces are not allowed. Please enter your answer without spaces.", style="bold red")
            continue

        if answer == challenge["text_solution"]:

            # Stop timer and calculate duration
            end_time = time.time()
            console.print(f"Correct! Time taken: {end_time - start_time:.2f} seconds", style="bold green")
            return challenge["solution"]

        attempts += 1
        remaining_attempts = max_attempts - attempts
        console.print(f"Incorrect. {remaining_attempts} {'attempt' if remaining_attempts == 1 else 'attempts'} remaining.", style="bold red")

    # Stop timer and calculate duration if max attempts reached
    end_time = time.time()
    console.print(f"Time taken: {end_time - start_time:.2f} seconds", style="bold red")
    console.print(f"The correct answer was '{challenge['text_solution']}'. No hints for ring settings.", style="bold red")
    return None

def plugboard_challenge():
    """
    User Challenge for the plugboard settings.
    """
    clear_screen()
    challenge = get_random_challenge("plugboard_setting")
    console.print(f"\nPlugboard Challenge: {challenge['challenge']}\nHint: {challenge['hint']}", style="bold yellow")

    attempts, max_attempts = 0, 3
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().lower()

        if " " in answer:
            console.print("Spaces are not allowed. Please enter your answer without spaces.", style="bold red")
            continue

        if answer == challenge["text_solution"]:
            end_time = time.time()
            console.print(f"Correct! Time taken: {end_time - start_time:.2f} seconds", style="bold green")
            return challenge["solution"]

        attempts += 1
        console.print(f"Incorrect. {max_attempts - attempts} attempts remaining.", style="bold red")

    end_time = time.time()
    console.print(f"Time taken: {end_time - start_time:.2f} seconds", style="bold red")
    console.print(f"Unfortunately, you didn't get the correct answer. The correct answer was '{challenge['text_solution']}'.", style="bold red")
    return None

def setup_enigma_machine(ring_settings):
    """
    Setting up Enigma machine with predefined settings.
    """
    clear_screen()

    # https://pypi.org/project/py-enigma/
    # Set up Enigma Machine with some initial settings
    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings=ring_settings,
        plugboard_settings='AD FG'
    )
    return machine

def encrypt_string(machine, plaintext, initial_positions):
    """
    Encrypts a string using the Enigma machine.
    """
    machine.set_display(initial_positions)
    ciphertext = machine.process_text(plaintext)
    return ciphertext, initial_positions

def generate_email(user_name, ring_settings, rotor_positions):
    """
    Generates a random email with encrypted parts.
    """
    # https://www.w3schools.com/python/ref_random_choice.asp
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    sender = "secretagent@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net"])
    receiver = f"{user_name}@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "gmx.com", "outlook.com", "codeinstitute.net"])
    subject = "Top Secret Mission"
    body_plaintext = f"Hello{user_name}congratulationsyoucompletedyourmission"

    # Set up the Enigma machine for the email
    enigma = setup_enigma_machine(ring_settings)
    enigma.set_display(rotor_positions)
    encrypted_message = enigma.process_text(body_plaintext.replace(" ", "").upper()) 
    email_content = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{encrypted_message}"
    return email_content, encrypted_message

def email(user_name, ring_settings, rotor_positions):
    """
    Encrypted email.
    """
    email_content, encrypted_email = generate_email(user_name, ring_settings, rotor_positions)
    print("You've received an encrypted email:\n")
    return email_content, encrypted_email

def decrypt_email(user_name, rotor_hint, ring_hint, plugboard_hint, encrypted_message):
    """
    Decrypt email.
    """
    print(f"\nRotor Positions (Hint): {rotor_hint if rotor_hint else 'No specific hint, refer to the challenge solution.'}")
    print(f"Ring Settings (Hint): {ring_hint if ring_hint else 'No specific hint, refer to the challenge solution.'}")
    print(f"Plugboard Settings (Hint): {plugboard_hint if plugboard_hint else 'No specific hint, refer to the challenge solution.'}")

    while True:
        rotor_positions = input(f"Enter the rotor positions (Hint was {rotor_hint}): ").upper()
        if " " in rotor_positions or not rotor_positions:
            console.print("Invalid input. Please enter the rotor positions without spaces and cannot be empty.", style="bold red")
            continue
        break

    while True:
        ring_settings_input = input(f"Enter the ring settings as three numbers separated by spaces (Hint: {ring_hint if ring_hint else 'No hint'}): ")
        if "  " in ring_settings_input or not ring_settings_input.strip():
            console.print("Invalid input. Please enter three numbers separated by a single space and cannot be empty.", style="bold red")
            continue
        ring_settings = ring_settings_input.split()
        if len(ring_settings) != 3 or not all(num.isdigit() for num in ring_settings):
            console.print("Invalid input. Please enter exactly three numbers separated by spaces.", style="bold red")
            continue
        ring_settings = [int(num) for num in ring_settings]
        break

    while True:
        plugboard_settings = input(f"Enter the plugboard settings as pairs of letters separated by spaces (Hint: {plugboard_hint if plugboard_hint else 'No hint'}): ")
        if "  " in plugboard_settings or not plugboard_settings.strip():
            console.print("Invalid input. Please enter pairs of letters separated by a single space and cannot be empty.", style="bold red")
            continue
        plugboard_pairs = plugboard_settings.upper().split()
        if any(len(pair) != 2 for pair in plugboard_pairs) or not all(pair.isalpha() for pair in plugboard_pairs):
            console.print("Invalid input. Please enter valid letter pairs (e.g., 'AB CD').", style="bold red")
            continue
        break

    enigma = setup_enigma_machine(ring_settings)
    enigma.set_display(rotor_positions)
    decrypted_message = enigma.process_text(encrypted_message)
    console.print(f"\nDecrypted message: {decrypted_message}\n", style="bold underline cyan")
    table = Table(title="Challenge Summary")
    table.add_column("Challenge", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_row("Rotor Position", "Completed")
    table.add_row("Ring Setting", "Completed")
    table.add_row("Plugboard Setting", "Completed")
    console.print(table)
    console.print(Panel("Congratulations, you've completed your mission!", title="Mission Complete", style="bold green"))

def clear_screen():
    """
    Clears the console screen.
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/Mac
    else:
        os.system('clear')

def run_game():
    """
    Run program functions.
    """
    clear_screen()
    menu()
    
print("\nWelcome the russian enigme game\n") 
run_game()