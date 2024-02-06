import tkinter as tk

root = tk.Tk()

root.title("Place System")

label1 = tk.Label(root, text="Title 1", bg="yellow")
label2 = tk.Label(root, text="Title 2", bg="green")
label3 = tk.Label(root, text="Title 3", bg="black", fg="white")

label1.place(x=0, y=0)
label2.place(relx=0.8, rely=0.4)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
