#!/usr/bin/python3
"""Performes unittests!"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class LetsMaxInt(unittest.TestCase):
    """Defines some unittests for func max_integer"""

    def testOrderedList(self):
            orderedL = [1, 2, 3, 69]
            self.assertEqual(max_integer(orderedL), 69)

    def testUnorderedList(self):
        unorderedL = [1, 2, 69, 4]
        self.assertEqual(max_integer(unorderedL), 69)

    def MaxPowerOne(self):
        POneL = [69, 1, 2, 3]
        self.assertEqual(max_integer(POneL), 69)

    def testEmptyList(self):
        thisBitchEmpty = []
        self.assertEqual(max_integer(thisBitchEmpty), None)

    def testOnlyOne(self):
        JustOne = [69]
        self.assertEqual(max_integer(JustOne), 69)

    def testFloats(self):
        weAllDo = [1.2, 4.5, 69.9, 5.3]
        self.assertEqual(max_integer(weAllDo), 69.9)

    def testIntsAndFloats(self):
        AllNum = [1, 4.3, 69, 69.2]
        self.assertEqual (max_integer(AllNum), 69.2)

    def testString(self):
        stupid = "I'm withz"
        self.assertEqual(max_integer(stupid), 'z')

    def testStringTuple(self):
        stupids = ["Kristopher", "Susan", "Ramlsay", "Nobelle", "Z"]
        self.assertEqual(max_integer(stupids), "Z")

    def finalTest(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
