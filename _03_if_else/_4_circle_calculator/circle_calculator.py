# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()
radius = simpledialog.askinteger(title='Radius', prompt='what is the radius of any circle?')
circle = simpledialog.askstring(title='Radius', prompt='Would you calculate the area or the circumference?')
if circle == 'area':
    area = math.pi * (radius ** 2)
    print("area is " + str(area))
elif circle == 'circumference':
    circumference = 2 * math.pi * radius
    print("circumference is " + str(circumference))



#Area = πr^2
#Circumference = 2πr 
