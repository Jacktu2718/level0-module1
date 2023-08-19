import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    jack=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    drawshape=simpledialog.askstring(title='shape selector', prompt='What shape do you want to draw?')
    # Draw the shape requested by the user using if-elif-else statements
if drawshape=='triangle':
    jack.forward(100)
    jack.right(120)
    jack.forward(100)
    jack.right(120)
    jack.forward(100)
if drawshape=='square':
    for i in range(3):
        jack.forward(100)
        jack.right(270)
    jack.forward(100)

    # Call the turtle .done() method
