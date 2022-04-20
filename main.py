from tkinter import*

window = Tk()


entry_box = Entry(window,bg='pink',fg='green',width=35,borderwidth=15)


def click(num):
    current_num = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0, str(current_num)+str(num))

def add():
    num1 = entry_box.get()
    global first_num
    global operation
    first_num = float(num1)
    operation = 'addition'
    entry_box.delete(0,END)

def minus():
    num1 = entry_box.get()
    global first_num
    global operation
    first_num = float(num1)
    operation = 'subtraction'
    entry_box.delete

def equal():
    num2 = entry_box.get()
    entry_box.delete(0,END)

    if operation == 'addition':
        entry_box.insert(0,first_num + float(num2))




button_1=Button(window,text='1',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('1'))
button_2=Button(window,text='2',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('2'))
button_3=Button(window,text='3',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('3'))
button_4=Button(window,text='4',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('4'))
button_5=Button(window,text='5',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('5'))
button_6=Button(window,text='6',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('6'))
button_7=Button(window,text='7',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('7'))
button_8=Button(window,text='8',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('8'))
button_9=Button(window,text='9',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('9'))
button_0=Button(window,text='0',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('0'))
button_period=Button(window,text='.',padx=30,pady=20,bg='green',fg='pink',command=lambda :click('.'))

button_add =Button(window,text='+',padx=30,pady=20,bg='green',fg='pink',command=add)
button_equal =Button(window,text='=',padx=30,pady=20,bg='green',fg='pink',command=equal)

entry_box.grid(row=0,column=0,columnspan=3)
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=1)

button_period.grid(row=4,column=0)
button_add.grid(row=4,column=2)
button_equal.grid(row=4,column=1)

window.mainloop()