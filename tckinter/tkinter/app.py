import tkinter as tk

window = tk.Tk() # creating the window

label = tk.Label( # adding text
    text="Yoo",
    
    foreground="white",
    background="black",

    width=10,
    height=10
    ) 

button = tk.Button(
    text="Click me!",

    bg="blue",
    fg="yellow",

    width=25,
    height=5,
)

entry = tk.Entry(
    fg="yellow", 
    bg="blue", 

    width=50
)

text = tk.Text(
    fg="yellow", 
    bg="blue",
)

# Retrieve text with .get()
# Delete text with .delete()
# Insert text with .insert()


# text.pack()
# entry.pack()
# button.pack()
# label.pack() # applying the widget

window.mainloop() # running the window
