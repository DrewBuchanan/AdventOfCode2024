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
        if (len(blocks) - i) % 1000 == 0:
            print(f"{len(blocks) - i}/{len(blocks)} blocks compressed {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        if blocks[i] == ".":
            continue
        split[i], split[split.index(".")] = split[split.index(".")], split[i]
    print(f"Blocks compressed {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return split

def compressFiles(blocks):
    # id, startIndex, length
    max_id = max(blocks)
    for i in range(int(max_id), 0, -1):
        print(f"{int(max_id) - i}/{max_id} files compressed {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        lei = 0
        si = str(i)
        while (lei < len(blocks) - 1):
            fei = blocks.index(".", lei+1)
            lei = fei
            while lei < len(blocks) - 1 and blocks[lei + 1] == ".":
                lei += 1
            if lei > blocks.index(si):
                break
            empty_block_length = lei - fei + 1
            file_length = blocks.count(si)
            if (empty_block_length >= file_length):
                blocks[blocks.index(si):blocks.index(si) + file_length], blocks[fei:fei + file_length] = blocks[fei:fei + file_length], blocks[blocks.index(si):blocks.index(si) + file_length]
                break
    return blocks

def checksum(compressed):
    checksum = 0
    for i in range(0, len(compressed)):
        if compressed[i] == ".":
            continue
        checksum += i * int(compressed[i])
    print(f"Checksum calculated {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return checksum

def main(inputPath):
    with open(inputPath) as file:
        diskmap = file.read()
        #print(f"Starting {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} with file of length {len(diskmap)}")
        #print(checksum(compressBlocks(getBlocks(diskmap))))
        print(f"Starting {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} with file of length {len(diskmap)}")
        print(checksum(compressFiles(getBlocks(diskmap))))

if __name__ == "__main__":
    inputPath = sys.argv[1]
    main(inputPath)