import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

label = tk.Label(root, text="Hello World!", font=("Arial", 20))
label.pack(pady=50)

root.mainloop()