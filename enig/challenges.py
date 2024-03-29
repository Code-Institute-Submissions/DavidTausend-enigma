import time
import random
from rich.table import Table
from rich.panel import Panel
from enig.util import get_random_challenge, clear_screen, console
from enig.enigma_setup import setup_enigma_machine


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


def generate_email(user_name, ring_settings, rotor_positions):
    """
    Generates a random email with encrypted parts.
    """
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
            f"by spaces\n(Hint: {formatted_hint}): "
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
            f"spaces\n(Hint: "
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
