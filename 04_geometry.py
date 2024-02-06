import tkinter as tk

root = tk.Tk()

root.geometry("400x100")
root.title("Place System")

label1 = tk.Label(root, text="This is a label", bg="yellow")
label2 = tk.Label(root, text="This is a label", bg="green")
label3 = tk.Label(root, text="This is a label", bg="black", fg="white")

label1.place(x=20, y=20)
label2.place(relx=0.8, rely=0.2)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
