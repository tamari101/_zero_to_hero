from turtle import *


#we want to paint a house

#sep 1:   draw a square

speed(30)

width(9)
color("gray")
forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)
 
 #end of square

#drawing a door




forward(70)
color("black")
left(90) 
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing of a window
color("brown")
begin_fill()
pendown
goto(0,150)
right(10)
goto(50,150)

left(50)
goto(50,200)

penup
goto(0,200)
left(150)



penup
goto(200,200)
right(300)


pendown
goto(200,150)
 
color("brown")
begin_fill
penup
goto(150,150)

penup
goto(150,200)












exitonclick()
