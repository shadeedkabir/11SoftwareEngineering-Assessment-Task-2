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
}

]