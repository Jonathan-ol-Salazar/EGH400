import unittest
import sys
# from EGH400 import Quadtree
import Quadtree

class TestQuadtree(unittest.TestCase):


    pass 



class TestPoint(unittest.TestCase):
    def setUp(self):
        identification = 1
        sequence = 1
        longitude = 1
        latitude = 1
        altitude = 1
        time = 1
        self.point = Quadtree.Point(identification, sequence, longitude, latitude, altitude, time)


    def test_init(self):
        testGetAll = [1,1,1,1,1,1]

        self.assertEqual(self.point.getAll(), testGetAll)
        

class TestNode(unittest.TestCase):
    pass 



if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()