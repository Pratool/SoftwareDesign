# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def split_dictionary(D):
    the_dic1 = {x : D[x] for x in D if x[0].isupper()}
    the_dic2 = {x : D[x] for x in D if x[0].islower()}
    
    return [the_dic1, the_dic2]

class SplitDictionaryTests(unittest.TestCase):
    def test_split_dictionary_basic(self):
        self.assertEqual(split_dictionary({'a':2,'B':'hello','c':'t'}), [{'B': 'hello'}, {'a':  2, 'c':  't'}])

if __name__ == '__main__':
    unittest.main()