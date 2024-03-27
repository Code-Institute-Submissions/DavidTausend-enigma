import random
import time
import os

# https://pypi.org/project/py-enigma/
from enigma.machine import EnigmaMachine

# https://github.com/Textualize/rich
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# https://www.toppr.com/ask/
challenges = {
    "rotor_position": [
        {
            "challenge": "Decrypt 'LXF' to find the initial rotor positions.",
            "hint": "It's a famous three-letter agency.",
            "solution": "FBI"
         },
        {
            "challenge": "Decrypt 'UGM' to find the initial rotor positions.",
            "hint": "A precious yellow metal (3 Letters).",
            "solution": "GLD"
         }
    ],
    "ring_setting": [
        {
            "challenge": (
                "I am always hungry, I must always be fed. "
                "The finger I touch will soon turn red. What am I?"
            ),
            "hint":  (
                "I can be found in every home and am essential for cooking, "
                "but be careful not to get too close."
            ),
            "text_solution": "fire",
            "solution": [5, 18, 21]
        },
        {
            "challenge": (
                "I speak without a mouth and hear without ears. "
                "I have no body, but I come alive with wind. What am I?"
            ),
            "hint": "Think about communication devices.",
            "text_solution": "echo",
            "solution": [0, 5, 19]
        },
        {
            "challenge": (
             "The more of this there is, the less you see. What is it?"
             ),
            "hint": "It's essential for life but can be dangerous in excess.",
            "text_solution": "darkness",
            "solution": [22, 1, 6]
        }
      ],
    "plugboard_setting": [
        {
            "challenge": (
                    "What 5-letter word becomes "
                    "shorter when you add two letters to it?"
                ),
            "hint": "It's not about length but semantics.",
            "text_solution": "short",
            "solution": "AD FG"
        },
        {
            "challenge":  (
                    "I speak without a mouth and hear without ears. "
                    "I have no body, but I come alive with wind. What am I?"
                ),
            "hint": "Often heard but not seen.",
            "text_solution": "echo",
            "solution": "EH CO"
        },
        {
            "challenge": (
                "Forward I am heavy, but backward I am not. What am I?"
                ),
            "hint": "Think about direction and weight.",
            "text_solution": "ton",
            "solution": "TN ON"
        }
    ]
}


def print_enigma_logo():
    logo = """
    ███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗ 
    ██╔════╝████╗  ██║██║██╔═════╗████╗ ████║██╔══██╗
    █████╗  ██╔██╗ ██║██║██║ ████║██╔████╔██║███████║
    ██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║
    ███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
    ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
    """
    print(logo)


def menu():
    """
    Main menu
    """
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
            console.print(
                "2. You will face a series of challenges designed to test your"
                " decryption skills and provide hints for the final task:"
                          )


def instructions():
    """
    User instructions for the game.
    """
    clear_screen()
    console.print("[bold]Instructions:[/bold]", justify="center")
    console.print(
        "1. Start the game by entering your name. "
        "You must be at least 18 years old to play."
    )
    console.print(
        "2. You will face a series of challenges"
        " designed to test your decryption "
        "skills and provide hints for the final task:"
    )
    console.print(
        "   a. Rotor Position Challenge: "
        "Decrypt a code to find the initial rotor"
        " positions of the Enigma machine."
    )
    console.print(
        "   b. Ring Setting Challenge: "
        "Solve a puzzle to discover the ring settings."
    )
    console.print(
        "   c. Plugboard Challenge: "
        "Answer a riddle to get a hint for the plugboard"
        " settings."
    )
    console.print(
        "3. After successfully completing the challenges,"
        " you will receive an encrypted email. "
        "The email contains a secret mission that you must decrypt using the"
        " Enigma machine."
    )
    console.print(
        "4. Use the hints from the challenges to configure"
        " the Enigma machine for decryption:"
    )
    console.print(
        "   a. Enter the rotor positions as hinted by "
        "the Rotor Position Challenge (e.g., 'kab')."
    )
    console.print(
        "   b. Input the ring settings as three numbers"
        " separated by spaces, based on the Ring"
        " Setting Challenge (e.g., '0 0 7')."
    )
    console.print(
        "   c. Provide the plugboard settings as pairs "
        "of letters separated by spaces, as indicated "
        "by the Plugboard Challenge (e.g., 'dt fp')."
    )
    console.print(
        "5. Decrypt the message to uncover the secret mission."
        " Correct decryption will reveal a coherent message "
        "congratulating you on completing your mission."
    )
    console.print(
        "6. Completing the mission successfully "
        "will prevent WWIII and win the war."
    )
    console.print(
        "\nGood luck, agent! The fate of the world rests in your hands.\n"
    )


def about():
    """
    Information about the game.
    """
    clear_screen()
    console.print(
        "[bold magenta]About the Game[/bold magenta]\n", justify="center"
    )
    console.print(
        "In a world where secret communications can alter the course of "
        "history, one machine stood out for its complexity and effectiveness:"
        " the Enigma. Used during a tumultuous time in human history, "
        "it encrypted messages that, if fallen into the wrong hands, could "
        "have changed the outcome of significant events.", style="italic"
        )
    console.print(
        "\nIn this game, you step into the shoes of a cryptanalyst during a "
        "critical period. Tasked with decrypting crucial messages, "
        "your success or failure could very well determine the fate of "
        "nations. Armed with your wit, intuition, and an understanding of "
        "the Enigma machine, you'll face various challenges that will test "
        "your decoding skills to the utmost."
    )
    console.print(
        "\nAs you navigate through the puzzles and riddles, remember that "
        "each solved challenge brings you one step closer to unveiling "
        "secrets meant for only a select few. The challenges you face are "
        "inspired by historical scenarios, although with a twist of fiction "
        "to enhance the gaming experience."
    )
    console.print(
        "\n[bold green]Are you ready to embark on this thrilling adventure, "
        "unravel the mysteries, and perhaps alter the course of history? "
        "Welcome to 'The Enigma Challenge.'[/bold green]", justify="center"
    )
    console.print("\nPress enter to return to the main menu.")
    input()
    menu()


def user():
    """
    Save the user name and manage the game flow.
    """
    clear_screen()
    console.print(
        "Welcome to the Adventure!", style="bold magenta", justify="center"
    )

    # Age Verification
    while True:
        user_age = input("\nPlease enter your age to start the game: ")
        if user_age.isdigit():
            user_age = int(user_age)
            if 18 <= user_age <= 100:
                break
            elif user_age < 18:
                console.print(
                    "You are too young to risk your life, "
                    "wait until you are older.\n", style="bold red"
                    )
                return
            else:
                console.print(
                    "Invalid input. Please enter a valid number "
                    "for age.", style="bold red"
                    )
        else:
            console.print(
                "Invalid input. Please enter a valid "
                "number for age.", style="bold red"
            )

    # Name Input
    while True:
        user_name = input(
            "\nEnter your name to embark on a thrilling adventure "
            "filled with mystery\nand intrigue (Max 15 characters): "
        ).strip()

        if 0 < len(user_name) <= 15 and user_name.replace(" ", "").isalpha():
            break
        else:
            console.print(
                "Invalid name. Please enter a name using alphabetic characters"
                " only, without numbers or special characters, and ensure it is"
                " no more than 15 characters long.", style="bold red"
            )

    introduction_to_enigma()
    story_challenge()
    enigma_key_challenge()

    # Initialize total time for all challenges
    total_time = 0

    # Rotor Position Challenge
    rotor_time, rotor_positions = rotor_position_challenge()
    total_time += rotor_time 
    if rotor_positions is None:
        console.print(
            "Failed to obtain rotor positions. "
            "Cannot proceed with email encryption."
        )
        return

    # Ring Setting Challenge
    ring_time, ring_hint = ring_setting_challenge()
    total_time += ring_time
    if ring_hint:
        total_time += ring_time
    else:
        console.print(
            "Failed to obtain ring settings. "
            "Cannot proceed with email encryption."
        )
        return

    # Plugboard Challenge
    plugboard_time, plugboard_hint = plugboard_challenge()
    total_time += plugboard_time 
    if plugboard_hint:
        total_time += plugboard_time
    else:
        console.print(
            "Failed to obtain plugboard settings. "
            "Cannot proceed with decryption."
        )
        return

    rotor_positions_str = (
        ''.join(rotor_positions) if isinstance(rotor_positions, list)
        else rotor_positions
    )

    # Display the encrypted email content
    email_content, encrypted_email = (
        email(user_name, ring_hint, rotor_positions_str)
    )
    console.print(email_content, style="bold green")

    # Decrypt with hints
    decrypt_email(
        user_name, rotor_positions_str, ring_hint,
        plugboard_hint, encrypted_email
    )

    # Display total time taken for all challenges at the end
    console.print(
        Panel(f"Total time taken for all challenges:"
              f"[bold]{total_time:.2f} seconds[/bold]",
              title="Challenge Time Summary", style="bold blue")
    )

    input("\nPress enter to go to main menu")
    clear_screen()


def introduction_to_enigma():
    """
    Introduction to the Enigma machine and the game's challenges.
    """
    clear_screen()
    console.print(
        "[bold magenta]Welcome to The Enigma Adventure!"
        "[/bold magenta]\n", justify="center"
    )

    intro_text = (
        "The Enigma machine, a marvel of early 20th-century technology,"
        " was a sophisticated device used for encrypting and "
        "decrypting secret messages. Originally developed for commercial use,"
        " it was famously adopted by the military forces "
        "of several nations, most notably by Nazi Germany before and during "
        "World War II. The complexity of its encryption "
        "mechanism, which involved a series of rotors and a plugboard, "
        "made it incredibly difficult for intercepted messages "
        "to be deciphered, thus changing the course of espionage"
        " and secret communications.\n\n"

        "In this adventure, you'll step into the shoes of a cryptanalyst "
        "faced with the monumental task of cracking the "
        "Enigma's codes. Through a series of challenges, you'll learn "
        "about the components and operations of the Enigma machine, "
        "piece together its settings, and ultimately decrypt a secret "
        "message that could alter the outcome of a great conflict. "
        "Each challenge is designed to test your problem-solving skills and "
        "give you a glimpse into the world of historical cryptography.\n\n"

        "Prepare yourself for a journey into the shadows of secret messages,"
        " where intuition, logic, and a keen eye for detail "
        "will be your best tools. The fate of nations could rest on your "
        "ability to understand and operate the enigmatic Enigma machine.\n"
    )

    console.print(intro_text, style="bold cyan")

    input("Press enter to embark on your first challenge...")


def display_time(times):
    """
    Display global challenge timer at the end of the game.
    """
    console.print(
        "\n[bold underline]Challenge Time Summary:[/bold underline]"
    )
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Challenge", style="dim")
    table.add_column("Time Taken (seconds)", justify="right")
    for challenge, time_taken in times.items():table.add_row(challenge, f"{time_taken:.2f}")
    console.print(table)


def get_random_challenge(challenge_type):
    """
    Randomly chosse a challenge question.
    """
    challenge_pool = challenges[challenge_type]
    selected_challenge = random.choice(challenge_pool)
    return selected_challenge


def story_challenge():
    """
    User needs to guess a coponent of the engima machine.
    """
    clear_screen()
    console.print(
        "The Lost Engineer:", style="bold magenta", justify="center"
    )
    console.print(
        "You've come across a diary belonging to an engineer who vanished in "
        "the last days of the war. The diary mentions a crucial part of the "
        "Enigma he was working on. This component is key to your mission."
        )

    diary_entry = (
        "...Despite the chaos, I continue my work on the machines. "
        "[???] is particularly fascinating, with its ability to transform "
        "each letter through a complex series of electrical paths. It's this "
        "component that might hold the key to our communications"
        " staying secure..."
    )

    console.print(f"\nDiary Entry:\n{diary_entry}", style="italic")
    console.print(
        "\nHint: This Enigma component was pivotal for scrambling letters."
        " It's mentioned in the diary entry.", style="bold yellow"
    )

    attempts, max_attempts = 0, 3

    while attempts < max_attempts:
        answer = input("\nIdentify the component: ").strip().upper()

        if answer == "ROTOR":
            console.print(
                "Correct! The rotors were indeed the heart of the Enigma's"
                " scrambling mechanism.", style="bold green"
            )
            break
        else:
            attempts += 1
            console.print(
                f"Incorrect. Try again. {max_attempts - attempts}"
                " attempts left.", style="bold red"
            )

    if attempts == max_attempts:
        console.print(
            "Unfortunately, you couldn't identify the component. "
            "It was the 'ROTOR'. This key piece will lead you to "
            "your next challenges.", style="bold red"
        )
    else:
        console.print(
            "With the knowledge of the rotor's importance, you proceed to "
            "uncover more about the Enigma machine.", style="bold green"
        )

    input("\nPress enter to continue...")


def enigma_key_challenge():
    """
    User needs to guess the daily key setting of the Enigma machine.
    """
    clear_screen()
    console.print(
        "[bold magenta]The Enigma Key Challenge"
        "[/bold magenta]\n", justify="center"
    )
    console.print(
        "Hint: To decrypt today's messages, the Enigma operators "
        "aligned the rotors to a specific starting position, which is widely "
        "recognized as a standard initial setting. "
        "What could it be?", style="bold cyan"
    )
    key_guess = input(
        "\nGuess the daily key setting (e.g., AAA, ABC): "
    ).strip().upper()

    if key_guess in ["AAA", "ABC"]:
        console.print(
            "\nCorrect! The daily key setting was indeed a simple starting "
            "position like 'AAA' or 'ABC'. This setting was the foundation "
            "for all subsequent operations each day.", style="bold green"
        )
    else:
        console.print(
            "\nIncorrect. The daily key setting was something simple and "
            "widely recognized, like 'AAA' or 'ABC'. This initial step was "
            "crucial for setting up the machine.", style="bold red"
        )

    input("\nPress enter to continue to the main challenges...")


def rotor_position_challenge():
    """
    User Challenge to find initial rotor position with a timer.
    """
    clear_screen()
    challenge = get_random_challenge("rotor_position")
    console.print(
        f"\nRotor Position Challenge: {challenge['challenge']}",
        style="bold yellow"
    )
    console.print(f"Hint: {challenge['hint']}", style="bold yellow")

    attempts, max_attempts = 0, 3

    # Start the timer
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().upper()
        if " " in answer:
            console.print(
                "Spaces are not allowed. "
                "Please enter your answer without spaces.", style="bold red"
            )
            continue
        if answer == challenge["solution"]:

            # Stop timer and calculate duration
            end_time = time.time()
            console.print(
                f"Correct! Time taken: "
                f"{end_time - start_time:.2f} seconds",
                style="bold green"
            )

            return end_time - start_time, challenge["solution"]

        attempts += 1
        console.print(
            f"Incorrect. "
            f"{max_attempts - attempts} attempts remaining.",
            style="bold red"
        )

    # Stop timer and calculate duration if max attempts reached
    end_time = time.time()
    console.print(
        f"Unfortunately, you didn't get the correct answer. "
        f"The correct answer was '{challenge['solution']}'.",
        style="bold red"
    )

    return end_time - start_time, None


def ring_setting_challenge():
    """
    User Challenge to find ring setting.
    """
    clear_screen()
    challenge = get_random_challenge("ring_setting")
    console.print(
        f"\nRing Setting Challenge: {challenge['challenge']}",
        style="bold yellow"
    )
    console.print(
        f"Hint: {challenge['hint']}",
        style="bold yellow"
    )

    attempts, max_attempts = 0, 3

    # Start the timer
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().lower()
        if " " in answer:
            console.print(
                "Spaces are not allowed. "
                "Please enter your answer without spaces.", style="bold red"
            )
            continue

        if answer == challenge["text_solution"]:

            # Stop timer and calculate duration
            end_time = time.time()
            console.print(
                f"Correct! Time taken: "
                f"{end_time - start_time:.2f} seconds",
                style="bold green"
            )
            return end_time - start_time, challenge["solution"]

        attempts += 1
        console.print(
            f"Incorrect. {max_attempts - attempts} "
            "attempts remaining.",
            style="bold red"
        )

    # Stop timer and calculate duration if max attempts reached
    end_time = time.time()
    console.print(
        f"Time taken: {end_time - start_time:.2f} seconds", style="bold red"
    )
    console.print(
        f"The correct answer was "
        f"'{challenge['text_solution']}'.",
        style="bold red"
    )

    return end_time - start_time, None


def plugboard_challenge():
    """
    User Challenge for the plugboard settings.
    """
    clear_screen()
    challenge = get_random_challenge("plugboard_setting")
    console.print(
        f"\nPlugboard Challenge: {challenge['challenge']}"
        f"\nHint: {challenge['hint']}",
        style="bold yellow"
    )

    attempts, max_attempts = 0, 3
    start_time = time.time()

    while attempts < max_attempts:
        answer = input("\nYour answer: ").strip().lower()
        if " " in answer:
            console.print(
                "Spaces are not allowed. Please enter your answer"
                " without spaces.", style="bold red"
            )
            continue

        if answer == challenge["text_solution"]:
            end_time = time.time()
            console.print(
                f"Correct! Time taken: "
                f"{end_time - start_time:.2f} seconds", style="bold green"
            )
            return end_time - start_time, challenge["solution"]

        attempts += 1
        console.print(
            f"Incorrect. {max_attempts - attempts} "
            f"attempts remaining.", style="bold red"
        )

    end_time = time.time()
    console.print(
        f"Time taken: {end_time - start_time:.2f} seconds", style="bold red"
    )
    console.print(
        f"The correct answer was "
        f"'{challenge['text_solution']}'.", style="bold red"
    )

    return end_time - start_time, None


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
    domains = [
        "gmail.com", "yahoo.com", "hotmail.com",
        "gmx.com", "outlook.com", "codeinstitute.net"
    ]
    sender_domain = random.choice(domains)
    receiver_domain = random.choice(domains)

    sender = f"secretagent@{sender_domain}"
    receiver = f"{user_name}@{receiver_domain}"
    subject = "Top Secret Mission"
    body_plaintext = (
        f"Hello {user_name} congratulations you completed your mission"
    )

    # Set up the Enigma machine for the email
    enigma = setup_enigma_machine(ring_settings)
    enigma.set_display(rotor_positions)
    encrypted_message = (
        enigma.process_text(body_plaintext.replace(" ", "").upper())
    )
    email_content = (
        f"From: {sender}\n"
        f"To: {receiver}\n"
        f"Subject: {subject}\n\n"
        f"{encrypted_message}"
    )
    return email_content, encrypted_message


def email(user_name, ring_settings, rotor_positions):
    """
    Encrypted email.
    """
    email_content, encrypted_email = generate_email(
        user_name, ring_settings, rotor_positions
    )
    print("You've received an encrypted email:\n")
    return email_content, encrypted_email


def decrypt_email(
    user_name, rotor_hint, ring_hint, plugboard_hint, encrypted_message
):
    """
    Decrypt email.
    """
    no_hint_msg = 'No specific hint, refer to the challenge solution.'

    rotor_hint_text = rotor_hint if rotor_hint else no_hint_msg
    ring_hint_text = ring_hint if ring_hint else no_hint_msg
    plugboard_hint_text = plugboard_hint if plugboard_hint else no_hint_msg

    print(f"\nRotor Positions (Hint): {rotor_hint_text}")
    print(f"Ring Settings (Hint): {ring_hint_text}")
    print(f"Plugboard Settings (Hint): {plugboard_hint_text}")

    while True:
        rotor_positions = input(
            f"Enter the rotor positions (Hint was {rotor_hint}): "
        ).upper()
        if " " in rotor_positions or not rotor_positions:
            console.print(
                "Invalid input. Please enter the rotor positions "
                "without spaces and cannot be empty.", style="bold red"
            )
            continue
        if rotor_hint and rotor_positions != rotor_hint:
            console.print(
                f"Incorrect rotor positions. "
                f"Hint: {rotor_hint}", style="bold red"
            )
            continue
        break

    while True:
        formatted_hint = (
            ' '.join(map(str, ring_hint)) if ring_hint else 'No hint'
        )
        ring_settings_input = input(
            f"Enter the ring settings as three numbers separated "
            f"by spaces (Hint: {formatted_hint}): "
        )
        if "  " in ring_settings_input or not ring_settings_input.strip():
            console.print(
                "Invalid input. Please enter three numbers separated by a "
                "single space and cannot be empty.", style="bold red"
            )
            continue

        ring_settings = ring_settings_input.split()
        if (len(ring_settings) != 3 or
                not all(num.isdigit() for num in ring_settings)):

            console.print(
                "Invalid input. Please enter exactly three "
                "numbers separated by spaces.", style="bold red"
            )
            continue

        ring_settings = [int(num) for num in ring_settings]
        input_comparison = ' '.join(str(num) for num in ring_settings)
        if ring_hint and input_comparison != formatted_hint:
            console.print(
                f"Incorrect ring settings. "
                f"Hint: {formatted_hint}", style="bold red"
            )
            continue
        break

    while True:
        plugboard_settings = input(
            f"Enter the plugboard settings as pairs of letters separated by "
            f"spaces (Hint: "
            f"{plugboard_hint if plugboard_hint else 'No hint'}): "
            )
        if "  " in plugboard_settings or not plugboard_settings.strip():
            console.print(
                "Invalid input. Please enter pairs of letters separated by a"
                " single space and cannot be empty.", style="bold red"
            )
            continue

        plugboard_pairs = plugboard_settings.upper().split()

        if (any(len(pair) != 2 for pair in plugboard_pairs) or
                not all(pair.isalpha() for pair in plugboard_pairs)):
            console.print(
                "Invalid input. Please enter valid letter "
                "pairs (e.g., 'AB CD').", style="bold red"
            )
            continue
        if (plugboard_hint and
                plugboard_settings.upper() != plugboard_hint.upper()):
            console.print(
                f"Incorrect plugboard settings. "
                f"Hint: {plugboard_hint}", style="bold red"
            )
            continue
        break

    enigma = setup_enigma_machine(ring_settings)
    enigma.set_display(rotor_positions)
    decrypted_message = enigma.process_text(encrypted_message)
    console.print(
        f"\nDecrypted message: "
        f"{decrypted_message}\n", style="bold underline cyan"
    )
    table = Table(title="Challenge Summary")
    table.add_column("Challenge", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_row("Rotor Position", "Completed")
    table.add_row("Ring Setting", "Completed")
    table.add_row("Plugboard Setting", "Completed")
    console.print(table)
    console.print(
        Panel(
            "Congratulations, you've completed your mission!",
            title="Mission Complete",
            style="bold green")
    )


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
    print_enigma_logo()
    menu()


print("\nWelcome to the Enigma game\n")
run_game()
