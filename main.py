from structures import Quadtree
# from structures import RTree
# from structures import KDTree
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import FlightPlanGenerator



def main():
    
    # Quadtree Initialization
    quadtree = Quadtree.Quadtree(0,0,10,10,1)

    # # R-Tree Initialization
    # FANOUT = 4
    # rtree = RTree.RTree(0,0,1000,1000, FANOUT)

    # # K-D Tree Initialization
    # kdtree = KDTree.KDTree()



    # Example Times, ISO-8601
    start_time = "2020-09-29T00:00:00Z"
    expire_time =   "2020-09-29T00:10:00Z"

    location = "42,-70,0' AMSL" 
    radius = "1m" 
    height = "20m"

    # Flight Plan Generator Initialization
    fpg = FlightPlanGenerator.FlightPlanGenerator(start_time, expire_time ,location, radius, height)

    # Set flight plan
    # fpg.addParams(start_time, expire_time ,location, radius, height)

    x = fpg.sendRequest()

    print("X")


if __name__ == "__main__":
    # execute only if run as a script
    main()

