import tkinter as tk
root = tk.Tk()
root.title()
root.size(400,400)
cb = tk.Checkbutton(root, text = "Click me")
cb.pack()
rb = tk.Radiobutton(root,text = "Radio Button")
rb.pack()
b = tk.Button(root,text = "Button")
b.pack()
root.mainloop()
