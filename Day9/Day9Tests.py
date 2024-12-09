import unittest
from Day9 import getBlocks, compressBlocks, checksum

class getBlocksTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(getBlocks("12345"), ['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2'])
    def testTwo(self):
        self.assertEqual(getBlocks("2333133121414131402"), ['0','0','.','.','.','1','1','1','.','.','.','2','.','.','.','3','3','3','.','4','4','.','5','5','5','5','.','6','6','6','6','.','7','7','7','.','8','8','8','8','9','9'])

class compressBlocksTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(compressBlocks(['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2']), ['0','2','2','1','1','1','2','2','2','.','.','.','.','.','.'])
    def testTwo(self):
        self.assertEqual(compressBlocks(['0','0','.','.','.','1','1','1','.','.','.','2','.','.','.','3','3','3','.','4','4','.','5','5','5','5','.','6','6','6','6','.','7','7','7','.','8','8','8','8','9','9']), ['0','0','9','9','8','1','1','1','8','8','8','2','7','7','7','3','3','3','6','4','4','6','5','5','5','5','6','6','.','.','.','.','.','.','.','.','.','.','.','.','.','.'])

class checksumTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(checksum("0099811188827773336446555566.............."), 1928)

if __name__ == "__main__":
    unittest.main(argv=["first-arg-ignored"], buffer=True)