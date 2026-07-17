import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# FAQ Dataset
faq_data = {
    "what is python": "Python is a high-level, interpreted programming language.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is java": "Java is an object-oriented programming language.",
    "what is c language": "C is a powerful procedural programming language.",
    "what is c++": "C++ is an object-oriented programming language.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript adds interactivity to websites.",
    "what is ai": "Artificial Intelligence enables machines to simulate human intelligence.",
    "what is machine learning": "Machine Learning allows systems to learn from data.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning using neural networks.",
    "what is data science": "Data Science is the study of extracting insights from data.",
    "what is database": "A database stores and manages data.",
    "what is sql": "SQL is used to manage relational databases.",
    "what is dbms": "DBMS stands for Database Management System.",
    "what is operating system": "An operating system manages computer hardware and software.",
    "what is linux": "Linux is an open-source operating system.",
    "what is windows": "Windows is an operating system developed by Microsoft.",
    "what is internet": "The Internet is a global network connecting computers.",
    "what is cloud computing": "Cloud computing provides computing services over the internet.",
    "what is github": "GitHub is a platform for hosting Git repositories.",
    "what is git": "Git is a version control system.",
    "what is api": "API allows communication between software applications.",
    "what is compiler": "A compiler translates source code into machine code.",
    "what is interpreter": "An interpreter executes code line by line.",
    "what is variable": "A variable stores data values.",
    "what is function": "A function is a reusable block of code.",
    "what is loop": "Loops execute a block of code repeatedly.",
    "what is list": "A list stores multiple items in one variable.",
    "what is tuple": "A tuple is an ordered immutable collection.",
    "what is dictionary": "A dictionary stores key-value pairs.",
    "what is set": "A set stores unique elements.",
    "what is class": "A class is a blueprint for creating objects.",
    "what is object": "An object is an instance of a class.",
    "what is inheritance": "Inheritance allows one class to inherit another.",
    "what is polymorphism": "Polymorphism allows one interface to have multiple implementations.",
    "what is encapsulation": "Encapsulation binds data and methods together.",
    "what is abstraction": "Abstraction hides implementation details.",
    "what is recursion": "Recursion is a function calling itself.",
    "what is algorithm": "An algorithm is a step-by-step procedure to solve a problem.",
    "what is flowchart": "A flowchart is a graphical representation of an algorithm.",
    "what is binary search": "Binary search works on sorted arrays.",
    "what is linear search": "Linear search checks elements one by one.",
    "what is stack": "Stack follows LIFO principle.",
    "what is queue": "Queue follows FIFO principle.",
    "what is linked list": "Linked List stores nodes connected by pointers.",
    "what is tree": "Tree is a hierarchical data structure.",
    "what is graph": "Graph consists of nodes and edges.",
    "what is recursion error": "RecursionError occurs when recursion exceeds the limit.",
    "what is exception": "Exceptions are runtime errors.",
    "what is try except": "Try-except handles exceptions.",
    "what is file handling": "File handling is used to read and write files.",
    "what is oop": "OOP stands for Object-Oriented Programming.",
    "what is tkinter": "Tkinter is Python's GUI library.",
    "what is numpy": "NumPy is used for numerical computing.",
    "what is pandas": "Pandas is used for data analysis.",
    "what is matplotlib": "Matplotlib is used for plotting graphs.",
    "what is flask": "Flask is a lightweight Python web framework.",
    "what is django": "Django is a high-level Python web framework.",
    "what is chatbot": "A chatbot is a software that simulates conversation.",
    "what is nlp": "NLP stands for Natural Language Processing."
}

print("FAQ Dataset Loaded Successfully!")
# ---------------- NLP PREPROCESSING ----------------

stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Prepare questions
questions = list(faq_data.keys())
answers = list(faq_data.values())

clean_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(clean_questions)

print("NLP Processing Completed Successfully!")
# ---------------- FIND BEST MATCH ----------------

def get_answer(user_input):
    user_input = preprocess(user_input)

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()
    best_score = similarity[0][best_match]

    if best_score > 0.25:
        return answers[best_match]
    else:
        return "Sorry, I couldn't understand your question. Please ask another question."
        # ---------------- CHATBOT ----------------

print("\n===================================")
print("      FAQ CHATBOT")
print("Type 'exit' to quit")
print("===================================\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you for using the FAQ Chatbot. Goodbye!")
        break

    response = get_answer(user_input)
    print("Bot:", response)

