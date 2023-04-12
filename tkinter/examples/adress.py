import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

# List of field labels
labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

for id, text in enumerate(labels):

    label = tk.Label(master=frm_form, text=text)
    entry = tk.Entry(master=frm_form, width=50)

    label.grid(row=id, column=0, sticky="e")
    entry.grid(row=id, column=1)

frm_button = tk.Frame()
frm_button.pack(fill=tk.X, padx=5, pady=5)

btn_submit = tk.Button(master=frm_button, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_button, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()