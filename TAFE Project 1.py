import tkinter
import tkinter as tk

root = tkinter.Tk()

l1 = tk.Label(root, text="Login")
l2 = tk.Label(root, text="Username:")
l3 = tk.Label(root, text="Password:")

l1.grid(row=0, column=1, sticky="W", pady=2)
l2.grid(row=1, column=0, sticky="W", pady=2)
l3.grid(row=2, column=0, sticky="W", pady=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=1, column=1, pady=2)
e2.grid(row=2, column=1, pady=2)

b1 = tk.Button(text="Submit")
b1.grid(row=4, column=3, sticky="W", pady=2)

root.mainloop()