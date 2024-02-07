import tkinter as tk

root = tk.Tk()

root.geometry("700x550")
root.title("text System")


def get_data():
    # data = entry_widget.get("3.3", "end") => get data from line 3, column 3 to the end
    data = entry_widget.get("1.0", "end") # get data from line 1, column 0 to the end
    print(f"\n[+] Data by user:\n{data}")


entry_widget = tk.Text(root)
entry_widget.pack(padx=15, pady=15, fill=tk.X)

button = tk.Button(root, text="send", command=get_data)
button.pack(pady=10)

root.mainloop()
