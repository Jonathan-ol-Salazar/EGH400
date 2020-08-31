import unittest
import sys
import math

import KDTree as kdtree

class TestKDTree(unittest.TestCase):
    def setUp(self):

        # Dummy points from GeeksforGeeks site on KDTree
        # (3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)
        self.point1 = kdtree.Point(1,1,3,6,2,3)
        self.point2 = kdtree.Point(1,2,17,15,2,3)
        self.point3 = kdtree.Point(1,3,13,15,1,1)
        self.point4 = kdtree.Point(1,4,6,12,1,1)
        self.point5 = kdtree.Point(1,5,9,1,2,3)
        self.point6 = kdtree.Point(1,6,2,7,1,1)
        self.point7 = kdtree.Point(1,7,10,19,1,1)

        self.f1Points = [self.point1,self.point2,self.point3,self.point4,self.point5,self.point6,self.point7]    # List of points


        self.kdtree = kdtree.KDTree()


    def test_Insert(self):
        # FOR REPORT
        # # Initial Insert
        # self.assertEqual(self.kdtree.Insert(self.f1), 1)    
        # # Insert 2nd point
        # self.assertEqual(self.kdtree.Insert(self.f2), 1)    
        # # Insert 3rd point
        # self.assertEqual(self.kdtree.Insert(self.f3), 1) 
        # # Insert 4th point
        # self.assertEqual(self.kdtree.Insert(self.f4), 1)            
        
        
        for point in self.f1Points:
           self.assertEqual(self.kdtree.Insert(point), 1)            
        

    def test_Delete(self):
        # Deleting a non-existent point
        self.assertEqual(self.kdtree.Delete(self.point1), 0)
        self.assertEqual(self.kdtree.Delete(self.point2), 0)
        self.assertEqual(self.kdtree.Delete(self.point3), 0)
        self.assertEqual(self.kdtree.Delete(self.point4), 0)
        self.assertEqual(self.kdtree.Delete(self.point5), 0)        

        # Adding points to delete
        for point in self.f1Points:
           self.assertEqual(self.kdtree.Insert(point), 1)            
    
        # Deleting an existent point
        self.assertEqual(self.kdtree.Delete(self.point1), 1)
        self.assertEqual(self.kdtree.Delete(self.point2), 1)
        self.assertEqual(self.kdtree.Delete(self.point3), 1)
        self.assertEqual(self.kdtree.Delete(self.point4), 1)
        self.assertEqual(self.kdtree.Delete(self.point5), 1)        


    def test_Query(self):
      # Searching a non-existent point
        self.assertEqual(self.kdtree.Query(self.point1), 0)
        self.assertEqual(self.kdtree.Query(self.point2), 0)
        self.assertEqual(self.kdtree.Query(self.point3), 0)
        self.assertEqual(self.kdtree.Query(self.point4), 0)
        self.assertEqual(self.kdtree.Query(self.point5), 0)        

        # Adding points to search
        for point in self.f1Points:
           self.assertEqual(self.kdtree.Insert(point), 1)            
    
        # Searching an existent point
        self.assertEqual(self.kdtree.Query(self.point1), self.point1)
        self.assertEqual(self.kdtree.Query(self.point2), self.point2)
        self.assertEqual(self.kdtree.Query(self.point3), self.point3)
        self.assertEqual(self.kdtree.Query(self.point4), self.point4)
        self.assertEqual(self.kdtree.Query(self.point5), self.point5)

        


