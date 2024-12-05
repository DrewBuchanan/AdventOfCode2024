import sys
import re

def main():
    inputPath = sys.argv[1]
    rules = []
    updates = []
    rulesfinished = False
    with open(inputPath) as f:
        for line in f.readlines():
            if rulesfinished:
                updates.append(line.strip())
            elif line.strip() == "":
                rulesfinished = True
            else:
                rules.append(line.strip())

    incorrect_updates = []
    correct_updates = []
    rule_failed = False
    for i in range(0, len(updates)):
        for j in range(0, len(rules)):
            pages = rules[j].split("|")
            if pages[0] in updates[i] and pages[1] in updates[i]:
                regex = f"({pages[0]}).+({pages[1]})"
                findall = re.findall(regex, updates[i])
                if len(findall) <= 0:
                    incorrect_updates.append(updates[i])
                    rule_failed = True
                    break
        if rule_failed:
            rule_failed = False
        else:
            correct_updates.append(updates[i])

    sum = 0
    for i in range(0, len(correct_updates)):
        split = correct_updates[i].split(",")
        sum += int(split[int(len(split) / 2)])

    print(f"Sum of mid item of valid rules {sum}")
    print()

    sum = 0
    i = 0
    while i < len(incorrect_updates):
        modified_rule = False
        j = 0
        while j < len(rules):
            pages = rules[j].split("|")
            if pages[0] in incorrect_updates[i] and pages[1] in incorrect_updates[i]:
                regex = f"({pages[0]}).+({pages[1]})"
                findall = re.findall(regex, incorrect_updates[i])
                if len(findall) <= 0:
                    incorrect_updates[i] = pages[0].join(part.replace(pages[0], pages[1]) for part in incorrect_updates[i].split(pages[1]))
                    modified_rule = True
                    break
            j += 1
        if not modified_rule:
            split = incorrect_updates[i].split(",")
            sum += int(split[int(len(split) / 2)])
            i += 1
            print()

    print()
    print(f"Sum of formerly invalid rules {sum}")

if __name__ == '__main__':
    main()