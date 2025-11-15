# Program #2: Show Info and Quit Buttons
# Author: Zepora Lilly
# Date: 11/14/2025

import tkinter as tk

def show_info():
    info_label.config(text="Zepora Lilly\n13667 86th Pl N\nMaple Grove, MN 55369")

# Create the main window
root = tk.Tk()
root.title("Personal Info")

# Create a label to display the info
info_label = tk.Label(root, text="", font=("Arial", 12), pady=20)
info_label.pack()

# Create the Show Info button
show_button = tk.Button(root, text="Show Info", command=show_info)
show_button.pack(pady=10)

# Create the Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Run the application

root.mainloop()
