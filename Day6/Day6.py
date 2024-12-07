import sys
from itertools import product

def main():
	inputPath = sys.argv[1]
	directions = [(-1,0), (0,1), (1,0), (0,-1)]
	direction = 0
	with open(inputPath) as f:
		# Get to assume square input
		file = f.readlines()
		length = sum(1 for _ in file)
		grid = [[0 for x in range(length + 2)] for y in range(length + 2)]
		position = ()
		positions_visited = []
		for row in range(0, length+2):
			for column in range(0, length+2):
				if row == 0 or row == length+1:
					grid[row][column] = "*"
				elif column == 0 or column == length+1:
					grid[row][column] = "*"
				else:
					if file[row - 1][column - 1] == "^":
						position = (row, column)
						positions_visited.append(position)
					grid[row][column] = file[row - 1][column - 1]

	while position[0] != 0 and position[0] != length + 2 and position[1] != 0 and position[1] != length + 2:
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

if __name__ == "__main__":
	main()