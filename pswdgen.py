# Import tkinter from python libraries
from tkinter import *

# Import random - To generate Random characters
from random import randint


# Define a function that generates a rondom string of characters with a specified length
def generate():
	password.delete(0, END)
	length=int(charanswer.get())
	pswd = ''
	for x in range(length):
		pswd += chr(randint(33, 126))

	password.insert(0, pswd)
	

# Create a GUI Window
window = Tk()

# Add a desired title
window.title("Password Generator")

# Give the window a desired size
window.geometry('600x500')



# Make a frame to accomodate name entry window
nameframe = LabelFrame(window, text = "ENTER USERNAME : ", font = "timesnewroman 15")
nameframe.pack(padx=10,pady=40)

nameanswer = Entry(nameframe, width = 30, font = "timesnewroman 15")
nameanswer.pack(padx=5,pady=15)


# Make a frame to accomodate entry window for number of characters
charframe = LabelFrame(window, text = "NUMBER OF CHARACTERS ?", font = "timesnewroman 15")
charframe.pack(padx=10, pady=20)

charanswer = Entry(charframe, width = 10, font = "timesnewroman 15")
charanswer.pack(padx=5, pady=10)

# Make a frame to accomodate generate button
Buttonframe = Frame(window)
Buttonframe.pack(pady = 20)

# Make a button named "generate" and place it in frame made above - Give a function that generates password
generateBtn = Button(Buttonframe, text = "GENERATE", font = "lucida 18", command = generate)
generateBtn.grid(row=0, column=2)


# Make an entry window to display the generated password
password = Entry(window, text='', font = "lucida 20")		
password.pack()

window.mainloop()