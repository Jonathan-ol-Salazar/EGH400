import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from structures import Quadtree
from structures import RTree
from structures import KDTree

# sys.setrecursionlimit(int(MAX)) 
import FlightPlanGenerator



def main():


    # GLOBAL PARAMETERS
    maxPoints = 1

    # QLD Coverage
    longitude1 = 138
    latitude1 = 28
    longitude2 = 153
    latitude2 = 10

    # Generator Params
    numPlans = 50
    numPoints = 10
    maxAltitude = 20

    # Quadtree Initialization
    quadtree = Quadtree.Quadtree(longitude1,latitude1,longitude2,latitude2,maxPoints)

    # R-Tree Initialization
    FANOUT = 4
    rtree = RTree.RTree(longitude1,latitude1,longitude2,latitude2,FANOUT)

    # K-D Tree Initialization
    kdtree = KDTree.KDTree()

    # Flight Plan Generator Initialization
    fpg = FlightPlanGenerator.FlightPlanGenerator(longitude1,latitude1,longitude2,latitude2,numPlans,numPoints,maxAltitude)

################## FLIGHT PLAN GENERATIONS #####################

    # Take off and land
    fpg.manualGenerator()
    quadtreePoints = fpg.getPointsStructures("quad")

    # if fpg.sendRequests() == 1:
    # Quadtree 
    insertResultQuad = []
    for plan in quadtreePoints.values():
        for point in plan:
            # print(point.getAll())
            insertResultQuad.append(quadtree.Insert(point))
        
    
    # Random flight    
    fpg.randomGenerator()
    kdtreePoints = fpg.getPointsStructures("kd")
    rtreePoints = fpg.getPointsStructures("r")

    # if fpg.sendRequests() == 1:
    # KDTree
    insertResultKD = []
    for plan in kdtreePoints.values():
        for point in plan:
            insertResultKD.append(kdtree.Insert(point))
        
    # RTree
    insertResultR = []
    for plan in rtreePoints:
        insertResultR.append(rtree.Insert(plan))


 
    x = 1

if __name__ == "__main__":
    # execute only if run as a script
    main()

