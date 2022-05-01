import random
import tkinter
width = 1024
height = 768
canvas = tkinter.Canvas(bg="#202020", width=width, height=height)
canvas.pack()
q = 3
data = []
barWidth = 50
gap = (width/2 - q*barWidth) / (q+1)
barChartWidth = width/2
barChartHeight = height/2
canvas.create_line(0,height/2,width, height/2, fill = "#b30047") 
canvas.create_line(width/2,0,width/2,height, fill = "#b30047")
def getData():
    global data1, data2, data3, data
    data1 = random.randrange(100)
    data2 = random.randrange(150)
    data3 = random.randrange(200)
    data = [data1, data2, data3]



def barChart():
    global gap, width, height, barWidth, q, data,barChartWidth,barChartHeight
    e = barChartWidth + gap
    t = 0
    for i in range (q):
        canvas.create_rectangle(e, barChartHeight - 50,e + barWidth, barChartHeight - 50 - data[t], fill = "#b80047" )
        canvas.create_text(e + barWidth/2 ,barChartHeight - 40, text = data[t], font = "Arial 20", fill = "#00CC99")
        e += gap + barWidth
        t += 1














#print (gap)

getData()
barChart()
print (data)
canvas.mainloop()