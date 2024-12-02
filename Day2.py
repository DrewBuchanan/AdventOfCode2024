f = open("Day2Input.txt", "r")
safe = 0
for r in f.readlines():
    levels = r.split()
    diffs=[]
    for current, nxt in zip(levels, levels[1:]):
        diffs.append(int(current) - int(nxt))
    diffs.append(all(flag > 0 for (flag) in diffs) or all(flag < 0 for (flag) in diffs))
    diffs.append(all(abs(flag) <= 3 and abs(flag) >= 1 for (flag) in diffs))
    print(str(diffs))
    if diffs[-2:] == [True, True]:
        safe += 1
print(safe)