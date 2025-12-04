# 🤓 Quiz App

A simple but extensible **True/False Quiz Application** built with Python, Tkinter, and the Open Trivia Database API.
The app demonstrates clean separation of concerns across data retrieval, model objects, UI, and quiz logic — making it easy to extend into a full-featured learning or game application.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Questions](https://img.shields.io/badge/Questions-OpenTDB_API-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## App Screenshot

```md
<p align="center">
  <img src="images/app_screenshot.png" width="350" alt="Quiz App Screenshot">
</p>
```

---

## Features

* Pulls **live trivia questions** from the Open Trivia Database API
* Clean, responsive **Tkinter GUI** with True/False buttons
* Real-time **score tracking**
* Class-based architecture for easy extension
* Visual feedback (green/red) to reinforce correct/incorrect answers
* Automatically advances through questions
* Clear end-of-quiz message and button disabling

---

## 🗂️ Project Structure

```md
quiz-app/
│
├── images/
│   ├── true.png
│   ├── false.png
│
├── data.py                 # Fetch trivia data from OpenTDB API
├── main.py                 # Entry point that wires all classes together
├── question_model.py       # Question class blueprint
├── quiz_brain.py           # Quiz engine logic
├── ui.py                   # Tkinter GUI class
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/lesliejohnson-io/quiz-gui.git
cd quiz-gui
```

### 2. Install dependencies

(Only built-in Python libraries needed for base project)

```bash
pip install requests
```

---

## Running the App

```bash
python main.py
```

The quiz window will appear with your first question.

---

## 🔧 How It Works

### **1. data.py**

Fetches 10 True/False questions from OpenTDB:

```python
parameters = {"amount": 10, "type": "boolean"}
response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
```

---

### **2. question_model.py**

Defines a `Question` object with `.text` and `.answer`.

---

### **3. quiz_brain.py**

Handles:

* advancing the question index
* verifying answers
* scoring
* checking if questions remain

---

### **4. ui.py**

Tkinter GUI using:

* Canvas for question text
* Labels for score
* Image buttons for True/False
* Background color feedback

---

## 📝 License

MIT License. Free to use and modify.
