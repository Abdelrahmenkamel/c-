import tkinter as tk
from tkinter import colorchooser

def activate_robo_painter():
    robo_painter.activate()

def set_canvas_width_height():
    width = int(width_entry.get())
    height = int(height_entry.get())
    robo_painter.set_canvas(width, height)

def change_color():
    color = colorchooser.askcolor()[1]  # Get color in hex format
    if color:
        rgb_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))  # Convert hex to RGB
        robo_painter.change_brush_color(rgb_color)

def draw_on_canvas():
    x = int(x_entry.get())
    y = int(y_entry.get())
    robo_painter.draw_point(x, y)
    robo_painter.display_canvas()

robo_painter = RoboPainter()

# GUI setup
root = tk.Tk()
root.title("RoboPainter Control")

# Canvas size
tk.Label(root, text="Canvas Width:").pack()
width_entry = tk.Entry(root)
width_entry.pack()
tk.Label(root, text="Canvas Height:").pack()
height_entry = tk.Entry(root)
height_entry.pack()
tk.Button(root, text="Set Canvas", command=set_canvas_width_height).pack()

# Change color
tk.Button(root, text="Change Brush Color", command=change_color).pack()

# Draw coordinates
tk.Label(root, text="X Coordinate:").pack()
x_entry = tk.Entry(root)
x_entry.pack()
tk.Label(root, text="Y Coordinate:").pack()
y_entry = tk.Entry(root)
y_entry.pack()
tk.Button(root, text="Draw", command=draw_on_canvas).pack()

# Activate RoboPainter
tk.Button(root, text="Activate RoboPainter", command=activate_robo_painter).pack()

root.mainloop()
