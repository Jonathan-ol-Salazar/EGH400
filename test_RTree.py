import unittest
import sys
import math

import RTree as rtree


class TestRTree(unittest.TestCase):
    def setUp(self):

        # Initial params
        longitude1 = 0
        latitude1 = 0
        longitude2 = 10
        latitude2 = 10
        fanout = 2

        self.rtree = rtree.RTree(latitude1, longitude1, latitude2, longitude2, fanout)
        # self.rtree.root.purgeChildren()
        # self.rtree.root.purgeObjects()

        # Creating objects

        # Object 1 
        point1 = rtree.Point(1,1,1,1,2,3)
        point2 = rtree.Point(1,2,1,2,2,3)
        point3 = rtree.Point(1,3,1,3,1,1)
        point4 = rtree.Point(1,4,1,4,1,1)
        f1Points = [point1,point2,point3,point4]    # List of points
        self.f1 = self.rtree.createObject(f1Points)

        # Object 2 
        point1 = rtree.Point(2,1,2,1,2,3)
        point2 = rtree.Point(2,2,2,2,2,3)
        point3 = rtree.Point(2,3,2,3,1,1)
        point4 = rtree.Point(2,4,2,4,1,1)
        f2Points = [point1,point2,point3,point4]    # List of points
        self.f2 = self.rtree.createObject(f2Points)


        # Object 3 
        point1 = rtree.Point(3,1,3,1,2,3)
        point2 = rtree.Point(3,2,3,2,2,3)
        point3 = rtree.Point(3,3,3,3,1,1)
        point4 = rtree.Point(3,4,3,4,1,1)
        f3Points = [point1,point2,point3,point4]    # List of points
        self.f3 = self.rtree.createObject(f3Points)


        # Object 4
        point1 = rtree.Point(4,1,4,1,2,3)
        point2 = rtree.Point(4,2,4,2,2,3)
        point3 = rtree.Point(4,3,4,3,1,1)
        point4 = rtree.Point(4,4,4,4,1,1)
        f4Points = [point1,point2,point3,point4]    # List of points
        self.f4 = self.rtree.createObject(f4Points)

        # Object 5 
        point1 = rtree.Point(5,1,5,1,2,3)
        point2 = rtree.Point(5,2,5,2,2,3)
        point3 = rtree.Point(5,3,5,3,1,1)
        point4 = rtree.Point(5,4,5,4,1,1)
        f5Points = [point1,point2,point3,point4]    # List of points
        self.f5 = self.rtree.createObject(f5Points)



    def test_createObject(self):

        # HORIZONTAL OBJECT
        point1 = rtree.Point(1,1,1,1,2,3)
        point2 = rtree.Point(1,2,1,2,2,3)
        point3 = rtree.Point(1,3,1,3,1,1)
        point4 = rtree.Point(1,4,1,4,1,1)
        pointsH = [point1,point2,point3,point4]    # List of points, HORIZONTAL

        start = (pointsH[0].getLong(), pointsH[0].getLat()) # Start coords
        end = (pointsH[-1].getLong(), pointsH[-1].getLat()) # End coords

        self.assertEqual(self.rtree.createObject(pointsH).getPoints(), rtree.Object(start[0], start[1], end[0], end[1], 1, points=pointsH).getPoints())   


        # VERTICAL OBJECT        
        point1 = rtree.Point(1,1,1,1,2,3)
        point2 = rtree.Point(1,2,2,1,2,3)
        point3 = rtree.Point(1,3,3,1,1,1)
        point4 = rtree.Point(1,4,4,1,1,1)
        pointsV = [point1,point2,point3,point4]    # List of points, VERTICAL

        start = (pointsV[0].getLong(), pointsV[0].getLat()) # Start coords
        end = (pointsV[-1].getLong(), pointsV[-1].getLat()) # End coords

        self.assertEqual(self.rtree.createObject(pointsV).getPoints(), rtree.Object(start[0], start[1], end[0], end[1], 0, points=pointsV).getPoints() )     

        
        # NON VERTICAL OR HORIZONTAL OBJECT
        point1 = rtree.Point(1,1,1,9,2,3)
        point2 = rtree.Point(1,2,2,1,2,3)
        point3 = rtree.Point(1,3,3,1,1,1)
        point4 = rtree.Point(1,4,4,2,1,1)           # Altered latitude
        points = [point1,point2,point3,point4]      # List of points, VERTICAL

        self.assertEqual(self.rtree.createObject(points), None)

    def test_Insert(self):
        # FOR REPORT
        # Initial Insert
        # self.assertEqual(self.rtree.Insert(self.f1), 1)    
        # # Insert 2nd point
        # self.assertEqual(self.rtree.Insert(self.f2), 1)    
        # # Insert 3rd point
        # self.assertEqual(self.rtree.Insert(self.f3), 1) 
        # # Insert 4th point
        # self.assertEqual(self.rtree.Insert(self.f4), 1)            
        

        # Object 1 
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects before insert
        self.assertEqual(len(self.rtree.root.getChildren()), 0)     # No children before insert
        
        self.assertEqual(self.rtree.Insert(self.f1), 1)            # Initial Insert

        self.assertEqual(len(self.rtree.root.getChildren()), 1)     # Children after insert
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects after insert
        self.assertEqual(self.rtree.root.getParent(), None)         # No Parent


        # Object 2      
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects before insert
        self.assertEqual(len(self.rtree.root.getChildren()), 1)     # No children before insert
        
        # self.rtree.Insert(self.f2)
        self.assertEqual(self.rtree.Insert(self.f2), 1)            # Insert another object

        self.assertEqual(len(self.rtree.root.getChildren()), 1)     # Children after insert
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects after insert
        self.assertEqual(self.rtree.root.getParent(), None)         # No Parent
      


        # Object 3 
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects before insert
        self.assertEqual(len(self.rtree.root.getChildren()), 1)     # No children before insert
        
        self.rtree.Insert(self.f3)
        # self.assertEqual(self.rtree.Insert(f3), 1)            # Insert another object

        self.assertEqual(len(self.rtree.root.getChildren()), 2)     # Children after insert
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects after insert
        self.assertEqual(self.rtree.root.getParent(), None)         # No Parent



        # Object 4       
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects before insert
        self.assertEqual(len(self.rtree.root.getChildren()), 2)     # No children before insert
        
        self.rtree.Insert(self.f4)
        # self.assertEqual(self.rtree.Insert(f4), 1)            # Insert another object

        self.assertEqual(len(self.rtree.root.getChildren()), 2)     # Children after insert
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects after insert
        self.assertEqual(self.rtree.root.getParent(), None)         # No Parent



        # Object 5       
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects before insert
        self.assertEqual(len(self.rtree.root.getChildren()), 2)     # No children before insert
        
        self.rtree.Insert(self.f5)
        # self.assertEqual(self.rtree.Insert(f5), 1)            # Insert another object

        self.assertEqual(len(self.rtree.root.getChildren()), 2)     # Children after insert
        self.assertEqual(len(self.rtree.root.getObjects()), 0)      # No objects after insert
        self.assertEqual(self.rtree.root.getParent(), None)         # No Parent


    def test_Delete(self):
        # Deleting non existing object
        point1 = rtree.Point(5,1,0,0,2,3)
        point2 = rtree.Point(5,2,0,0,2,3)
        point3 = rtree.Point(5,3,0,0,1,1)
        point4 = rtree.Point(5,4,0,0,1,1)
        dummyPoints = [point1,point2,point3,point4]    # List of points
        objectDummy = self.rtree.createObject(dummyPoints)

        self.assertEqual(self.rtree.Delete(objectDummy), 0)

        
        
        # Deleting existing object

        # Add all objects
        self.rtree.Insert(self.f1)
        self.rtree.Insert(self.f2)
        self.rtree.Insert(self.f3)
        self.rtree.Insert(self.f4)
        self.rtree.Insert(self.f5)

        # Find them -> Delete them -> Find them
        self.assertEqual(self.rtree.Query(self.f1), self.f1)
        self.assertEqual(self.rtree.Delete(self.f1), 1)
        self.assertEqual(self.rtree.Query(self.f1), 0)

        self.assertEqual(self.rtree.Query(self.f2), self.f2)
        self.assertEqual(self.rtree.Delete(self.f2), 1)
        self.assertEqual(self.rtree.Query(self.f2), 0)

        self.assertEqual(self.rtree.Query(self.f3), self.f3)
        self.assertEqual(self.rtree.Delete(self.f3), 1)
        self.assertEqual(self.rtree.Query(self.f3), 0)

        self.assertEqual(self.rtree.Query(self.f4), self.f4)
        self.assertEqual(self.rtree.Delete(self.f4), 1)
        self.assertEqual(self.rtree.Query(self.f4), 0)

        self.assertEqual(self.rtree.Query(self.f5), self.f5)
        self.assertEqual(self.rtree.Delete(self.f5), 1)
        self.assertEqual(self.rtree.Query(self.f5), 0)




    def test_Query(self):       
        # Find objects before being inserted
        self.assertEqual(self.rtree.Query(self.f1), 0)
        self.assertEqual(self.rtree.Query(self.f2), 0)
        self.assertEqual(self.rtree.Query(self.f3), 0)
        self.assertEqual(self.rtree.Query(self.f4), 0)
        self.assertEqual(self.rtree.Query(self.f5), 0)

        # Add all objects
        self.rtree.Insert(self.f1)
        self.rtree.Insert(self.f2)
        self.rtree.Insert(self.f3)
        self.rtree.Insert(self.f4)
        self.rtree.Insert(self.f5)


        # Find them
        self.assertEqual(self.rtree.Query(self.f1), self.f1)

        self.assertEqual(self.rtree.Query(self.f2), self.f2)

        self.assertEqual(self.rtree.Query(self.f3), self.f3)
 
        self.assertEqual(self.rtree.Query(self.f4), self.f4)

        self.assertEqual(self.rtree.Query(self.f5), self.f5)





        # Find them -> Delete them -> Find them
        self.assertEqual(self.rtree.Query(self.f1), self.f1)
        self.assertEqual(self.rtree.Delete(self.f1), 1)
        self.assertEqual(self.rtree.Query(self.f1), 0)

        self.assertEqual(self.rtree.Query(self.f2), self.f2)
        self.assertEqual(self.rtree.Delete(self.f2), 1)
        self.assertEqual(self.rtree.Query(self.f2), 0)

        self.assertEqual(self.rtree.Query(self.f3), self.f3)
        self.assertEqual(self.rtree.Delete(self.f3), 1)
        self.assertEqual(self.rtree.Query(self.f3), 0)

        self.assertEqual(self.rtree.Query(self.f4), self.f4)
        self.assertEqual(self.rtree.Delete(self.f4), 1)
        self.assertEqual(self.rtree.Query(self.f4), 0)

        self.assertEqual(self.rtree.Query(self.f5), self.f5)
        self.assertEqual(self.rtree.Delete(self.f5), 1)
        self.assertEqual(self.rtree.Query(self.f5), 0)







if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()