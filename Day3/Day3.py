import re

#Part 1
text = open("Day3Input.txt", "r").read()
x = re.findall("mul\\((\\d+),(\\d+)\\)", text)
sum = 0
for i in x:
    sum += int(i[0]) * int(i[1])
print(sum)

#Part 2
sum = 0
muls = list(re.finditer("mul\\((\\d+),(\\d+)\\)", text))
donts = list(re.finditer("don't\\(\\)", text))
dos = list(re.finditer("do\\(\\)", text))

matches = sorted(muls + donts + dos, key=lambda x: x.start())
enabled = True
for match in matches:
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    else:
        if enabled:
            first, second = match.groups()
            sum += int(first) * int(second)
print(sum)