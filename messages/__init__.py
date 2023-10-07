"""Import all messages."""
from pathlib import Path


# 19 TODO: Add typing
def get_all_messages():
    """Returns a list with all the messages filtered"""
    messages_path = Path("./messages")

    all_messages = []
    for msg in messages_path.iterdir():
        message = msg.stem
        if message.isalpha() and message != "unknown":
            all_messages.append(message)
    return all_messages
