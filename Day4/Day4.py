import sys

def main():
    inputPath = sys.argv[1]
    partOneDirections = [(0,1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    lines = []
    letters = ["X", "M", "A", "S"]
    count = 0
    row = 0
    column = 0
    doDayOne = False
    
    with open(inputPath) as file:
        for fline in file:
            lines.append(fline.strip())
    if doDayOne:
    # Part 1 Grid traversal
        while (row < len(lines)):
            column = 0
            while (column < len(lines[row])):
                if lines[row][column] == "X":
                    for i in range(0, len(partOneDirections)):
                        for j in range(1, 4):
                            withinX = column + (partOneDirections[i][0] * j) < len(lines) and column + (partOneDirections[i][0] * j) >= 0
                            if not withinX:
                                break
                            withinY = row + (partOneDirections[i][1] * j) < len(lines) and row + (partOneDirections[i][1] * j) >= 0
                            if not withinY:
                                break
                            matches = lines[row + (partOneDirections[i][1] * j)][column + (partOneDirections[i][0] * j)] == letters[j]
                            if not matches:
                                break
                            if j == 3:
                                count += 1
                column += 1
            row += 1
        print(count)

    #Part 2 Grid Traversal
    count = 0
    row = 0
    column = 0
    while (row < len(lines)):
        column = 0
        while (column < len(lines[row])):
            if lines[row][column] == "A":
                if column >= 1 and column < len(lines[row]) - 1 and row >= 1 and row < len(lines[row]) - 1:
                    try:
                        topleft = lines[row-1][column-1]
                        topright = lines[row-1][column+1]
                        bottomleft = lines[row+1][column-1]
                        bottomright = lines[row+1][column+1]
                    except:
                        print(str(column) + ", " + str(row))
                        return
                    
                    if topleft == "X" or topright == "X" or bottomleft == "X" or bottomright == "X":
                        column += 1
                        continue

                    if topleft == "A" or topright == "A" or bottomleft == "A" or bottomright == "A":
                        column += 1
                        continue

                    if (topleft == topright and bottomleft == bottomright and topleft != bottomleft) or (topleft == bottomleft and topright == bottomright and topleft != topright):
                        count += 1
            column += 1
        row += 1
    
    print(count)

if __name__ == '__main__':
    main()