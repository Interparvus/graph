import random
import tkinter
width = 1024
height = 768
canvas = tkinter.Canvas(bg="#333399", width=width, height=height)
canvas.pack()
data = []
gap = 0
canvas.create_line(0,height/2,width, height/2)
canvas.create_line(width/2,0,width/2,height)
def getData():
    global data1, data2, data3, data
    data1 = random.randrange()
    data2 = random.randrange()
    data3 = random.randrange()
    data = [data1, data2, data3]


def barChart():
    global gap, data, width, height
    gap = 0


















canvas.mainloop()