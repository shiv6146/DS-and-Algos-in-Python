import turtle

def draw_triangle(turtleObj, points, color):
	turtleObj.fillcolor(color)
	turtleObj.penup()
	turtleObj.goto(points[0][0],points[0][1])
	turtleObj.pendown()
	turtleObj.begin_fill()
	turtleObj.goto(points[1][0], points[1][1])
	turtleObj.goto(points[2][0], points[2][1])
	turtleObj.goto(points[0][0], points[0][1])
	turtleObj.end_fill()

def get_mid(p1, p2):
	return ( (p1[0]+p2[0])/2, (p1[1]+p2[1])/2 )

def sierpinski(turtleObj, points, degree):
	colormap = ["orange", "red", "blue", "green", "yellow", "violet", "white"]
	draw_triangle(turtleObj, points, colormap[degree])

	#this time am not gonna miss u buddy(Base case of recursion)
	if degree > 0:
		sierpinski(turtleObj, [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree-1) #left triangles recursive call
		sierpinski(turtleObj, [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree-1) #top triangles recursive call
		sierpinski(turtleObj, [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree-1) #right triangles recursive call


t = turtle.Turtle()
s = turtle.Screen()
points = [[-100,-50], [0, 100], [100, -50]]
sierpinski(t, points, 3)
s.exitonclick()