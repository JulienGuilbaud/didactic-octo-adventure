import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image  # Import the necessary modules

def function1():
    # Placeholder for function 1's actual code
    print("Function 1 executed")
    goodbye()


def function2():
    # Placeholder for function 2's actual code
    print("Function 2 executed")
    goodbye()


def function3():
    # Placeholder for function 3's actual code
    print("Function 3 executed")
    goodbye()

def goodbye():
    messagebox.showinfo("Au Revoir", "Merci et au revoir!")
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Function Executor")

# Style for a modern look (optional)
style = ttk.Style()
style.theme_use("clam")  # Or explore other themes like 'aqua', 'alt', etc.

# Frame for buttons
button_frame = ttk.Frame(root, padding="20")
button_frame.pack()

# Add the company logo
try:
    logo = Image.open("asset/2.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(root, image=logo)
    logo_label.pack(pady=(0, 20)) # Add some spacing below the logo
except FileNotFoundError:
    print("Logo file not found.")  # Handle the case where the image isn't found
    
# Buttons
button1 = ttk.Button(button_frame, text="Function 1", command=function1)
button1.pack(pady=10)

button2 = ttk.Button(button_frame, text="Function 2", command=function2)
button2.pack(pady=10)

button3 = ttk.Button(button_frame, text="Function 3", command=function3)
button3.pack(pady=10)



root.mainloop()

