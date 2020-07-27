import unittest
import sys
import math
import Custom_Exception as exception
# from EGH400 import Quadtree
import Quadtree as quadtree

class TestQuadtree(unittest.TestCase):


    pass 



class TestPoint(unittest.TestCase):
    def setUp(self):

        # Initial params
        identification = 1
        sequence = 1
        longitude = 1
        latitude = 1
        altitude = 1
        time = 1

        self.point = quadtree.Point(identification, sequence, longitude, latitude, altitude, time)

    # Getters

    def test_getAll(self):
        testGetAll = [1,1,1,1,1,1]
        self.assertEqual(self.point.getAll(), testGetAll)
    
    def test_getID(self):
        self.assertEqual(self.point.getID(), self.point.id)

    def test_getSequence(self):
        self.assertEqual(self.point.getSequence(), self.point.sequence)

    def test_getLong(self):
        self.assertEqual(self.point.getLong(), self.point.longitude)

    def test_getLat(self):
        self.assertEqual(self.point.getLat(), self.point.latitude)

    def test_getAlt(self):
        self.assertEqual(self.point.getAlt(), self.point.altitude)

    def test_getTime(self):
        self.assertEqual(self.point.getTime(), self.point.time)  

    # Setters

    def test_setAll(self):
        testSetAll = [1,1,1,1,1,1]      # Array of attr to set
        self.point.setAll(testSetAll)   # Set new attr
        self.assertEqual(self.point.getAll(), testSetAll)   # Use getAll() to check 
    
    def test_setID(self):
        testID = 2
        self.point.setID(testID)
        self.assertEqual(self.point.getID(), testID)

    def test_setSequence(self):
        testSequence = 2
        self.point.setSequence(testSequence)
        self.assertEqual(self.point.getSequence(), testSequence)

    def test_setLong(self):
        testLong = 2
        self.point.setLong(testLong)
        self.assertEqual(self.point.getLong(),testLong )

    def test_setLat(self):
        testLat = 2
        self.point.setLat(testLat)
        self.assertEqual(self.point.getLat(), testLat)

    def test_setAlt(self):
        testAlt = 2
        self.point.setAlt(testAlt)
        self.assertEqual(self.point.getAlt(),testAlt)

    # Add in when time is of type datetime
    # def test_setTime(self):
    #     testTime = 2
    #     self.point.setTime(testTime)
    #     self.assertEqual(self.point.getTime(), testTime)    

    # def test_typeInt(self):
    #     testList = []
    #     testInt = 1
    #     testIntMax = math.inf
    #     testIntMin = -math.inf


    #     self.assertRaises(exception.typeNotInt, self.point.setID, testList)

    #     # with self.assertRaises(exception.typeNotInt):
    #     #     self.point.setID(testList)

    #         # self.point.setID(testList)
    #     # self.assertRaises(exception.typeNotInt, self.point.setID(testInt))
    #     # self.assertRaises(exception.typeNotInt, self.point.setID(testIntMax))
    #     # self.assertRaises(exception.typeNotInt, self.point.setID(testIntMin))


        

class TestNode(unittest.TestCase):
    pass 



if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()