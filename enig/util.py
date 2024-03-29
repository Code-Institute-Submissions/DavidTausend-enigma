import os
import random
from rich.console import Console

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
