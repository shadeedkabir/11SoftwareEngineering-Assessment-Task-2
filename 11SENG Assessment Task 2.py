from tkinter import *#imports all symbols from the tkinter module into the current name:
def button_click():
    label2=Label(root, text="Welcome to the multiplication quiz!")
    label2.place(x=150, y=50)


root =Tk()
root.title("Example of Button")
root.geometry("400x400") #make the window 400 x 400 size


button1=Button(root,text="Start", command=button_click)
button1.place(x=165,y=300)


root.mainloop()