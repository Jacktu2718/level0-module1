from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    answer=simpledialog.askstring(title='Unbirthday',prompt='when is your birthday?')
    if answer=='8/18':
        messagebox.showinfo(title='Unbirthday', message='Happy Birthday!')
    else:
        messagebox.showinfo(title='Unbirthday', message='Unhappy Birthday!HA!HA!')
