import os
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

folder = os.listdir("/home/armigofire/factoria_f5/pills/python/python-pill/slides")
for file in folder:
    print(file)

root = tk.Tk()
root.title("PYTHON PILL")
root.geometry("800x600+100+100")
root.resizable(False, False)
""" root.iconbitmap("") """    # ICON

img =  ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/" + file))

label1 = tk.Label(image=img)
label1.image = img

label1.place(x=0, y=0)

""" message = tk.Label(root, text="Haii:3")
message.pack() """

root.mainloop()
