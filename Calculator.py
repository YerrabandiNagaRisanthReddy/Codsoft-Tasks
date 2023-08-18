# Import Tkinter from python library
from tkinter import *

# MAKE A GUI WINDOW OF DESIRED SIZE
root = Tk()

# geometry - Width x Height
root.geometry("400x650")

root.title("CALCULATOR")

# Change the Icon to desired ico file 
root.wm_iconbitmap("GUI\ASSETS\calculator_Icon.ico")


# INSERT ENTRY WINDOW AND SET THE STRING VARIABLE TO BLANK TEXT
# THIS WILL BE THE SCREEN FOR THE CALCULATOR
screenval = StringVar()
screenval.set("")

screen = Entry(root, textvariable = screenval, justify = RIGHT, 
        font = "TimesNewRoman 40 bold", cursor = "xterm")
screen.pack(fill = X, padx = 5, pady = 10)


# DEFINE FUNCTIONS WHICH ARE TO BE USED WHEN THE BUTTON IS CLICKED - COMMAND FUNCTIONS
def Clear(event) : 
    screenval.set("")
    screen.update()
    print(screenval.get())

def equal(event) : 
    value = eval(screen.get())
    screenval.set(value)
    screen.update()
    print(value)

def value(event) : 
    global screenval
    text = event.widget.cget("text")
    print(text)
    screenval.set(screenval.get() + text)
    screen.update()

def symbol(event) : 
    global screenval
    text = event.widget.cget("text")
    print(text)
    screenval.set(screenval.get() + text)
    screen.update()

# MAKE FRAMES AND INSERT BUTTONS IN EACH ROW
f1 = Frame(root)

bCl = Button(f1, text = "C", font = "Lucida 20 bold",
        padx = 4, pady = 5, cursor = "hand2")
bCl.pack(side = LEFT, padx = 72, pady = 5)
bCl.bind("<Button-1>", Clear)

bE = Button(f1, text = "=", font = "Lucida 20 bold",
        padx = 4, pady = 5, cursor = "hand2")
bE.pack(side = LEFT, padx = 72, pady = 5)
bE.bind("<Button-1>", equal)

f1.pack(pady = 30)


f2 = Frame(root)

b7 = Button(f2, text = "7", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b7.pack(side = LEFT, padx = 8, pady = 5)
b7.bind("<Button-1>", value)

b8 = Button(f2, text = "8", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b8.pack(side = LEFT, padx = 8, pady = 5)
b8.bind("<Button-1>", value)

b9 = Button(f2, text = "9", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b9.pack(side = LEFT, padx = 8, pady = 5)
b9.bind("<Button-1>", value)

bPl = Button(f2, text = "+", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
bPl.pack(side = LEFT, padx = 8, pady = 5)
bPl.bind("<Button-1>", symbol)

f2.pack()


f3 = Frame(root)

b4 = Button(f3, text = "4", font = "Lucida 20 bold", 
        padx = 5, pady = 5, cursor = "hand2")
b4.pack(side = LEFT, padx = 8, pady = 5)
b4.bind("<Button-1>", value)

b5 = Button(f3, text = "5", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b5.pack(side = LEFT, padx = 8, pady = 5)
b5.bind("<Button-1>", value)

b6 = Button(f3, text = "6", font = "Lucida 20 bold", 
        padx = 5, pady = 5, cursor = "hand2")
b6.pack(side = LEFT, padx = 8, pady = 5)
b6.bind("<Button-1>", value)

bMi = Button(f3, text = "-", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
bMi.pack(side = LEFT, padx = 8, pady = 5)
bMi.bind("<Button-1>", symbol)

f3.pack(pady = 30)


f4 = Frame(root)

b1 = Button(f4, text = "1", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b1.pack(side = LEFT, padx = 8, pady = 5)
b1.bind("<Button-1>", value)

b2 = Button(f4, text = "2", font = "Lucida 20 bold", 
        padx = 5, pady = 5, cursor = "hand2")
b2.pack(side = LEFT, padx = 8, pady = 5)
b2.bind("<Button-1>", value)

b3 = Button(f4, text = "3", font = "Lucida 20 bold" ,
        padx = 5, pady = 5, cursor = "hand2")
b3.pack(side = LEFT, padx = 8, pady = 5)
b3.bind("<Button-1>", value)

bMu = Button(f4, text = "*", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
bMu.pack(side = LEFT, padx = 8, pady = 5)
bMu.bind("<Button-1>", symbol)

f4.pack()


f5 = Frame(root)

b0 = Button(f5, text = "0", font = "Lucida 20 bold",
        padx = 5, pady = 5, cursor = "hand2")
b0.pack(side = LEFT, padx = 10, pady = 5)
b0.bind("<Button-1>", value)

bPo = Button(f5, text = ".", font = "Lucida 25 bold",
        padx = 5, pady = 2, cursor = "hand2")
bPo.pack(side = LEFT, padx = 9, pady = 3)
bPo.bind("<Button-1>", symbol)

bDi = Button(f5, text = "/", font = "Lucida 20 bold",
        padx = 6, pady = 5, cursor = "hand2")
bDi.pack(side = LEFT, padx = 8, pady = 5)
bDi.bind("<Button-1>", symbol)

bPe = Button(f5, text = "%", font = "Lucida 20 bold",
        padx = 3, pady = 5, cursor = "hand2")
bPe.pack(side = LEFT, padx = 8, pady = 5)
bPe.bind("<Button-1>", symbol)

f5.pack(pady = 30)

root.mainloop()