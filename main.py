import random
import tkinter

width = 1024
height = 768
canvas = tkinter.Canvas(bg="#202020", width=width, height=height)
canvas.pack()
q = 3
i = 0
data = []
barWidth = 50
graphX = 50
gap = (width/2 - q*barWidth) / (q+1)
barChartWidth = width/2
barChartHeight = height/2
rec = 0
text = 0
canvas.create_line(0,height/2,width, height/2, fill = "#b30047") 
canvas.create_line(width/2,0,width/2,height, fill = "#b30047")
canvas.create_line(50,0,50,height/2 - 50)
canvas.create_line(50,height/2 - 50,width/2-50,height/2 - 50)
def getData():
    global data1, data2, data3, data
    data1 = random.randrange(100)
    data2 = random.randrange(150)
    data3 = random.randrange(200)
    data = [data1, data2, data3]
    


def barChart():
    global gap, width, height, barWidth, q, data,barChartWidth,barChartHeight,rec,text
    e = barChartWidth + gap
    t = 0
    i = 0
    for i in range (q):
        if i % 3 ==0:
            canvas.create_rectangle(width/2 + 1,height/2 - 1,width,0,fill = "#202020")
            t = 0
        rec = canvas.create_rectangle(e, barChartHeight - 50,e + barWidth, barChartHeight - 50 - data[t], fill = "#b80047" )
        text = canvas.create_text(e + barWidth/2 ,barChartHeight - 40, text = data[t], font = "Arial 20", fill = "#00CC99")
        e += gap + barWidth
        t += 1
        i+=1
def graph():
    global gap, width, height, barWidth, q, data,barChartHeight,barChartWidth,graphX,graphPos1x,graphPos1y,graphPos2x,graphPos2y,i,gPos1x,gPos1y,gPos2x,gPos2y,Pos1x,Pos1y,Pos2x,Pos2y
    
    if i == 0:
        graphPos1x = [graphX]
        graphPos1y = [barChartHeight - 50 - data[0]]
        graphPos2x = [graphX+2]
        graphPos2y = [barChartHeight - 50 - data[0]+2]

        gPos1x = [graphX]
        gPos1y = [barChartHeight - 50 - data[1]]
        gPos2x = [graphX+2]
        gPos2y = [barChartHeight - 50 - data[1]+2]

        Pos1x = [graphX]
        Pos1y = [barChartHeight - 50 - data[1]]
        Pos2x = [graphX+2]
        Pos2y = [barChartHeight - 50 - data[1]+2]
    else:
        pass 


    canvas.create_oval(graphX,barChartHeight - 50 - data[0],graphX+2,barChartHeight - 50 - data[0], outline = "#b80047")
    canvas.create_oval(graphX,barChartHeight - 50 - data[1],graphX+2,barChartHeight - 50 - data[1], outline = "#00CC99")
    canvas.create_oval(graphX,barChartHeight - 50 - data[2],graphX+2,barChartHeight - 50 - data[2], outline = "white")
    graphPos1x.append(graphX)
    graphPos1y.append(barChartHeight - 50 - data[0])
    graphPos2x.append(graphX)
    graphPos2y.append(barChartHeight - 50 - data[0])
    

    gPos1x.append(graphX)
    gPos1y.append(barChartHeight - 50 - data[1])
    gPos2x.append(graphX)
    gPos2y.append(barChartHeight - 50 - data[1])

    Pos1x.append(graphX)
    Pos1y.append(barChartHeight - 50 - data[2])
    Pos2x.append(graphX)
    Pos2y.append(barChartHeight - 50 - data[2])
    
    canvas.create_line(graphPos1x[i],graphPos1y[i],graphPos1x[i+1],graphPos1y[i+1], fill = "#b80047")
    canvas.create_line(graphPos1x[i],gPos1y[i],graphPos1x[i+1],gPos1y[i+1], fill = "#00CC99")
    canvas.create_line(graphPos1x[i],Pos1y[i],graphPos1x[i+1],Pos1y[i+1], fill = "white")

    
   
    graphX += 7
    i+=1





def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#canvas.bind('<Motion>', motion)



for i in range (60):
    
    getData()
    graph()
    
    barChart()

    

canvas.update()
canvas.mainloop()
