import turtle

t = turtle.Turtle()
s = turtle.Screen()

def draw_spiral(turtleObj, length):
	if length > 0:	#Everytime I keep on missing the base case of the recursion(Exit condition)
		turtleObj.forward(length)
		turtleObj.right(90)
		draw_spiral(turtleObj, length - 5)

draw_spiral(t, 100)
s.exitonclick()