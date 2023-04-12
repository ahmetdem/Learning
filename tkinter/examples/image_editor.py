import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("800x800")

image = Image.open("images/peak.png")

thumbnail_size = (800, 800)
image.thumbnail(thumbnail_size)

photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo, anchor="center")

label.grid(row=1, column=0, sticky="nsew")

window.grid_rowconfigure(0,weight=0)
window.grid_rowconfigure(1,weight=1)
window.grid_columnconfigure(0,weight=1)

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

next_button = tk.Button(frm_buttons, text=">")
previous_button = tk.Button(frm_buttons, text="<")

next_button.pack(padx=5, pady=2, ipadx=15, side="right")
previous_button.pack(padx=5, pady=2, ipadx=15, side="right")

frm_buttons.grid(row=0, column=0, sticky="we")

# Start the tkinter event loop
window.mainloop()
