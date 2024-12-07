import sys
from itertools import product

position = ()
directions = [(-1,0), (0,1), (1,0), (0,-1)]

def generateGrid(inputPath):
	with open(inputPath) as f:
		# Get to assume square input
		file = f.readlines()
		length = sum(1 for _ in file)
		positions_visited = []
		grid = [[0 for x in range(length + 2)] for y in range(length + 2)]
		for row in range(0, length+2):
			for column in range(0, length+2):
				if row == 0 or row == length+1:
					grid[row][column] = "*"
				elif column == 0 or column == length+1:
					grid[row][column] = "*"
				else:
					if file[row - 1][column - 1] == "^":
						position = (row, column)
						positions_visited.append((position))
					grid[row][column] = file[row - 1][column - 1]
	return grid, length, position, positions_visited

def partOne(inputPath):
	grid, length, position, positions_visited = generateGrid(inputPath)
	direction = 0
	while True:
		next_position = tuple(map(sum,zip(position, directions[direction])))
		item_at_next_position = grid[next_position[0]][next_position[1]]
		if item_at_next_position == ".":
			grid[position[0]][position[1]], grid[next_position[0]][next_position[1]] = grid[next_position[0]][next_position[1]], grid[position[0]][position[1]]
			position = next_position
			positions_visited.append(position)
		elif item_at_next_position == "*":
			break
		elif item_at_next_position == "#":
			direction = (direction + 1) % len(directions)

	print(f"{len(set(positions_visited))}")

#In theory, this should work, given infinite time, however it's slow and bad lol
def partTwo(inputPath):
	grid, length, position, positions_visited = generateGrid(inputPath)
	direction = 0
	positions_visited = [(position, direction)]
	grid[position[0]][position[1]] = "."
	loopable_locations = []
	for row in range(1, length + 1):
		for column in range(1, length + 1):
			grid, length, position, positions_visited = generateGrid(inputPath)
			direction = 0
			positions_visited = [(position, direction)]
			grid[position[0]][position[1]] = "."
			if grid[row][column] != ".":
				continue
			grid[row][column] = "O"
			while True:
				next_position = tuple(map(sum,zip(position, directions[direction])))
				item_at_next_position = grid[next_position[0]][next_position[1]]
				if item_at_next_position == "." or item_at_next_position == "|" or item_at_next_position == "-" or item_at_next_position == "+":
					if direction == 0 or direction == 2:
						if item_at_next_position == "-":
							grid[next_position[0]][next_position[1]] = "+"
						else:
							grid[next_position[0]][next_position[1]] = "|"
					else:
						if item_at_next_position == "|":
							grid[next_position[0]][next_position[1]] = "+"
						else:	
							grid[next_position[0]][next_position[1]] = "-"
					position = next_position
					if (position, direction) in positions_visited:
						loopable_locations.append((row, column))
						break
					else:
						positions_visited.append((position, direction))
				elif item_at_next_position == "*":
					break
				elif item_at_next_position == "#" or item_at_next_position == "O":
					direction = (direction + 1) % len(directions)
				else:
					print(f"{item_at_next_position} {next_position}")
	print(loopable_locations)

if __name__ == "__main__":
	inputPath = sys.argv[1]
	partOne(inputPath)
	partTwo(inputPath)