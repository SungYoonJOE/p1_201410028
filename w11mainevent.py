import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def Line(size,at):
    t1.penup()
    t1.setpos(at)
    t1.pendown()
    t1.forward(size)

def keyup():
    t1.forward(50)

def keydown():
    t1.back(50)

def keyright():
    t1.right(90)

def keyleft():
    t1.left(90)

def mousegoto(x,y):
    t1.setpos(x,y)

def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
    wn.onkey(wn.bye,"q")

def addMouse():
    wn.onclick(mousegoto)

def lab11():
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

lab11()
Line(400,(200,200))