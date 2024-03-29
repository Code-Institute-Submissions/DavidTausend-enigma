from enig.logo import print_enigma_logo
from enig.util import clear_screen
from enig.menu import menu


def run_game():
    """
    Run program functions.
    """
    clear_screen()
    print_enigma_logo()
    menu()
