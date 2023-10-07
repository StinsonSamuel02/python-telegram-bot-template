"""Import all commands."""
from pathlib import Path

from .start import *
from .unknown import *
from .ginnebra import *
from .menu import *


# 19 TODO: Add typing
def get_all_commands():
    """Returns a list with all the commands names"""
    commands_path = Path("./commands")

    all_commands = []
    for cmd in commands_path.iterdir():
        command = cmd.stem
        if command.isalpha() and command != "unknown":
            all_commands.append(command)
    return all_commands
