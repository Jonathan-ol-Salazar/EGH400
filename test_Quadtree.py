import unittest
import sys
import math
import Custom_Exception as exception
# from EGH400 import Quadtree
import Quadtree as quadtree

class TestQuadtree(unittest.TestCase):
    def setUp(self):

        # Initial params
        longitude1 = 0
        latitude1 = 0
        longitude2 = 10
        latitude2 = 10
        maxPoints = 1


        self.quadtree = quadtree.Quadtree(latitude1, longitude1, latitude2, longitude2, maxPoints)
        self.quadtree.root.purgeChildren()
        self.quadtree.root.purgePoints()


    def test_Insert(self):


        # Root Level 
        point1 = quadtree.Point(1,1,1,1,1,1)
        self.quadtree.Insert(point1)

        self.assertEqual(self.quadtree.root.points[point1.getKey()][0].getAll(), point1.getAll())
        self.assertEqual(len(self.quadtree.root.getChildren()), 0)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 1)      # Single point
        self.assertEqual(self.quadtree.root.getParent(), None)


        # Existing Point
        point2 = quadtree.Point(1,1,1,1,1,1)
        self.quadtree.Insert(point2)

        self.assertEqual(len(self.quadtree.root.getChildren()), 0)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 1)      # Single point
        self.assertEqual(self.quadtree.root.getParent(), None)


        # New level
        point2 = quadtree.Point(1,2,1,2,2,3)
        self.quadtree.Insert(point2)

        self.assertEqual(len(self.quadtree.root.getChildren()), 4)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 0)      # No points
        self.assertEqual(self.quadtree.Query(point1), point1)
        self.assertEqual(self.quadtree.Query(point2), point2)


        # Existing point varying levels
        point2 = quadtree.Point(1,2,5,3,2,3)
        self.quadtree.Insert(point2)
        self.assertEqual(self.quadtree.Query(point2), point2)

        point3 = quadtree.Point(1,2,4,4,2,3)
        self.quadtree.Insert(point3)
        self.assertEqual(self.quadtree.Query(point3), point3)

        point4 = quadtree.Point(1,2,3,5,2,3)
        self.quadtree.Insert(point4)
        self.assertEqual(self.quadtree.Query(point4), point4)

        point5 = quadtree.Point(1,2,2,6,2,3)
        self.quadtree.Insert(point5)
        self.assertEqual(self.quadtree.Query(point5), point5)

        point6 = quadtree.Point(1,2,1,7,2,3)
        self.quadtree.Insert(point6)
        self.assertEqual(self.quadtree.Query(point6), point6)



    def test_Update(self):
        # Non-existant
        # Root Level 
        # Single Level
        # Each Quadrant
        pass

    def test_Delete(self):
        # Non-existant
        point1 = quadtree.Point(1,1,1,1,1,1)
        self.assertEqual(self.quadtree.Delete(point1), 0)
        self.assertEqual(len(self.quadtree.root.getChildren()), 0)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 0)      # No point

        # Existing point at root level
        self.quadtree.Insert(point1)
        self.assertEqual(self.quadtree.Delete(point1), 1)

        # Multilevel
        point2 = quadtree.Point(1,2,1,2,2,3)
        self.quadtree.Insert(point2)
        self.assertEqual(len(self.quadtree.root.getChildren()), 0)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 1)      # Single point
        
        point3 = quadtree.Point(1,3,4,2,2,3)
        self.quadtree.Insert(point3)
        point4 = quadtree.Point(1,4,2,2,2,3)
        self.quadtree.Insert(point4)
        self.assertEqual(len(self.quadtree.root.getChildren()), 4)    # 4 children
        self.assertEqual(len(self.quadtree.root.getPoints()), 0)      # No point

        self.assertEqual(self.quadtree.Delete(point2), 1)
        self.assertEqual(self.quadtree.Delete(point3), 1)
        self.assertEqual(self.quadtree.Delete(point4), 1)
        self.assertEqual(len(self.quadtree.root.getChildren()), 0)    # No children
        self.assertEqual(len(self.quadtree.root.getPoints()), 0)      # No point
        
        # Each Quadrant
        point1 = quadtree.Point(1,1,1,9,2,3)    # Quadrant One
        point2 = quadtree.Point(1,2,8,9,2,3)    # Quadrant Two
        point3 = quadtree.Point(1,3,1,4,2,3)    # Quadrant Three
        point4 = quadtree.Point(1,4,8,4,2,3)    # Quadrant Four
        
        # Inserting points into each quadrant
        self.quadtree.Insert(point1)
        self.quadtree.Insert(point2)
        self.quadtree.Insert(point3)
        self.quadtree.Insert(point4)

        self.assertEqual(len(self.quadtree.root.getChildren()), 4 )  # Four children
        
        # Deleting all the points
        self.assertEqual(self.quadtree.Delete(point1), 1)  
        self.assertEqual(self.quadtree.Delete(point2), 1)
        self.assertEqual(self.quadtree.Delete(point3), 1)
        self.assertEqual(self.quadtree.Delete(point4), 1)

        self.assertEqual(len(self.quadtree.root.getChildren()), 0 )  # Four children



    def test_Query(self):
        # Non-existant
        point1 = quadtree.Point(1,1,1,1,1,1)
        
        self.assertEqual(self.quadtree.Query(point1), None)
        

        # ROOT LEVEL 
        self.quadtree.Insert(point1)        
        self.assertEqual(self.quadtree.Query(point1), point1)

        # SINGLE LEVEL
        
        # New point at existing location
        point2 = quadtree.Point(1,1,1,1,1,2)
        self.quadtree.Insert(point2)    
        self.assertEqual(self.quadtree.Query(point1), point1)
        self.assertEqual(self.quadtree.Query(point2), point2)

        point3 = quadtree.Point(1,2,1,2,1,1)
        self.quadtree.Insert(point3)    
        self.assertEqual(self.quadtree.Query(point1), point1)
        self.assertEqual(self.quadtree.Query(point2), point2)
        self.assertEqual(self.quadtree.Query(point3), point3)



        # EACH QUADRANT
        point1 = quadtree.Point(1,1,1,9,2,3)    # Quadrant One
        point2 = quadtree.Point(1,2,8,9,2,3)    # Quadrant Two
        point3 = quadtree.Point(1,3,1,4,2,3)    # Quadrant Three
        point4 = quadtree.Point(1,4,8,4,2,3)    # Quadrant Four
        
        # Inserting points into each quadrant
        self.quadtree.Insert(point1)
        self.quadtree.Insert(point2)
        self.quadtree.Insert(point3)
        self.quadtree.Insert(point4)
        
        # Query all points
        self.assertEqual(self.quadtree.Query(point1), point1)
        self.assertEqual(self.quadtree.Query(point2), point2)
        self.assertEqual(self.quadtree.Query(point3), point3)
        self.assertEqual(self.quadtree.Query(point4), point4)



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