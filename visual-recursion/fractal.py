import turtle

def draw_tree(turtleObj, branchLength):
	#Base case of recursion(Exit condition)
	if branchLength > 5:
		turtleObj.forward(branchLength)
		turtleObj.right(20)
		draw_tree(turtleObj, branchLength - 15)
		turtleObj.left(40)
		draw_tree(turtleObj, branchLength - 15)
		turtleObj.right(20)
		turtleObj.backward(branchLength)

t = turtle.Turtle()
s = turtle.Screen()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.color("green")
draw_tree(t, 75)
s.exitonclick()
