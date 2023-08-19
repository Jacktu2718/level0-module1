# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()
radius=simpledialog.askstring(title='Radius', prompt='what is the radius of any circle?')
if radius=='100':
circle=simpledialog.askstring(title='Radius', prompt='Would you calculate the area or the circumference?')
if circle='area':


#Area = πr^2
#Circumference = 2πr 
