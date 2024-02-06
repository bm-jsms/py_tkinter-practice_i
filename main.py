import tkinter as tk

root = tk.Tk()

root.title("My First GUI with Python")

label = tk.Label(root, text="Hello World!", font=("Arial", 40), bg="yellow", fg="blue")
label.pack(fill=tk.X)


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
