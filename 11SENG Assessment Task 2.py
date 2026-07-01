# Imports
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Windows
root = Tk()
root.title("Worlds Flag Quiz")
root.geometry("900x600")
root.configure(bg="#89E5FF")
root.resizable(False, False)

# Global Variables
score = 0
question_number = 0
current_question = {}
flag_photo = None

# Questions
questions = [

{
    "image":"images/australia.png",
    "correct":"Australia",
    "options":[
        "Australia", 
        "New Zealand", 
        "Fiji", 
        "United Kingdom",
    ]
},

{
    "image":"images/japan.png",
    "correct":"Japan",
    "options":[
        "China",
        "Japan",
        "South Korea",
        "Vietnam"
    ]
},

{
    "image":"images/canada.png",
    "correct":"Canada",
    "options":[
        "Canada",
        "USA",
        "Austria",
        "France"
    ]
},

{
    "image":"images/brazil.png",
    "correct":"Brazil",
    "options":[
        "Brazil",
        "Argentina",
        "Mexico",
        "Portugal"
    ]
},

{
    "image":"images/france.png",
    "correct":"France",
    "options":[
        "France",
        "Italy",
        "Belgium",
        "Netherlands"
    ]
},

{
    "image":"images/germany.png",
    "correct":"Germany",
    "options":[
        "Germany",
        "Belgium",
        "Austria",
        "Switzerland"
    ]
},

{
    "image":"images/india.png",
    "correct":"India",
    "options":[
        "India",
        "Pakistan",
        "Bangladesh",
        "Sri Lanka"
    ]
},

{
    "image":"images/italy.png",
    "correct":"Italy",
    "options":[
        "Italy",
        "France",
        "Ireland",
        "Mexico"
    ]
},

{
    "image":"images/china.png",
    "correct":"China",
    "options":[
        "China",
        "Vietnam",
        "Japan",
        "South Korea"
    ]
},

{
    "image":"images/usa.png",
    "correct":"United States",
    "options":[
        "United States",
        "Australia",
        "Liberia",
        "United Kingdom"
    ]
}

]

# Shuffle questions
random.shuffle(questions)

# Functions
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# Closing the program
def exit_program():
    root.destroy()


# Loads and resizes the flag image
def load_flag(image_path):

    global flag_photo

    try:

        image = Image.open(image_path)

        # Resizing flag to fit neatly on the screen
        image = image.resize((320, 200))

        flag_photo = ImageTk.PhotoImage(image)

        return flag_photo

    except:

        return None
    

# Instructions Page

def instructions_page():

    clear_screen()

    title = Label(
        root,
        text="Instructions",
        font=("Arial",30,"bold"),
        bg="#B9E6FF"
    )
        
    title.pack(pady=20)

    instructions = Label(
        root,
        text="""• A flag will appear on the screen.

• Choose the correct country.

• There are four answer choices.

• Each correct answer earns 1 point.

• Your total score is shown at the end.

• Good luck!""",
        font=("Arial",16),
        justify=LEFT,
        bg="#B9E6FF"
    )
    instructions.pack(pady=20)

    begin_button = Button(
        root,
        text="BEGIN QUIZ",
        width=20,
        font=("Arial",14),
        command=start_quiz
    )

    begin_button.pack(pady=15)

    back_button = Button(
        root,
        text="BACK",
        width=20,
        font=("Arial",14),
        command=welcome_page
    )

    back_button.pack()


# Welcome Page

def welcome_page():

    clear_screen()

    # Title

    title = Label(
        root,
        text="World\nFlags Quiz",
        font=("Arial",34,"bold"),
        bg="#B9E6FF",
        fg="navy"
    )

    title.pack(pady=40)

    # Description

    description = Label(
        root,
        text="Test your knowledge of flags from around the world!\n"
             "Can you identify every country correctly?",
        font=("Arial",16),
        bg="#B9E6FF"
    )

    description.pack(pady=20)

    # Buttons

    next_button = Button(
        root,
        text="NEXT",
        width=18,
        font=("Arial",14),
        command=instructions_page
    )

    next_button.pack(pady=15)

    exit_button = Button(
        root,
        text="EXIT",
        width=18,
        font=("Arial",14),
        command=exit_program
    )

    exit_button.pack()


# Start Quiz

def start_quiz():

    global score
    global question_number

    score = 0
    question_number = 0

    random.shuffle(questions)

    display_question()


# Display Question

def display_question():

    global current_question
    global flag_photo

    clear_screen()

    # Get the current question
    current_question = questions[question_number]

    # Heading

    heading = Label(
        root,
        text=f"Question {question_number + 1} of {len(questions)}",
        font=("Arial",18,"bold"),
        bg="#B9E6FF"
    )

    heading.pack(pady=10)

    # Score

    score_label = Label(
        root,
        text=f"Score: {score}",
        font=("Arial",16),
        bg="#B9E6FF"
    )

    score_label.pack()

    # Loading Flag

    flag_photo = load_flag(current_question["image"])

    if flag_photo != None:

        flag_label = Label(
            root,
            image=flag_photo,
            bg="#B9E6FF"
        )

        flag_label.pack(pady=20)

    else:

        missing = Label(
            root,
            text="Image could not be loaded.",
            font=("Arial",16),
            fg="red",
            bg="#B9E6FF"
        )

        missing.pack(pady=20)

    # Answer Buttons

    for option in current_question["options"]:

        answer_button = Button(
            root,
            text=option,
            width=25,
            font=("Arial",14),
            command=lambda answer=option: check_answer(answer)
        )

        answer_button.pack(pady=5)

