from structures import Quadtree
# from structures import RTree
# from structures import KDTree
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import FlightPlanGenerator
import math
import random
import numpy as np

def pointConverter():
    pass 


def main():


    # GLOBAL PARAMETERS
    height = "20m"
    
    numPlans = 50
    LongLat = math.ceil(math.sqrt(numPlans) * 2)
    radius = 2

    # Quadtree Initialization
    quadtree = Quadtree.Quadtree(0,0,LongLat,LongLat,1)

    # # Quadtree Points Initialization
    # quadtreePoints = []
    # i = 1
    # j = 1
    # for i in range(1,numPlans): # Number of flights
    #     for j in range(10): # Number of points in flights
    #         point = Quadtree.Point(i,j, (j*radius)-1, LongLat -1, j*2, j)

    #         if j == 0:
    #             point = Quadtree.Point(i,j, 0, LongLat -1, j*2, j)

    #         quadtreePoints.append(point)
    #         # i+=1
    #         j+=1
    #     j=0
    #     i+=1


    quadtreeDictPoints = {}
    for i in range(1,51):
        quadtreePoints = []
        newPlan = True
        longitude = random.randint(0,100)
        latitude = random.randint(0,100)
        altitude = random.randint(0,20)
        randLatLong = random.choice([0, 1])


        for j in range(1,11):
            identification = i
            sequence = j

            time = j
            
            if newPlan == False:
                if randLatLong == 0:
                    longitude += 20
                else:
                    latitude += 20    

            newPlan = False          

            point = Quadtree.Point(identification,sequence,longitude,latitude,altitude,time)
            quadtreePoints.append(point)
            
        quadtreeDictPoints[i] = quadtreePoints

    
    # Point Converter
        # Loop through each plan
        # Get information for BC
    
    for plan in quadtreeDictPoints.values():
        # Getting coords to calculate distance of flight
        startCoords = np.array([plan[0].longitude, plan[0].latitude])
        endCoords = np.array([plan[-1].longitude, plan[-1].latitude])

        # Finding orientation of travel
        if plan[0].longitude == plan[-1].longitude:
            location = str(longitude) + ',' +  str(latitude/2) 
        else:
            location = str(longitude/2) + ',' +  str(latitude) 

        location = str(location) + ",0' AMSL"
        radius = str(np.linalg.norm(startCoords - endCoords)) + 'm'



    # # R-Tree Initialization
    # FANOUT = 4
    # rtree = RTree.RTree(0,0,1000,1000, FANOUT)

    # # K-D Tree Initialization
    # kdtree = KDTree.KDTree()

    # Parameters being sent are just cylinders that encapsulate entire plan

    # Example Times, ISO-8601
    start_time = "2020-09-29T00:00:00Z"
    expire_time =   "2020-09-29T00:10:00Z"

    # location = "42,-70,0' AMSL" # Based on spacing between each plan (long, lat, ft above ground, Above Mean Sea Level)
    # radius = "2m"               # Based on spacing between each plan
    # height = "20m"              # Based on max altitude of each plan

    # Flight Plan Generator Initialization
    fpg = FlightPlanGenerator.FlightPlanGenerator(start_time, expire_time ,location, radius, height)

    # Set flight plan
    # fpg.addParams(start_time, expire_time ,location, radius, height)

    x = fpg.sendRequest()

    print("X")


if __name__ == "__main__":
    # execute only if run as a script
    main()

