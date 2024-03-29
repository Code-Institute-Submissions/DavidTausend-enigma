from enig.logo import console
from enig.user import user
from enig.util import clear_screen


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
    console.print("\nPress enter to return to the main menu.")
    input()
    clear_screen()
    menu()


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
    clear_screen()
    menu()


def menu():
    """
    Main menu
    """
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
                "Invalid choice. Please select a valid option from the menu.",
                style="bold red"
            )
