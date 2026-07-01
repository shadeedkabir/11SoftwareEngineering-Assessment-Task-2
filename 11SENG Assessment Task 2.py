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
def clear_screebn():
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