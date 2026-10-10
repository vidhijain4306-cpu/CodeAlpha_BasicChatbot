# CodeAlpha Internship - Task 3: Basic Chatbot
# Created by: Vidhi

import datetime
import random
import re

# Predefined canned responses and conversational patterns
RESPONSES = {
    r"\b(hi|hello|hey|greetings|hola)\b": [
        "Hello! How can I help you today?",
        "Hey there! What's on your mind?",
        "Hi! Good to talk to you. How are you doing?"
    ],
    r"\b(how are you|how's it going|how are you doing)\b": [
        "I'm doing great, thank you for asking! How are you?",
        "All systems running smoothly! How has your day been?"
    ],
    r"\b(your name|who are you)\b": [
        "I am AlphaBot, a Python rule-based conversational assistant built for CodeAlpha internship!",
        "My name is AlphaBot. Nice to meet you!"
    ],
    r"\b(time|what time is it)\b": [
        lambda: f"The current time is {datetime.datetime.now().strftime('%I:%M:%S %p')}."
    ],
    r"\b(date|what day is it|today's date)\b": [
        lambda: f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."
    ],
    r"\b(tell me a joke|joke|make me laugh)\b": [
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because he used up all his cache!",
        "There are 10 types of people in the world: those who understand binary, and those who don't."
    ],
    r"\b(python|codealpha|internship)\b": [
        "Python is one of the most versatile languages in the world!",
        "CodeAlpha internships give students hands-on project experience in real-world software development."
    ],
    r"\b(help|commands|options)\b": [
        "You can chat with me naturally! Ask me about:\n  - Time or Date\n  - Tell me a joke\n  - My name / who I am\n  - How I am doing\n  - Python or CodeAlpha\n  - Type 'bye' or 'exit' to quit."
    ]
}

FALLBACK_RESPONSES = [
    "I'm not sure I understand that. Type 'help' to see what you can ask me!",
    "Interesting! Could you rephrase that?",
    "I haven't learned how to answer that yet, but I'm constantly improving!"
]


def get_bot_response(user_input):
    """
    Matches the user's input against regex patterns and returns an appropriate reply.
    """
    clean_input = user_input.strip().lower()

    for pattern, replies in RESPONSES.items():
        if re.search(pattern, clean_input):
            selected = random.choice(replies)
            # If reply is a function (e.g. for dynamic time/date), call it
            return selected() if callable(selected) else selected

    return random.choice(FALLBACK_RESPONSES)


def chat():
    """
    Main interactive chat loop.
    """
    print("=" * 50)
    print("           WELCOME TO ALPHABOT CHAT            ")
    print("=" * 50)
    print("Hi! I am AlphaBot. Type 'help' for topics or 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAlphaBot: Goodbye! Have a wonderful day!")
            break

        if not user_input:
            continue

        # Check for exit commands
        if user_input.lower() in ("bye", "exit", "quit", "goodbye"):
            print("AlphaBot: Bye! Have a great day ahead! Take care!")
            break

        response = get_bot_response(user_input)
        print(f"AlphaBot: {response}\n")


if __name__ == "__main__":
    chat()
