"""
    Unit tests for Alphabet Soup
"""

import unittest
import alphasoup as s

class TestCases(unittest.TestCase):

    testList = ["Joe", "Bill", "Larry", "Joe", "Fred", "Bill"]
    aList = ["AAA", "BBB", "CCC"]
    dList = [["AAA", "a.a.a"], ["AAA", "A.A.A"], ["AAA", "Alpha Apple Angry"], ["BBB", "Big Boy Bob"], ["CCC", "Cool Cat Charlie"], ["CCC", "Crazy Coot Curly"]]
    
    def test_unique_list(self):
        self.assertTrue(s.unique_list(self.testList) == ["Joe", "Bill", "Larry", "Fred"])
        self.assertFalse(s.unique_list(self.testList) == ["Bob"])

    def test_filter_data(self):
        self.assertTrue(s.filter_data("AAA", self.dList) == ["a.a.a", "A.A.A", "Alpha Apple Angry"])
        self.assertFalse(s.filter_data("BBB", self.dList) == ["a.a.a", "A.A.A", "Alpha Apple Angry"])
        self.assertFalse(s.filter_data("CCC", self.dList) == ["Crazy Coot Curly"])
        self.assertTrue(s.filter_data("BBB", self.dList) == ["Big Boy Bob"])
        self.assertTrue("Crazy Coot Curly" in s.filter_data("CCC", self.dList))
        self.assertTrue("Big Boy Bob" in s.filter_data("BBB", self.dList))
        