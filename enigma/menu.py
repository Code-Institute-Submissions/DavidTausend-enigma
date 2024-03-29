from enigma.game_logic import run_game
from enigma.game_logic import user
from enigma.ui import instructions, about, console

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
                "2. You will face a series of challenges designed to test your"
                " decryption skills and provide hints for the final task:"
                          )