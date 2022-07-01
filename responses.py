from datetime import datetime

def sample_responses(input_message):
    user_message = str(input_message).lower()

    if user_message in ("hello"):
        return "Hello, friend."

    if user_message in ("how are you?", "how are you"):
        return "Doing well, wby?"

    return "I don't understand."
