# importing wikipedia module
import wikipedia as wiki
# importing tkinter module for gui
from tkinter import *
from tkinter.messagebox import showinfo

# creating window
win = Tk()
# window title
win.title('Wikipedia')
# window size
win.geometry('200x70')

# function for finding summary
def search_wiki():
    # extracting text from entry components
    search = entry.get()
    # extracting summary using wikipedia.summary module
    answer = wiki.summary(search)
    # showing summary in the showinfo messagebox
    showinfo("Wikipedia Answer : ", answer)

# creating label to show text on GUI
label = Label(win, text = "Wikipedia Search : ")
label.grid(row = 0, column = 0)

# creating entry component to get user text to get summary
entry = Entry(win)
entry.grid(row = 1, column = 0)

# creating button for calling search function
button = Button(win, text = "Search", command = search_wiki)
button.grid(row = 1, column = 1, padx = 10)

# looping the window
win.mainloop()