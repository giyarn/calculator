from tkinter import*
from PIL import ImageTk,Image
window = Tk()
window.iconbitmap('bayanihan.jpg')

my_image1 = ImageTk.PhotoImage(Image.open('images/1.png'))
my_image2 = ImageTk.PhotoImage(Image.open('images/2 (2).png'))
my_image3 = ImageTk.PhotoImage(Image.open('images/3.png'))

imagelist = [my_image1,my_image2,my_image3]


label1 = Label(window,image=my_image1)
label1.grid(row=0,column=0,columnspan=3)

def forward(imageno):
    global label1
    global button_forward
    global button_back

    label1.grid_forget()
    label1 = Label(image=imagelist[imageno - 1])
    button_forward = Button(window,text=">>",command=lambda:forward(imageno + 1))
    button_back = Button(window, text="<<", command=lambda: forward(imageno - 1))
    if imageno == 2:
        button_forward = Button(window,text=">>",state=DISABLED)

    label1.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def back(imageno):
    global label1
    global button_forward
    global button_back

    label1.grid_forget()
    label1 = Label(image=imagelist[imageno - 1])
    button_forward = Button(window,text=">>",command=lambda:forward(imageno + 1))
    button_back = Button(window, text="<<", command=lambda: forward(imageno - 1))
    if imageno == 0:
        button_back = Button(window,text="<<",state=DISABLED)

    label1.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


button_back = Button(window,text="<<",command=back)
button_forward = Button(window,text=">>",command=forward(1))
button_quit = Button(window,text="EXIT",command=window.quit)

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
window.mainloop()