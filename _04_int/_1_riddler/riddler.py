"""
* Write a python program that asks the user a minimum of 3 riddles.
  messagebox.
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
riddle = simpledialog.askstring(title='riddle', prompt='Do you want hard or easy riddles?')
if riddle == 'hard':
    hard = simpledialog.askstring(title='riddle', prompt='The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?')
    if hard == 'coffin':
        messagebox.showinfo(title='riddle', message='you got it!')
    else:
        messagebox.showinfo(title='riddle', message='It is wrong!')

elif riddle == 'easy':
    easy = simpledialog.askstring(title='riddle', prompt='I’m tall when I’m young, and I’m short when I’m old. What am I?')
    if easy == 'candle':
        messagebox.showinfo(title='riddle', message='you got it!')
    else:
        messagebox.showinfo(title='riddle', prompt='It is wrong')
