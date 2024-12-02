import sys

def toInt(x):
    return int(x)

def all_ascending(report):
    for i in range(1, len(report)):
        if report[i - 1] >= report[i]:
            return False
    return True

def all_descending(report):
    for i in range(1, len(report)):
        if report[i - 1] <= report[i]:
            return False
    return True

def changes_in_range(report):
    for i in range(1, len(report)):
        if abs(report[i-1] - report[i]) > 3:
            return False
    return True

def is_safe(report):
    return (all_ascending(report) or all_descending(report)) and changes_in_range(report)

def is_safe_with_dampen(report):
    dampened = False
    i = 0
    while not dampened:
        test_report = report.copy()
        test_report.pop(i)
        if is_safe(test_report):
            return True
        i += 1
        if (i == len(report)):
            dampened = True
    return False

def main():
    inputPath = sys.argv[1]
    reports = []
    unsafe_reports = []
    safe = 0
    with open(inputPath) as f:
        for line in f:
            report = line.split()
            report = list(map(toInt, report))
            reports.append(report)

    for report in reports:
        if is_safe(report):
            safe += 1
        else:
            unsafe_reports.append(report)
    
    print("Undampened: " + str(safe))

    for report in unsafe_reports:
        if is_safe_with_dampen(report):
            safe += 1

    print("Dampened: " + str(safe))
    
if __name__ == '__main__':
    main()