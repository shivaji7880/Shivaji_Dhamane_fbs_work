import tkinter as tk
from tkinter import messagebox


questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    }
]


current_question = 0
score = 0


def show_question():
    question = questions[current_question]

    label_question.config(
        text=question["question"]
    )

    for i in range(4):
        buttons[i].config(
            text=question["options"][i]
        )


def check_answer(selected):
    global current_question
    global score

    correct_answer = questions[current_question]["answer"]

    if selected == correct_answer:
        score += 1
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showerror(
            "Result",
            "Incorrect Answer!\nCorrect Answer: " + correct_answer
        )

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            "Your Score: " + str(score) +
            "/" + str(len(questions))
        )

        root.destroy()


root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x350")


label_question = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=450
)

label_question.pack(pady=30)


buttons = []

for i in range(4):
    button = tk.Button(
        root,
        text="",
        width=30,
        command=lambda i=i: check_answer(
            buttons[i].cget("text")
        )
    )

    button.pack(pady=5)
    buttons.append(button)


show_question()

root.mainloop()