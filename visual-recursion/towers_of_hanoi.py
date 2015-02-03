#Legendary Towers of hanoi
def move_disk(n, fromPeg, toPeg):
	print("Moving disk %d from %s to %s."%(n, fromPeg, toPeg))

def towers_of_hanoi(height, fromPeg, toPeg, withPeg):
	if height >= 1:
		towers_of_hanoi(height-1, fromPeg, withPeg, toPeg)
		move_disk(height, fromPeg, toPeg)
		towers_of_hanoi(height-1, withPeg, toPeg, fromPeg)

#Keep in my mind the order of arguments given in the function call (OriginPole, DestinationPole, IntermediatePole)
#Here I am trying to move disks from Peg A to Peg C
towers_of_hanoi(4, "A", "C", "B")