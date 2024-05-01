import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
#
# root window
root = tk.Tk()
#root.title('Medical ChatBot')
#root.geometry('300x70')
#root.resizable(False, False)
# place a label on the root window
message = tk.Label(root, text="How can I help you?")
message.pack()


# keep the window displaying

root.mainloop()
