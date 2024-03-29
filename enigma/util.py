import os
import random
from rich.panel import Panel
from rich.console import Console

console = Console()

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
    for challenge, time_taken in times.items():
        table.add_row(
            challenge,
            f"{time_taken:.2f}")
    console.print(table)


def get_random_challenge(challenge_type):
    """
    Randomly chosse a challenge question.
    """
    challenge_pool = challenges[challenge_type]
    selected_challenge = random.choice(challenge_pool)
    return selected_challenge