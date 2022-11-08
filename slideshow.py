import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
root.title("PYTHON PILL")
root.geometry("800x600+100+100")
root.resizable(False, False)
""" root.iconbitmap("") """

img =  ImageTk.PhotoImage(Image.open("../logo.png"))
message = tk.Label(root, text="Haii:3")
message.pack()

root.mainloop()