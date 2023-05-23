from tkinter import *
from tkinter import messagebox
import browse

def submit():
    try:
        link = str(e1.get())
        views = int(e2.get())
        browse.getView(link, views) 
        top.quit()
    except:
        top.quit()

# Create the main Tkinter window
top = Tk()
top.title("Get YouTube Views")
top.geometry("400x100")
top.resizable(0,0)
top.configure(background="red")
top.iconbitmap('youtube.ico')

# Create and place the "Paste your link" label
l1 = Label(top, text="Paste your link", bg="red", font=("Arial", 11))
l1.place(x=10,y=10)

# Create and place the entry field for YouTube link
e1 = Entry(top, width=45)
e1.place(x=115,y=10)
e1.focus_set()

# Create and place the "Number of views" label
l2 = Label(top, text="Number of views", bg="red", font=("Arial", 11))
l2.place(x=10,y=40)

# Create and place the entry field for number of views
e2 = Entry(top, width=20)
e2.place(x=115,y=40)
e2.focus_set()

# Create the "Submit Now" button
btn = Button(top, text="Submit Now", command=submit)
btn.place(x=250, y=40)

# Start the Tkinter event loop
top.mainloop()