# Import tkinter modules from Python Libraries
from tkinter import *
from tkinter import messagebox

# Define a function that adds tasks to the list
def newTask():
    task = my_entry.get()
    if task != "":
        list.insert(ANCHOR, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# Define a function that deletes taks from the list
def deleteTask():
    list.delete(ANCHOR)
    
# Create a GUI Window
ws = Tk()
ws.geometry('500x450+500+200')

# Add desired Title
ws.title('TO-DO LIST')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

# Make a frame using Frame widget
frame = Frame(ws)
frame.pack(pady=10)

# Make a list using listbox widget and place it in frame created before
list = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",   
)
list.pack(side=LEFT, fill=BOTH)

# create a list variable and make it blank for adding tasks to the list area
task_list = []

for item in task_list:
    list.insert(END, item)

# add a scrollbar for easier navigation
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=BOTH)

list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

# Create an entry eidget to enter tasks that are to be added
my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

# Make a button that says "ADD TASKS" and assign a function to it
# that adds tasks to the list
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Make a button that says "DELETE TASKS" and assign a function to it
# That deletes tasks from the list
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()