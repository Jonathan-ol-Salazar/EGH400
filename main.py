from structures import Quadtree
from structures import RTree
from structures import KDTree
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

# sys.setrecursionlimit(int(MAX)) 
import FlightPlanGenerator


def pointConverter():
    pass 


def main():


    # GLOBAL PARAMETERS
    height = "20m"
    LongLat = 100

    # Quadtree Initialization
    quadtree = Quadtree.Quadtree(0,0,LongLat,LongLat,1)
    rtree = RTree.RTree(0,0,LongLat,LongLat,4)
    kdtree = KDTree.KDTree()



    # # R-Tree Initialization
    # FANOUT = 4
    # rtree = RTree.RTree(0,0,1000,1000, FANOUT)

    # # K-D Tree Initialization
    # kdtree = KDTree.KDTree()

    # Parameters being sent are just cylinders that encapsulate entire plan



    # location = "42,-70,0' AMSL" # Based on spacing between each plan (long, lat, ft above ground, Above Mean Sea Level)
    # radius = "2m"               # Based on spacing between each plan
    # height = "20m"              # Based on max altitude of each plan

    # Flight Plan Generator Initialization
    fpg = FlightPlanGenerator.FlightPlanGenerator()
    fpg.randomGenerator()

    quadtreePoints = fpg.getPointsStructures("quad")
    kdtreePoints = fpg.getPointsStructures("kd")
    rtreePoints = fpg.getPointsStructures("r")

    # x = fpg.sendRequests()
    x = 1
    # Adding points to structures
    if x != None: 
        # # Quadtree 
        # insertResultQuad = []
        # for plan in quadtreePoints.values():
        #     for point in plan:
        #         insertResultQuad.append(quadtree.Insert(point))
        
        # KDTree
        insertResultKD = []
        for plan in kdtreePoints.values():
            for point in plan:
                insertResultKD.append(kdtree.Insert(point))
        
        # RTree
        insertResultR = []
        for plan in rtreePoints:
            c= rtree.Insert(plan)
            if c == 0:
                print("asdf")
            insertResultR.append(c)

            # insertResultR.append(rtree.Insert(plan))



    # x = fpg.sendRequest()

    print("X")


if __name__ == "__main__":
    # execute only if run as a script
    main()

