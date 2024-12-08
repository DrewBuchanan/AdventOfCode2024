import sys
from itertools import combinations
import unittest

class TestMain(unittest.TestCase):
    def testOne(self):
        self.assertEqual(main("TestInputs/Day8TestInput1.txt"), 2)
    def testTwo(self):
        self.assertEqual(main("TestInputs/Day8TestInput2.txt"), 4)
    def testThree(self):
        self.assertEqual(main("TestInputs/Day8TestInput3.txt"), 4)
    def testFour(self):
        self.assertEqual(main("TestInputs/Day8TestInput4.txt"), 14)
    def testFive(self):
        self.assertEqual(main("Inputs/Day8Input.txt"), 228)
    def testSix(self):
        self.assertEqual(main("TestInputs/Day8TestInput5.txt", True), 9)
    def testSeven(self):
        self.assertEqual(main("TestInputs/Day8TestInput4.txt", True), 34)
    def testEight(self):
        self.assertEqual(main("Inputs/Day8Input.txt", True), 766)

def main(inputPath, p2=False):
    antennas = {}
    grid = []

    with open(inputPath) as f:
        lines = f.readlines()
        rows = len(lines)
        columns = len(lines[0].strip())
        for r in range(0, rows):
            row = list(lines[r].strip())
            grid.append(row)
            for c in range(0, columns):
                if row[c] != ".":
                    if row[c] not in antennas:
                        antennas[row[c]] = []
                    antennas[row[c]].append((r,c))
                        
    for key, value in antennas.items():
        print(key, ": ", value)

    anti_nodes = []

    for key, value in antennas.items():
        if p2:
            for antenna in value:
                anti_nodes.append(antenna)
        combos = list(combinations(value, 2))
        print(combos)
        for combo in combos:
            dx = combo[1][1] - combo[0][1]
            dy = combo[1][0] - combo[0][0]

            i = 1
            while inBounds((combo[1][0] + (dy * i), combo[1][1] + (dx * i)), rows, columns):
                anti_nodes.append((combo[1][0] + (dy * i), combo[1][1] + (dx * i)))
                grid[combo[1][0] + (dy * i)][combo[1][1] + (dx * i)] = "#"
                if not p2:
                    break
                i += 1

            i = 1
            while inBounds((combo[0][0] - (dy * i), combo[0][1] - (dx * i)), rows, columns):
                anti_nodes.append((combo[0][0] - (dy * i), combo[0][1] - (dx * i)))
                grid[combo[0][0] - (dy * i)][combo[0][1] - (dx * i)] = "#"
                if not p2:
                    break
                i += 1

    for row in grid:
        print("".join(row))

    return len(set(anti_nodes))

def inBounds(position, rows, columns):
    return 0 <= position[0] < rows and 0 <= position[1] < columns

if __name__ == "__main__":
    unittest.main(argv=["first-arg-ignored"], buffer=True)
    inputPath = sys.argv[1]