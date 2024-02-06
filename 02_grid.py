import tkinter as tk

root = tk.Tk()

root.title("Grid System")

label = tk.Label(root, text="title1!",  bg="yellow")
label2 = tk.Label(root, text="title2!", bg="green")
label3 = tk.Label(root, text="title3!", bg="black", fg="white")

label.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop()
