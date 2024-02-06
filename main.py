import tkinter as tk

root = tk.Tk()

root.title("My First GUI with Python")

label = tk.Label(root, text="Hello World!", font=(
    "Arial", 40), bg="yellow", fg="blue")
label.pack(fill=tk.X)


label2 = tk.Label(root, text="Title 2", font=(
    "Arial", 25), bg="green", fg="white")
label2.pack(fill=tk.X)

label3 = tk.Label(root, text="Title 3", font=(
    "Arial", 25), bg="black", fg="white")
label3.pack(side=tk.LEFT, fill=tk.Y)


def tmp():
    print("\n[INFO] Button was clicked!")


button = tk.Button(root, text="Click Me!", command=tmp)
button.pack()


def exit_app():
    print("\n[INFO] Exiting the application...")
    exit()


exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

root.mainloop()
