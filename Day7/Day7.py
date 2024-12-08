import sys
import re

class TreeNode:
	def __init__(self, value, parent):
		self.value = value
		self.parent = parent
		self.add = None
		self.mult = None
		self.concat = None
		self.canReachTarget = False

	def __repr__(self, level=0):
		ret = "  "*level+repr(self.value)+"\n"
		if self.add is not None:
			ret += self.add.__repr__(level+1)
		if self.mult is not None:
			ret += self.mult.__repr__(level+1)
		if self.concat is not None:
			ret += self.concat.__repr__(level+1)
		return ret

def canReachTarget(numbers, target, useConcat = False):
	root = TreeNode(numbers[0], None)
	generateChildNodes(numbers[1:], root, target, useConcat)
	return root.canReachTarget

def generateChildNodes(numbers, parent, target, useConcat):
	parent.add = TreeNode(parent.value + numbers[0], parent)
	parent.mult = TreeNode(parent.value * numbers[0], parent)
	if useConcat:
		parent.concat = TreeNode(int(str(parent.value) + str(numbers[0])), parent)
	if (len(numbers)) > 1:
		generateChildNodes(numbers[1:], parent.add, target, useConcat)
		generateChildNodes(numbers[1:], parent.mult, target, useConcat)
		if useConcat:
			generateChildNodes(numbers[1:], parent.concat, target, useConcat)
	elif parent.add.value == target or parent.mult.value == target or (useConcat and parent.concat.value == target):
		reverse_node = parent
		while reverse_node.parent is not None:
			reverse_node = reverse_node.parent
		reverse_node.canReachTarget = True

def solve(inputPath, useConcat):
	reachable_targets = []
	with open(inputPath) as f:
		for line in f.readlines():
			split = [int(s) for s in re.findall("(\\d+)", line)]
			if canReachTarget(split[1:], split[0], useConcat):
				reachable_targets.append(split[0])
	return sum(reachable_targets)

if __name__ == "__main__":
	inputPath = sys.argv[1]
	print(f"Part One: {solve(inputPath, False)}")
	print(f"Part Two: {solve(inputPath, True)}")