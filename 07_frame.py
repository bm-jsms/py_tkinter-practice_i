import tkinter as tk

root = tk.Tk()

root.geometry("700x550")
root.title("frame System")

frame = tk.Frame(root, bg="cyan", bd=5)
frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

label = tk.Label(frame, text="My first frame", bg="green")
label.pack()

root.mainloop()
