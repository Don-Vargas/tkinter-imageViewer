from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Tarea No.3')

img1 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo1.png'))
img2 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo2.png'))
img3 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo3.png'))
img4 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo4.png'))
img5 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo5.png'))
img6 = ImageTk.PhotoImage(PIL.Image.open('img/gazapo6.png'))


img_lst = [img1,img2,img3,img4,img5,img6]

lbl = Label(root, text="hello", image=img1)
lbl.grid(row=0, column=0, columnspan=3)

def forward(img_numb):
    global lbl
    global btn_forward
    global btn_back
    
    lbl.grid_forget()
    lbl = Label(root, text="hello", image=img_lst[img_numb-1])
    btn_forward = Button(root, text='>>', command=lambda: forward(img_numb+1))
    btn_back = Button(root, text = '<<', command=lambda: back(img_numb-1))
    
    if img_numb == 5:
        btn_forward = Button(root, text='>>', state=DISABLED)

    lbl.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

def back(img_numb):
    global lbl
    global btn_forward
    global btn_back
    
    lbl.grid_forget()
    lbl = Label(root, text="hello",image=img_lst[img_numb-1])
    btn_forward = Button(root, text='>>', command=lambda:forward(img_numb+1))
    btn_back = Button(root, text = '<<', command=lambda: back(img_numb-1))
    
    if img_numb == 1:
        btn_back = Button(root, text='<<', state=DISABLED)

    lbl.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

btn_back = Button(root, text='<<', command=back, state=DISABLED)
btn_exit = Button(root, text='Exit Program', command=root.destroy)
btn_forward = Button(root, text='>>', command=lambda:forward(2))

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2)

root.mainloop()
