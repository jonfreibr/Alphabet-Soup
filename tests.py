"""
    Unit tests for Alphabet Soup
"""

import unittest
import argparse
import alphasoup as s

class TestCases(unittest.TestCase):

    def get_args():
        parser = argparse.ArgumentParser(
            description='Alphabet Soup (Acronym Lookup Tool)',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('-f',
            '--file',
            help='The soup. (source spreadsheet)',
            metavar='filename',
            type=str,
            default='testdata.xlsx')
        args = parser.parse_args()
        return args
    
    args = get_args()
    al, dl, u = s.get_data(args)
    
    def test_get_data(self):
        al, dl, u = s.get_data(self.args)
        self.assertTrue(len(al)==10)
        self.assertTrue(s.filter_data('AA', dl) == ["Affirmative Action", "Allocation Advise"])
        self.assertTrue(s.filter_data('WRIST', dl) == ["Weather Radar Identification of Severe Thunderstorms"])
        self.assertTrue(s.filter_data('ZDE', dl) == ["Zero Day Exploit"])
        self.assertFalse(s.filter_data('WRIST', dl) == ["Zero Day Exploit"])
    
    def test_unique_list(self):
        self.assertTrue(s.unique_list(self.al) == ["4WD", "A", "AA", "AAD", "CDL", "FIG", "PAX", "WRIST", "WRM", "ZDE"])
        self.assertFalse(s.unique_list(self.al) == ["4WD", "A", "A", "A", "AA", "AA", "AAD", "CDL", "CDL", "CDL", "FIG", "PAX", "WRIST", "WRM", "ZDE"])
        self.assertFalse(s.unique_list(self.al) == ["Bob"])

    def test_filter_data(self):
        self.assertTrue(s.filter_data("AA", self.dl) == ["Affirmative Action", "Allocation Advise"])
        self.assertFalse(s.filter_data("AAD", self.dl) == ["Affirmative Action"])
        self.assertFalse(s.filter_data("CDL", self.dl) == ["Assistant Associate Director"])
        self.assertTrue(s.filter_data("AAD", self.dl) == ["Assistant Associate Director"])
        self.assertTrue("Commercial Drivers License" in s.filter_data("CDL", self.dl))
        self.assertTrue("War Reserve Material" in s.filter_data("WRM", self.dl))

        