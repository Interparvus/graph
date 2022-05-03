from cmath import sin
import random
import tkinter
import math

red = "#d41186"
yellow = "#FFA500"
blue = "#00CC99"
green = "#099a37"
colors = [red,blue,yellow]
width = 1024
height = 768
canvas = tkinter.Canvas(bg="#202020", width=width, height=height)
canvas.pack()
pieCh = 0
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
spiderG = 0

canvas.create_line(0,height/2,width, height/2, fill = "#b30047") 
canvas.create_line(width/2,0,width/2,height, fill = "#b30047")
canvas.create_line(50,0,50,height/2 - 50)
canvas.create_line(50,height/2 - 50,width/2-50,height/2 - 50)
def getData():
    global data1, data2, data3, data
    data1 = random.randrange(1,100)
    data2 = random.randrange(1,100)
    data3 = random.randrange(1,100)
    data = [data1, data2, data3]
    


def barChart():
    global gap, width, height, barWidth, q, data,barChartWidth,barChartHeight,rec,text,red,colors,green
    e = barChartWidth + gap
    t = 0
    i = 0
    for i in range (q):
        if i % 3 ==0:
            canvas.create_rectangle(width/2 + 1,height/2 - 1,width,0,fill = "#202020")
            t = 0
        rec = canvas.create_rectangle(e, barChartHeight - 50,e + barWidth, barChartHeight - 50 - data[t], fill = colors[t] )
        text = canvas.create_text(e + barWidth/2 ,barChartHeight - 40, text = data[t], font = "Arial 20", fill = green)
        e += gap + barWidth
        t += 1
        i+=1
def graph():
    global gap, width, height, barWidth, q, data,barChartHeight,barChartWidth,graphX,graphPos1x,graphPos1y,graphPos2x,graphPos2y,i,gPos1x,gPos1y,gPos2x,gPos2y,Pos1x,Pos1y,Pos2x,Pos2y,red
    
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
    canvas.create_oval(graphX,barChartHeight - 50 - data[2],graphX+2,barChartHeight - 50 - data[2], outline = "#FFA500")
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
    
    canvas.create_line(graphPos1x[i],graphPos1y[i],graphPos1x[i+1],graphPos1y[i+1], fill = red)
    canvas.create_line(graphPos1x[i],gPos1y[i],graphPos1x[i+1],gPos1y[i+1], fill = "#00CC99")
    canvas.create_line(graphPos1x[i],Pos1y[i],graphPos1x[i+1],Pos1y[i+1], fill = "#FFA500")

    
   
    graphX += 7
    i+=1

def pieChart():
    global height,width,x1,x2,y1,y2,data,pieCount,pie1,pie2,pie3,red,pieCh
    x1 = width/6
    x2 = x1 + width/6
    y1 = height - 100
    y2 = height/2 + 100
    pieCount = data[0] + data[1] + data [2]
    pie1 = data[0]
    pie2 = data [1]
    pie3 = data [2]

    def prop(n):
        global height,width,x1,x2,y1,y2,data,pieCount,pie1,pie2,pie3,red,pieCh
        return 360.0 * n / 100
        
    canvas.delete(pieCh)
    pieCh = canvas.create_arc((x1,y1,x2,y2), fill=red, outline=red, start=prop(0), extent = prop(pie1/pieCount*100)), canvas.create_arc((x1,y1,x2,y2), fill="#00CC99", outline="#00CC99", start=prop(pie1/pieCount*100), extent = prop(pie2/pieCount*100)),canvas.create_arc((x1,y1,x2,y2), fill="#FFA500", outline="#FFA500", start=prop(pie2/pieCount*100+pie1/pieCount*100), extent = prop(pie3/pieCount*100))


def spiderChart():
    global red,width,height,cntPoint,side,triangleHeight,a,b,s,c,data,dataA,dataB,dataC,dataS,dataS2,K_A,K_B,K_C,spiderG
    cntPoint = width*3/4 , height*3/4
    
    s = complex(2*sin(1.047198)*100)
    
    side = s.real
    triangleHeight = 150
    dataS = side/100 * data[2]
    dataS2 = side/100 * data[1]
    a = 3/4*width,height - 100
    b = (3/4*width + side/2),height - 100 - math.sqrt(side**2 - (side/2)**2)
    c = (3/4*width - side/2),height - 100 - math.sqrt(side**2 - (side/2)**2)
    canvas.create_polygon((a, b, c), outline=red)

    K_A = 100/data[1]
    K_B = 100/data[2]
    K_C = 100/data[0]
    dataA = 3/4*width, height - 100 - (100-data[1]) 
    dataB = (3/4*width + side/2) - 75 +(75/K_B),height - 100 - math.sqrt(side**2 - (side/2)**2) +50 -(50/K_B) 
    dataC = (3/4*width - side/2) + 75 -(75/K_C),height - 100 - math.sqrt(side**2 - (side/2)**2) +50 -(50/K_C)
    canvas.delete(spiderG)
    spiderG = canvas.create_polygon((dataA, dataB, dataC), outline="white")



for i in range (60):
    
    getData()
    graph()
    pieChart()
    barChart()
    spiderChart()

canvas.update()
canvas.mainloop()
