

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    jack=simpledialog.askstring(title='remarkeble', prompt='What is your name?')
    if "jack" == jack:
        messagebox.showinfo(title='remarkeble',message='Your very funny')
    elif"liam" == jack:
        messagebox.showinfo(title='remarkeble',message='Your so smart')
    elif"James" == jack:
        messagebox.showinfo(title='remarkeble',message='your very confident')
