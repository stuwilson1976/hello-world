from tkinter import *

root = Tk()
root.title('Firewall Rule')
root.geometry('800x300')

label1 = Label(root, text='Create Firewall Rules')
label1.grid()

protocol = Entry(root, width=10)
protocol.grid(column=1, row=1)
from_port = Entry(root, width=10)
from_port.grid(column=2, row=1)
to_port = Entry(root, width=10)
to_port.grid(column=3, row=1)
src_sn = Entry(root, width=10)
src_sn.grid(column=4, row=1)


def clicked():
    res = 'You entered: ' + protocol.get() + ' ' + from_port.get() + '-' + to_port.get() + ' ' + src_sn.get()
    label1.configure(text=res)


button1 = Button(root, text='Generate rule', fg='red', command=clicked)

button1.grid(column=1, row=2)

root.mainloop()
