import sys
import datetime

def getBlocks(diskMap):
    id = 0
    blocks = []
    for i in range(0, len(diskMap)):
        if i % 2 == 0:
            for j in range(0, int(diskMap[i])):
                blocks.append(str(id))
            id += 1
        else:
            for j in range(0, int(diskMap[i])):
                blocks.append(".")
    print(f"Blocks generated {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return blocks

def compressBlocks(blocks):
    split = list(blocks)
    for i in range(len(blocks) - 1, 0, -1):
        if i % 100 == 0:
            print(f"{i}/{len(blocks)} Blocks compressed {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        if blocks[i] == ".":
            continue
        split[i], split[split.index(".")] = split[split.index(".")], split[i]
    print(f"Blocks compressed {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return split

def checksum(compressed):
    checksum = 0
    for i in range(0, compressed.index(".")):
        checksum += i * int(compressed[i])
    print(f"Checksum calculated {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return checksum

def main(inputPath):
    with open(inputPath) as file:
        diskmap = file.read()
        print(f"Starting {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} with file of length {len(diskmap)}")
        print(checksum(compressBlocks(getBlocks(diskmap))))

if __name__ == "__main__":
    inputPath = sys.argv[1]
    main(inputPath)