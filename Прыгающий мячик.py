import turtle
window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)
ball = turtle.Turtle()
ball.shape('circle')
ball.up()
dx=6
dy=5
while True:
	x,y = ball.position()
	if x+dx>=300 or x+dx <= -300:
		dx= -dx
	if y+dy>=300 or y+dy <= -300:
		dy= -dy
	ball.goto(x+dx,y+dy)
	
window.mainloop()
