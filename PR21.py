import tkinter as tk
root = tk.Tk()
cb = tk.Checkbutton(root, text = "Click me" , command = root.destroy)
cb.pack()
root.mainloop()
