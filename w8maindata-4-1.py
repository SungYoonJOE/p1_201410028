﻿import turtle 
wn=turtle.Screen() 
wn.bgpic("C:\Users\P400\Desktop\myMaze.gif") 
t1=turtle.Turtle() 
t1.speed(1) 
t1.penup() 
t1.goto(-400,300) 
t1.pendown() 
t1.pencolor("Red") 
t1.right(90) 
t1.fd(400) 
t1.backward(150) 
t1.left(90) 
t1.fd(300) 
t1.left(90) 
t1.fd(300) 
t1.back(150) 
t1.right(90) 
t1.fd(300) 
t1.left(90) 
t1.right(90) 
t1.right(90) 
t1.fd(200) 
t1.fd(300) 
t1.back(100) 
t1.left(90) 
t1.fd(200) 

t1.home()
t1.clear()

def saveTracks():
    tracks=list()
    tracks.append(t1.pos)
    t1.penup() 
    t1.goto(-400,300)
    t1.pendown() 
    t1.pencolor("Red")   
    t1.right(90) 
    t1.fd(400)
    t1.backward(150) 
    t1.left(90) 
    t1.fd(300)  
    t1.left(90) 
    t1.fd(300) 
    t1.back(150) 
    t1.right(90) 
    t1.fd(300) 
    t1.left(90) 
    t1.right(90) 
    t1.right(90) 
    t1.fd(200) 
    t1.fd(300) 
    t1.back(100) 
    t1.left(90) 
    t1.fd(200) 

saveTracks()

print tracks

def lab8():
    mytracks=saveTracks()
    print mytracks
def main():
    lab8()