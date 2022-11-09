from tkinter import *
from PIL import ImageTk, Image

def forward(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])

    button_back = Button(root, text='<--', command=lambda: back(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(root, text='-->', state=DISABLED)
    else:
        button_forward = Button(root, text='-->', command=lambda: forward(image_number+1))
    
    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text='-->', command=lambda: back(image_number+1))

    if image_number == 1:
        button_back = Button(root, text='<--', state=DISABLED)
    else:
        button_back = Button(root, text='<--', command=lambda: back(image_number-1))
    
    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

root = Tk()
root.title('Epic Romantic Slideshow')
image1 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/0-portada.png"))
image2 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/1-slide.png"))
image3 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/2-slide.png"))
image4 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/3-slide.png"))
image5 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/4-slide.png"))
image6 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/5-slide.png"))
image7 = ImageTk.PhotoImage(Image.open("/home/armigofire/factoria_f5/pills/python/python-pill/slides/6-slide.png"))
image_list = [image1, image2, image3, image4, image5, image6, image7]

image_label = Label(image=image1)
image_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text='<--', state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='-->', command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()