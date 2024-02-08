import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("300x350")
root.title("Menu system")

bar_menu = tk.Menu(root)
root.config(menu=bar_menu)

menu1 = tk.Menu(bar_menu, tearoff=0)
bar_menu.add_cascade(label="Menu", menu=menu1)

menu1.add_command(label="New")
menu1.add_command(label="Open")
menu1.add_command(label="Save")

menu2 = tk.Menu(bar_menu, tearoff=0)
bar_menu.add_cascade(label="Extra", menu=menu2)


def menu_action():
    # 1=Window title, 2=Message
    messagebox.showinfo("Message", "Hi, I'm a extra menu item!")


menu2.add_command(label="eu", command=menu_action)

root.mainloop()
