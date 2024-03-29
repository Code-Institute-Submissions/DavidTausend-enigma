from enigma.ui import print_enigma_logo, console
from enigma.challenges import (
    rotor_position_challenge, 
    ring_setting_challenge, 
    plugboard_challenge, 
    email, 
    decrypt_email
)
from enigma.enigma_setup import setup_enigma_machine

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
                " only, without numbers or special characters, and ensure it "
                "is no more than 15 characters long.", style="bold red"
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


def run_game():
    """
    Run program functions.
    """
    clear_screen()
    print_enigma_logo()
    menu()