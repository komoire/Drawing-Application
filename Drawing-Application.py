import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Drawing Application")

# Set up a Canvas widget
canvas = tk.Canvas(root, bg='white', width=600, height=400)
canvas.pack()

# Variable to hold the previous mouse position
old_x = None
old_y = None

# Drawing function
def draw(event):
    global old_x, old_y
    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y, width=5, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
    old_x = event.x
    old_y = event.y

# Reset the mouse position when the button is released
def reset(event):
    global old_x, old_y
    old_x, old_y = None, None

# Bind the mouse events to the canvas
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', reset)

# Run the application
root.mainloop()
