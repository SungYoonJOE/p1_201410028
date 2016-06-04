import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def keyup():
    t1.forward(10)
def keydown():
    t1.back(10)
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

wn.listen()
turtle.mainloop()

t1.shape("circle")
t1.pencolor("Green")

def goalone(pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(40)
        t1.right(90)
        
def goaltwo(pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,3):
        t1.fd(30)
        t1.right(120)
        
def goalthree(pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    t1.circle(20)

goalthree((450.0))
goaltwo((400,0))
goalone((320,0))

def PushPush(distance):
	sum=0
	distance=raw_input('거리를 입력하세요(0~700)')
	marks=float(distance)
	if marks>=480:
		print "FAIL"
	elif marks>=430 and marks<480:
		print "You got 300points!"
	elif marks>=370 and marks<430:
		print "You got 200points!"
	elif marks>=280 and marks<370:
		print "You got 100points!"
	else marks<280:
		print "FAIL"
    sum+=marks

PushPush()