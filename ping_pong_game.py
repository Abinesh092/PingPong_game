# Ping Pong Game using Turtle Module
# Run this program using: python code.py
from turtle import *
import time as ts
#get_input_from_user

# screen
s=Screen()
s.setup(800,600)
s.bgcolor("green")
s.tracer(0)
# get_input_from_user
p1=s.textinput("player1's Name","number not allowed")
p2=s.textinput("player2's Name","number not allowed")
wp=s.numinput("winning points","string not allowed",10,5,60)
# left_pade
ls=Turtle()
ls.penup()
ls.goto(-390,0)
ls.pendown()
ls.color("white")
ls.shape("square")
ls.shapesize(5,1)
# right_pade
rs=Turtle()
rs.penup()
rs.goto(380,0)
rs.pendown()
rs.color("white")
rs.shape("square")
rs.shapesize(5,1)
#moveleft_pade
def up():
        ls.penup()
        ls.sety(ls.ycor()+20)
        
def down():
        ls.penup()
        ls.sety(ls.ycor()-20)
def rup():
        rs.penup()
        rs.sety(rs.ycor()+20)
def rdown():
        rs.penup()
        rs.sety(rs.ycor()-20)
s.listen()
s.onkeypress(up,"w")
s.onkeypress(down,"s")
s.onkeypress(rup,"o")
s.onkeypress(rdown,"l")

#ball
b=Turtle()
b.color("white")
b.shape("circle")
b.dx=0.50
b.dy=0.50
#title
t=Turtle()
t.penup()
t.goto (0,270)
t.ht()
pm1=0
pm2=0
l=1
ll=[50,40,30,20,15,10,5]
t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
while True :
        s.update()
        b.penup()
        b.sety(b.ycor()+b.dy)
        b.setx(b.xcor()+b.dx)
        if b.ycor()>= 290.0: #upside
                b.dy*=-1
        if b.ycor()<=-280.0:#downside
                b.dy*=-1
        if b.xcor()>=380.0: #rightside
            b.setx(375)
            b.setx(b.xcor()+b.dx)
            b.dx*=-1
            s.bgcolor("red")
            pm1+=1
            t.clear()
            t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
        if b.xcor()<=-390.0: #leftside
                b.setx(-385)
                b.dx*=-1
                s.bgcolor("red")
                pm2+=1
                t.clear()
                t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
        if b.xcor() >=370.0 and b.ycor ()<= rs.ycor()+48.0 and b.ycor()>=rs.ycor()-48.0: # right_pad
                b.setx(360)
                b.dx*=-1
                s.bgcolor("green")
                t.clear()
                t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
                if pm1 in ll or pm2 in ll:
                    l+=1
                    t.clear()
                    t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
                    b.dx+=0.45
                    b.dy+=0.45
                    ll.pop()
        if b.xcor() <=-380 and b.ycor()<= ls.ycor()+48.0 and b.ycor()>=ls.ycor()-48.0: #left_pad
                b.setx(-375)
                b.dx*=-1
                s.bgcolor("green")
                t.clear()
                t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
                if pm1 in ll or pm2 in ll:
                    l+=1
                    t.clear()
                    t.write(p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
                    b.dx+=0.45
                    b.dy+=0.45
                    ll.pop()
        if pm1==wp or pm2==wp:
                s.clear()
                t.home()
                t.write("game over "+p1+" "+str(pm1)+" "+p2+" "+str(pm2)+" your level "+str(l),align="center",font=("ariel",24,"normal"))
                ts.sleep(5)
                s.bye()
