# Part 1
f = open("Day1Input.txt", "r")
left = []
right = []
diff = 0
for l in f.readlines():
	n = l.split("   ")
	left.append(int(n[0]))
	right.append(int(n[1]))

left.sort()
right.sort()

for i, j in zip(left, right):
	diff += abs(i - j)

print(diff)

similarity = 0
#Part 2
for i in left:
	similarity += i * right.count(i)

print(similarity)