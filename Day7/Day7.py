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
	generateChildNodes(numbers[1:], root)
	if traverse(root, target, useConcat):
		return True
	else:
		return False

def traverse(node, target, useConcat):
	if node is None:
		return None
	if node.value > target:
		return None
	if node.value == target and node.add is None and node.mult is None and (not useConcat or node.concat is None):
		return node
	else:
		found_node = traverse(node.add, target, useConcat)
		if found_node is None:
			found_node = traverse(node.mult, target, useConcat)
		if found_node is None and useConcat:
			found_node = traverse(node.concat, target, useConcat)
		return found_node

def generateChildNodes(numbers, parent):
	parent.add = TreeNode(parent.value + numbers[0], parent)
	if (len(numbers)) > 1:
		generateChildNodes(numbers[1:], parent.add)
	parent.mult = TreeNode(parent.value * numbers[0], parent)
	if (len(numbers)) > 1:
		generateChildNodes(numbers[1:], parent.mult)
	parent.concat = TreeNode(int(str(parent.value) + str(numbers[0])), parent)
	if (len(numbers)) > 1:
		generateChildNodes(numbers[1:], parent.concat)

def partOne(inputPath):
	reachable_targets = []
	with open(inputPath) as f:
		for line in f.readlines():
			split = [int(s) for s in re.findall("(\\d+)", line)]
			if canReachTarget(split[1:], split[0]):
				reachable_targets.append(split[0])
	print(f"{sum(reachable_targets)}")

def partTwo(inputPath):
	reachable_targets = []
	with open(inputPath) as f:
		for line in f.readlines():
			split = [int(s) for s in re.findall("(\\d+)", line)]
			if canReachTarget(split[1:], split[0], True):
				reachable_targets.append(split[0])
	print(f"{sum(reachable_targets)}")

if __name__ == "__main__":
	inputPath = sys.argv[1]
	partOne(inputPath)
	partTwo(inputPath)