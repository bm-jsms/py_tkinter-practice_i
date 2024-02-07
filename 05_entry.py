import tkinter as tk

root = tk.Tk()

root.geometry("200x100")
root.title("entry System")


def get_data():
    data = entry_widget.get()
    print(f"\n[+] Data by user: {data}")


entry_widget = tk.Entry(root)
entry_widget.pack(padx=10, pady=10, fill=tk.X)

button = tk.Button(root, text="send", command=get_data)
button.pack(pady=10)

root.mainloop()
