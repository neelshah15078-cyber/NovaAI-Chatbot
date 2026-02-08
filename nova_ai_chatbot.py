import datetime
import random
from difflib import get_close_matches

KNOWLEDGE_BASE = {
    "what is ai": "AI (Artificial Intelligence) allows machines to simulate human intelligence.",
    "what is machine learning": "Machine Learning is a part of AI where systems learn from data.",
    "what is python": "Python is a popular programming language used in AI and software development.",
    "who is albert einstein": "Albert Einstein developed the theory of relativity.",
    "what is the capital of India": "The capital of India is New Delhi.",
    "what is pi": "Pi (π) is approximately 3.14159."
}

GREETINGS = {
    "patterns": ["hello", "hi", "hey"],
    "responses": [
        "Hello! I am NovaAI 🤖. How can I help you?",
        "Hi there! Ask me anything.",
        "Hey! I'm ready to help."
    ]
}

FAREWELLS = {
    "patterns": ["bye", "exit", "quit"],
    "responses": [
        "Goodbye! Have a great day 😊",
        "See you later!"
    ]
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs 😄",
    "Why was the math book sad? It had too many problems 📚"
]

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def calculate(expression):
    try:
        expression = expression.replace("calculate", "").strip()
        allowed = set("0123456789+-*/.() ")

        if not all(char in allowed for char in expression):
            return "Invalid characters used."

        return f"Answer: {eval(expression)}"
    except:
        return "Invalid calculation."

def find_match(user_input):
    questions = list(KNOWLEDGE_BASE.keys())
    match = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    return match[0] if match else None

def generate_response(user_input):
    text = user_input.lower()

    if "who are you" in text:
        return "I am NovaAI, your virtual assistant."

    if any(word == text for word in GREETINGS["patterns"]):
        return random.choice(GREETINGS["responses"])

    if any(word in text for word in FAREWELLS["patterns"]):
        return random.choice(FAREWELLS["responses"])

    if "time" in text:
        return f"Current time is {get_time()}"

    if "date" in text:
        return f"Today's date is {get_date()}"

    if "calculate" in text:
        return calculate(text)

    if "joke" in text:
        return random.choice(JOKES)

    match = find_match(text)
    if match:
        return KNOWLEDGE_BASE[match]

    return "I'm still learning. Please ask something else."

def chatbot():
    print("\n===== NOVA AI CHATBOT =====")
    print("Type 'bye' to exit\n")

    while True:
        user = input("You: ")

        if any(word in user.lower() for word in ["bye", "exit", "quit"]):
            print("NovaAI: Goodbye!")
            break

        print("NovaAI:", generate_response(user))
        print()

if __name__ == "__main__":
    chatbot()
