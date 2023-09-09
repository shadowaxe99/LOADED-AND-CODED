
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)
