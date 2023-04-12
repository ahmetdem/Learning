# import tkinter as tk

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# window.mainloop()

#-------------------------------------------------------------------------#

# import tkinter as tk

# window = tk.Tk()

# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)

# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)

# window.mainloop()

#-------------------------------------------------------------------------#

# import tkinter as tk

# window = tk.Tk()

# for i in range(3):

#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)

#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )

#         frame.grid(row=i, column=j, padx=5, pady=5)

#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# window.mainloop()

#-------------------------------------------------------------------------#

# import tkinter as tk

# window = tk.Tk()
# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)

# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="n")

# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="n")

# window.mainloop()

#-------------------------------------------------------------------------#

import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

"""
"n" or "N" to align to the top-center part of the cell
"e" or "E" to align to the right-center side of the cell
"s" or "S" to align to the bottom-center part of the cell
"w" or "W" to align to the left-center side of the cell
"""

window.mainloop()