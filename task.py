from tkinter import *
import random
def linFun(k,x,b):
    return k*x+b
def drawFunc():
    global SCREEN_WIDTH, SCREEN_HEIGHT
    k = int(entryK.get())
    b = int(entryB.get())
    for x in range(-1000,1000):
        can.create_rectangle(SCREEN_WIDTH/2 -x,
                        -SCREEN_HEIGHT/2 - linFun(k,x,b),
                        SCREEN_WIDTH/2 - x+1,
                        -SCREEN_HEIGHT / 2 -linFun(k, x, b)+1, fill = "#ff0000")
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
window = Tk()
window.geometry(str(SCREEN_WIDTH)+'x'+str(SCREEN_HEIGHT)+'+100+100')
window.title("Мое первое окно!")
label1 = Label(window, text="Впишите\n уравнение", font=('Courier', 24))
label1.grid(row=0,column=0)
label2 = Label(window, text="y =", font=('Courier', 28))
label2.grid(row=0,column=1)
entryK = Entry(window,width=8,font=('Courier', 28))
entryK.grid(row=0,column=2)
label3 = Label(window, text="x+", font=('Courier', 28))
label3.grid(row=0,column=3)
entryB = Entry(window,width=8,font=('Courier', 28))
entryB.grid(row=0,column=4)
but1 = Button(window,text = "нарисовать",font=('Courier', 28), command = drawFunc)
but1.grid(row=0,column=5)
can = Canvas(window, width = SCREEN_WIDTH, height = SCREEN_HEIGHT-100)
can.grid(row=1,column=0,columnspan = 6)
for i in range(0,SCREEN_WIDTH,50):
    can.create_line(i, 0, i, SCREEN_HEIGHT)
    can.create_line(0, i, SCREEN_WIDTH, i)
can.create_line(SCREEN_WIDTH/2,0,SCREEN_WIDTH/2,SCREEN_HEIGHT,width=5)
can.create_line(0,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT/2,width=5)
window.mainloop()