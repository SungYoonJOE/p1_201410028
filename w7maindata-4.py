﻿import turtle 
wn=turtle.Screen() 
#wn.bgpic("C:\Users\P400\Desktop\myMaze.gif") 
t1=turtle.Turtle() 
def saveTracks(): 
    t1.speed(1) 
    t1.penup() 
    tracks=list()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown() 
    t1.pencolor("Red") 
    t1.right(90) 
    t1.fd(400) 
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90) 
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.right(90) 
    t1.right(90) 
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90) 
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks

def replayTracks(tracks):
    for t in mytracks:
        print t

def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)
    
def main():
    lab7()