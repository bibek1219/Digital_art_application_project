import tkinter as tk

# Function to start drawing
def start_drawing(event):
    global is_drawing
    is_drawing = True
    x, y = event.x, event.y
    canvas.create_oval(x, y, x, y, width=brush_size, fill=current_color, outline=current_color)

# Function to draw lines
def draw(event):
    global is_drawing
    if is_drawing:
        x, y = event.x, event.y
        canvas.create_line(prev_x, prev_y, x, y, width=brush_size, fill=current_color)
        prev_x, prev_y = x, y

# Function to stop drawing
def stop_drawing(event):
    global is_drawing
    is_drawing = False

# Function to change brush size
def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

# Function to change brush color
def change_brush_color(new_color):
    global current_color
    current_color = new_color

# Create the main application window
root = tk.Tk()
root.title("Simple Digital Art")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Variable to keep track of drawing state
is_drawing = False
prev_x, prev_y = 0, 0

# Default brush size and color
brush_size = 3
current_color = "black"

# Bind mouse events to drawing functions
canvas.bind("<ButtonPress-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

# Create buttons for changing brush size and color
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

sizes = [1, 3, 5, 8, 10]
for size in sizes:
    tk.Button(button_frame, text=str(size), width=3, command=lambda size=size: change_brush_size(size)).pack(side=tk.LEFT)

colors = ["black", "red", "blue", "green", "yellow", "orange","pink","purple","grey"]
for color in colors:
    tk.Button(button_frame, width=3, bg=color, command=lambda color=color: change_brush_color(color)).pack(side=tk.LEFT)

root.mainloop()