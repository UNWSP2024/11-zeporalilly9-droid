# Program#1: Display your favorite saying
# Author: Zepora Lilly
# Date: 11/14/2025

import tkinter as tk

# Create the main window
root = tk. Tk()
root.title("Favorite Saying")

# Create a label with your favorite saying
saying = "Life with God is not immunity from difficulties, but pease within difficulties."
label = tk.Label(root, text=saying, font=("Arial", 14), padx=20, pady=20)
label.pack()

#Run the application

root.mainloop()