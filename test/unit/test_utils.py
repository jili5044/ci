import sys
import os
import unittest
import shutil
import random
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
import utils  # nopep8


class TestUtils(unittest.TestCase):

    def test_find_mean(self):
        A = [2, 2, 2, 2, 2, 2]
        mean = utils.find_mean(A)
        self.assertEqual(mean, 2)

        A = [3, 3, 3, 3]
        mean = utils.find_mean(A)
        self.assertEqual(mean, 3)
    
    
    def test_linear_search(self):
        L = random.sample(range(10, 30), 10)
        L.append(100)
        self.assertTrue(utils.linear_search(L, 100) >= 0)
        self.assertTrue(utils.linear_search(L, 200) == -1)

    def test_bindary_search(self):
        L = random.sample(range(10, 30), 10)
        L.append(100)

        L_idx = utils.index_list(L)

        self.assertTrue(utils.binary_search(L_idx, 100) >= 0)
