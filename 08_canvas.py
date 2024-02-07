import tkinter as tk

root = tk.Tk()

root.geometry("300x350")
root.title("canvas System")

canvas = tk.Canvas(root, width="100", height="100", bg="black")
canvas.pack(pady=10)

oval = canvas.create_oval(10, 10, 80, 80, fill="red")
arc = canvas.create_arc(10, 10, 80, 80, start=0, extent=180, fill="blue")
line = canvas.create_line(10, 10, 80, 80, fill="yellow")

root.mainloop()
