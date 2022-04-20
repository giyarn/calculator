from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog

window = Tk()
window.title("Window 1")
window.geometry("535x500")

frame = LabelFrame(window,text="Operation",padx=5,pady=5,borderwidth=10,width=65)
frame.grid(row=0,column=0,pady=10,padx=10,columnspan=4)



def click(num):
    current = entry_1.get()
    entry_1.delete(0,END)
    entry_1.insert(0, str(current)+str(num))


def add():
    num1 = entry_1.get()
    global first_num
    global operation
    first_num = float(num1)
    operation = '+'
    entry_1.delete(0,END)
    label_op1.configure(text=num1)
    label_op2.configure(text = "+")
def equals():
    num2 = entry_1.get()
    entry_1.delete(0,END)
    label_op3.configure(text = num2)
    if operation == 'addition':
        entry_1.insert(0,first_num + float(num2))
entry_1 = Entry(window, borderwidth=10,width=63,bg="pink")
entry_1.grid(row=1,column=0,columnspan=4)
#label for showing operation
label_op1 = Label(frame, text="",borderwidth=10,width=20,anchor=E)
label_op2 = Label(frame, text="",borderwidth=10,width=20)
label_op3 = Label(frame, text="",borderwidth=10,width=20,anchor=W)

label_op1.grid(row=0,column=0)
label_op2.grid(row=0,column=1)
label_op3.grid(row=0,column=2)

# number buttons
button_1 = Button(window,text="1",padx=40,pady=20,command= lambda : click(1))
button_2 = Button(window,text="2",padx=40,pady=20,command= lambda : click(2))
button_3 = Button(window,text="3",padx=40,pady=20,command= lambda : click(3))
button_4 = Button(window,text="4",padx=40,pady=20,command= lambda : click(4))
button_5 = Button(window,text="5",padx=40,pady=20,command= lambda : click(5))
button_6 = Button(window,text="6",padx=40,pady=20,command= lambda : click(6))
button_7 = Button(window,text="7",padx=40,pady=20,command= lambda : click(7))
button_8 = Button(window,text="8",padx=40,pady=20,command= lambda : click(8))
button_9 = Button(window,text="9",padx=40,pady=20,command= lambda : click(9))
button_0 = Button(window,text="0",padx=40,pady=20,command= lambda : click(0))
button_sqroot = Button(window,text="SQRT",padx=40,pady=20)
button_prd=Button(window,text=".",padx=40,pady=20)


#operation Buttons
button_add = Button(window,text="+",padx=40,pady=20,command=add)
button_subtract = Button(window,text="--",padx=40,pady=20)
button_division = Button(window,text="x",padx=40,pady=20)
button_multiplication = Button(window,text="/",padx=40,pady=20)
button_sqr = Button(window,text="^",padx=40,pady=20)
button_mode = Button(window,text="mode",padx=40,pady=20)
button_clear = Button(window,text="CLR",padx=40,pady=20)
button_equal = Button(window,text="=",padx=40,pady=20,command=equals)
#number button positions
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0)
button_prd.grid(row=5,column=1)
button_sqroot.grid(row=5,column=2)
#operation button positions
button_clear.grid(row=2,column=3)
button_sqr.grid(row=4,column=3)
button_mode.grid(row=3,column=3)

button_add.grid(row=5,column=3)
button_division.grid(row=6,column=1)
button_multiplication.grid(row=6,column=0)
button_subtract.grid(row=6,column=2)
button_equal.grid(row=6,column=3)



window.mainloop()