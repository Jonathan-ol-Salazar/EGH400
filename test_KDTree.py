import unittest
import sys
import math

import KDTree as kdtree

class TestKDTree(unittest.TestCase):
    def setUp(self):

        # Initial params
        longitude1 = 0
        latitude1 = 0
        longitude2 = 10
        latitude2 = 10
        fanout = 2

        self.kdtree = kdtree.KDTree()