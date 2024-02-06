import tkinter as tk

root = tk.Tk()

root.title("My First GUI with Python")

label = tk.Label(root, text="Hello World!")
label.pack()

def tmp():
    print("\n[INFO] Button was clicked!")


button = tk.Button(root, text="Click Me!", command=tmp)
button.pack()


root.mainloop()
