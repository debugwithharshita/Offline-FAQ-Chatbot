# 🤖 FAQ Chatbot using Python

![Python](https://shields.io)
![NLP](https://shields.io)
![Platform](https://shields.io)

A professional, rule-based Intelligent FAQ Chatbot built using Python, Natural Language Processing (NLP), and basic Machine Learning techniques. The application utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to mathematically evaluate user queries and fetch highly accurate responses from a predefined computer science knowledge base.

Optimized to run seamlessly across both standard Desktop IDEs and Android-based terminal environments like Pydroid 3.

---

## ✨ Key Features

* **Advanced Text Preprocessing**: Automates tokenization, case-normalization, punctuation stripping, and English stopword elimination.
* **Vector Space Modeling**: Implements Scikit-Learn's `TfidfVectorizer` to convert unstructured raw string queries into weighted mathematical vectors.
* **Cosine Similarity Matching**: Uses spatial geometry formulas to determine the closest conceptual match between user intent and the database.
* **Strict Confidence Filtering**: Enforces a `0.25` similarity threshold score. If user input is too ambiguous, the bot gracefully triggers a polite fallback prompt.
* **Cross-Platform CLI**: Interactive, memory-efficient command-line loop handling real-time runtime execution.

---

## 🏗️ Project Architecture & Pipeline

```text
 ┌──────────────┐       ┌──────────────────────┐       ┌────────────────────────┐
 │  User Input  │ ───>  │  Text Preprocessing  │ ───>  │  TF-IDF Vectorization  │
 └──────────────┘       │  (NLTK Stopwords)    │       └────────────────────────┘
                        └──────────────────────┘                    │
                                                                    ▼
 ┌──────────────┐       ┌──────────────────────┐       ┌────────────────────────┐
 │ Final Answer │ <───  │ Threshold Validation │ <───  │   Cosine Similarity    │
 └──────────────┘       │      (> 0.25)        │       │   (vs Dataset Keys)    │
                        └──────────────────────┘       └────────────────────────┘
```

---

## 🛠️ Tech Stack & Requirements

* **Core Language**: Python 3.x
* **Primary Frameworks**:
  * `nltk` (Natural Language Toolkit) - String tokenization and semantic filtering.
  * `scikit-learn` - Vector mapping matrix operations.
  * `string` - Standard structural operations.

---

## 📋 Installation & Environment Setup

Ensure you have your environment configured with the required dependencies before bootstrapping the script.

### Desktop Deployment (Windows, macOS, Linux):
Execute the following native pip command in your terminal console:
```bash
pip install nltk scikit-learn
```

### Android Native Deployment (Pydroid 3):
1. Launch the **Pydroid 3** application interface.
2. Select the **Pip** management terminal from the left sidebar navigation menu.
3. Search for `nltk` and `scikit-learn` independently, then click **Install**.

---

## 🚀 Execution Guide

1. Clone the project locally or pull it directly into your active workspace.
2. Fire up the core script via your terminal command structure:
   ```bash
   python faq_chatbot.py
   ```
3. **Note on First Run**: The backend pipeline will automatically parse and sync missing remote packages (`punkt`, `punkt_tab`, `stopwords`) onto your local machine storage.
4. Interact directly within the continuous interface (e.g., *"What is python?"*, *"What is machine learning?"*).
5. Type `exit` smoothly to shut down and de-allocate memory safely.

---

## 👩‍💻 Developer

* **Harshita Jain**

---

## 📄 License

This repository is distributed under the open-source **MIT License**. Feel free to fork, modify, and utilize this project framework for your academic or custom implementations.
