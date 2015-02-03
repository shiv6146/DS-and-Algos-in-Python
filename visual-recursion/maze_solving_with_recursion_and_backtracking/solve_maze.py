#In any maze problem, 
#Move ur object horizontally by changing the col value
#Move ur object vertically by changing the row value

import turtle

PART_OF_PATH = "O"
DEAD_END = "-"
OBSTACLE = "+"
TRIED = "."

class Maze:
	def __init__(self, mazeFilename):
		rowsInMaze = 0   #temporary var used to calculate the number of rows (not an instance var of Maze class)
		columnsInMaze = 0 #temporary var used to calculate the number of cols (not an instance var of Maze class)
		self.mazeList = [] #initializing the instance variable mazeList (holds the maze file content)

		#The following block of code simply reads the maze file and populates the number of rows and cols
		mazeFile = open(mazeFilename, "r")
		for line in mazeFile:
			rowList = []   #Clears the rowlist for every line in the mazeFile
			cols = 0       #Just a counter that helps to plot the startColumn once its identified in the maze
			for ch in line:
				rowList.append(ch)
				if ch == 'S':  #Identifies the start position of the object within the maze
					self.startRow = rowsInMaze
					self.startColumn = cols
				cols += 1
			rowsInMaze += 1
			self.mazeList.append(rowList)  #Appends each and every line in the mazeFile to mazeList
			columnsInMaze = len(rowList)

		#The following block of code assigns the populated values to the instance vars
		self.rowsInMaze = rowsInMaze
		self.columnsInMaze = columnsInMaze
		self.xTranslate = -columnsInMaze/2  #A little math to calculate the box size to be drawn in the maze
		self.yTranslate = -rowsInMaze/2
		self.t = turtle.Turtle("turtle")
		self.window = turtle.Screen()

		#A bit of complex math just to make the look of the maze cleaner and better
		self.window.setworldcoordinates(-(columnsInMaze)/2-0.5, -(rowsInMaze)/2-0.5, rowsInMaze/2+0.5, columnsInMaze/2+0.5)

	#This instance method renders the maze to the screen
	def draw_maze(self):
		self.t.speed(10)
		for x in range(self.rowsInMaze):
			for y in range(self.columnsInMaze):
				if self.mazeList[x][y] == OBSTACLE:
					self.draw_centered_box(x+self.xTranslate, -y-(self.yTranslate-7), "orange")
		self.t.color("black")
		self.t.fillcolor("blue")

	#This instance method renders the individual boxes inside the maze
	def draw_centered_box(self, x, y, color):
		self.t.penup()
		self.t.goto(x-0.5, y-0.5)
		self.t.color(color)
		self.t.fillcolor(color)
		self.t.setheading(90)
		self.t.pendown()
		self.t.begin_fill()
		for i in range(4):
			self.t.forward(1)
			self.t.right(90)
		self.t.end_fill()

	#This instance method moves the turtle within the maze
	def move_turtle(self, x, y):
		self.t.penup()
		#the next line makes the head of the turtle point towards the direction its about to take next
		self.t.setheading(self.t.towards(x+self.xTranslate, -y+self.yTranslate))
		self.t.goto(x+self.xTranslate, -y+self.yTranslate)

	#This instance method keeps track of the paths visited by the turtle by rendering a black dot within the maze
	def keep_track(self, color):
		self.t.dot(10, color)

	#This instance method updates the position of the turtle within the maze by changing the mazeList elements
	def update_position(self, row, col, val=None):
		if val:
			self.mazeList[row][col] = val
		self.move_turtle(col, row)

		#The following block of code is just to differentiate between the paths taken by the turtle on screen
		if val == PART_OF_PATH:
			color = "green"
		elif val == OBSTACLE:
			color = "red"
		elif val == TRIED:
			color = "black"
		elif val == DEAD_END:
			color = "red"
		else:
			color = None

		if color:
			self.keep_track(color)

	#This instance method checks for the exit out of the maze
	def is_exit(self, row, col):
		return ( row == 0 or row == self.rowsInMaze-1 or col == 0 or col == self.columnsInMaze-1 )

	#This is to overload the [] operator so that we could use the instance of the Maze class to access the elements of mazeList
	def __getitem__(self, index):
		return self.mazeList[index]

###################################################################################################################################################################################################

def search_maze(maze, startRow, startColumn):
	# try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return False
    maze.update_position(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
    	return False

    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn]:
    	return False

    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(startRow, startColumn):
    	maze.update_position(startRow, startColumn, PART_OF_PATH)
    	return True
    maze.update_position(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = search_maze(maze, startRow-1, startColumn) or search_maze(maze, startRow+1, startColumn) or search_maze(maze, startRow, startColumn-1) or search_maze(maze, startRow, startColumn+1)

    if found:
    	maze.update_position(startRow, startColumn, PART_OF_PATH)
    else:
    	maze.update_position(startRow, startColumn, DEAD_END)

    return found

##################################################################################################################################################################################################

mazeObj = Maze("maze2.txt")
mazeObj.draw_maze()
#mazeObj.update_position(mazeObj.startRow, mazeObj.startColumn)

#search_maze(mazeObj, mazeObj.startRow, mazeObj.startColumn)
#mazeObj.window.exitonclick()