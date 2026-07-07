import random

faq = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "I am an Offline FAQ Chatbot.",
    "who created you": "I was created using Python.",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI.",
    "what is chatbot": "A chatbot is a program that answers user questions.",
    "what is programming": "Programming is writing instructions for computers.",
    "what is internet": "The Internet is a global network.",
    "what is cpu": "CPU is the brain of the computer.",
    "what is ram": "RAM is temporary memory used by a computer.",
    "what is rom": "ROM stores permanent data.",
    "what is os": "Operating System manages computer resources.",
    "what is keyboard": "Keyboard is an input device.",
    "what is mouse": "Mouse is a pointing device."
}

# Automatically create many FAQs
for i in range(1, 201):
    faq[f"question {i}"] = f"This is the answer for question {i}."

print("=" * 50)
print("      OFFLINE FAQ CHATBOT")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    elif user in faq:
        print("Bot:", faq[user])

    else:
        suggestions = random.choice([
            "Sorry, I don't know that answer.",
            "Please ask another question.",
            "That question is not available in my database.",
            "Try asking something related to computers or Python."
        ])
        print("Bot:", suggestions)