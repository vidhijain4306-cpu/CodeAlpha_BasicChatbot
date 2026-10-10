# CodeAlpha - Task 3: Basic Chatbot

A simple rule-based conversational chatbot written in Python. Developed as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
AlphaBot is a lightweight command-line chatbot that processes user messages using pattern matching and regular expressions (`re`). It provides predefined and dynamic contextual responses to conversational prompts.

### 🎯 Key Features
- **Intent Recognition**: Matches conversational queries using regular expressions.
- **Dynamic Responses**: Provides real-time dynamic date and time responses using Python's `datetime` module.
- **Randomized Outputs**: Selects from multiple response variations to make dialogue feel natural.
- **Fallback Handling**: Gracefully handles unknown inputs by suggesting possible questions.
- **Clean Console UI**: Intuitive turn-by-turn chat interface with graceful exit handling.

---

## 🧠 Technologies & Concepts
- **Python Standard Library**: No external dependencies needed (`re`, `random`, `datetime`).
- **Regular Expressions**: Flexible pattern matching for user intents.
- **Dictionaries & Lambdas**: Mapping triggers to dynamic handler functions and canned text lists.

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x installed.

### Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/CodeAlpha_BasicChatbot.git
   ```
2. Navigate into the folder:
   ```bash
   cd CodeAlpha_BasicChatbot
   ```
3. Run the script:
   ```bash
   python chatbot.py
   ```

---

## 💬 Sample Interaction
```text
==================================================
           WELCOME TO ALPHABOT CHAT            
==================================================
Hi! I am AlphaBot. Type 'help' for topics or 'bye' to exit.

You: hello
AlphaBot: Hey there! What's on your mind?

You: what time is it
AlphaBot: The current time is 04:15:30 PM.

You: tell me a joke
AlphaBot: Why do Python programmers prefer dark mode? Because light attracts bugs!

You: bye
AlphaBot: Bye! Have a great day ahead! Take care!
```

---

## 👤 Author
- **Author**: Vidhi
- **Internship**: Python Programming Internship at **CodeAlpha**
- **Website**: [CodeAlpha](https://www.codealpha.tech)
