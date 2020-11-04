import json
import requests
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from structures import Quadtree, KDTree, RTree
import math
import random
import numpy as np
# Script to generate flight plans and interact with Skyy Network blockchain




class FlightPlanGenerator:
    # def __init__(self, start_time, expire_time, location, radius, height, generateRandom=False):
    #     self.generateRandom = generateRandom
    #     self.start_time = start_time
    #     self.expire_time = expire_time
    #     self.location = location
    #     self.radius = radius
    #     self.height = height
    #     # Possibly add function to convert Point to point

    
    def __init__(self,longitude1,latitude1,longitude2,latitude2, numPlans, numPoints, maxAltitude):
        # Default parameters: 50 flight plans with 10 points each at 20m altitude
        self.height = "20m"
        self.start_time = "2021-09-29T00:00:00Z"
        self.expire_time = "2021-09-29T00:10:00Z"
        self.longitude1 = longitude1
        self.longitude2 = longitude2
        self.latitude1 = latitude1
        self.latitude2 = latitude2
        self.numPlans = numPlans
        self.numPoints = numPoints
        self.maxAltitude = maxAltitude
   
    def addParams(self, start_time, expire_time, location, radius, height):
        self.start_time = start_time
        self.expire_time = expire_time
        self.location = location
        self.radius = radius
        self.height = height


    # Setters
    def setStartTime(self, start_time):
        self.start_time = start_time

    def setEndTime(self, expire_time):
        self.expire_time = expire_time

    def setLocation(self, location):
        self.location = location

    def setRadius(self, radius):
        self.radius = radius

    def setHeight(self, height):
        self.height = height
    
    def setPoints(self, points):
        self.points = points
    
    def setPointsBC(self, pointsBC):
        self.pointsBC = pointsBC


    # Getters
    def getStartTime(self):
        return self.start_time

    def getEndTime(self):
        return self.expire_time

    def getLocation(self):
        return self.location

    def getRadius(self):
        return self.radius

    def getHeight(self):
        return self.height
    
    def getPoints(self):
        return self.points
    
    def getPointsStructures(self, structure):
        if structure == "quad" or structure == "kd":
            return self.getPoints()
        elif structure == "r":
            plansObjectList = []
            # Get points
            plans = self.getPoints()
            # Convert them to RTree object
            for plan in plans.values():
                plansObjectList.append(RTree.createObject(plan))
            
            return plansObjectList
        else:
            return None


    def getLongitude1(self):
        return self.longitude1
        
    def getLongitude2(self):
        return self.longitude2

    def getLatitude1(self):
        return self.latitude1

    def getLatitude2(self):
        return self.latitude2

    def getNumPlans(self):
        return self.numPlans
    
    def getNumPoints(self):
        return self.numPoints
    
    def getMaxAltitude(self):
        return self.maxAltitude


    def manualGenerator(self, numPlans=50, numPoints=10, longitude=153, latitude=28, altitude=0):
        # Flight plans stored in dictionary
        dictPoints = {}

        # For loop to make 50 plans
        for i in range(1,self.getNumPlans()+1):
            # List to store flight points
            quadtreePoints = []                     


            # For loop to make 10 points in plan
            for j in range(1,self.getNumPoints()+1):
                identification = i
                sequence = j
                time = j
                
                # Take off and hover
                altitude += 1        

                # Make new point
                point = Quadtree.Point(identification,sequence,longitude,latitude,altitude,time)
                quadtreePoints.append(point)

            # Add to flight plan dictionary    
            dictPoints[i] = quadtreePoints
        
        self.setPoints(dictPoints)


    # Random Point Generator
    def randomGenerator(self):

        # Flight plans stored in dictionary
        dictPoints = {}

        # For loop to make 50 plans
        for i in range(1,self.getNumPlans()+1):
            # List to store flight points
            quadtreePoints = []                     
            newPlan = True

            # Random variables
            # longitude = random.randint(0,100)
            # latitude = random.randint(0,70)
            longitude = random.randint(self.getLongitude1(),self.getLongitude2())
            latitude = random.randint(self.getLatitude2(), self.getLatitude1())
            altitude = random.randint(0,self.getMaxAltitude())
            randLatLong = random.choice([0, 1])

            # For loop to make 10 points in plan
            for j in range(1,self.getNumPoints()+1):
                identification = i
                sequence = j

                time = j
                
                if newPlan == False:
                    if randLatLong == 0:
                        longitude += 1
                    else:
                        latitude += 1    

                newPlan = False          

                # Make new point
                point = Quadtree.Point(identification,sequence,longitude,latitude,altitude,time)
                quadtreePoints.append(point)

            # Add to flight plan dictionary    
            dictPoints[i] = quadtreePoints
        
        self.setPoints(dictPoints)

    # Convert points to BC
    def pointConverter(self, plan): 
        # Point Converter
            # Loop through each plan
            # Get information for BC and store in dict


            # Getting coords to calculate distance of flight
            startCoords = np.array([plan[0].longitude, plan[0].latitude])
            endCoords = np.array([plan[-1].longitude, plan[-1].latitude])

            # Finding orientation of travel
            if plan[0].longitude == plan[-1].longitude:
                location = str(plan[-1].latitude/2) + ',' + str(plan[0].longitude)
            else:
                location = str(plan[1].latitude) + ',' + str(plan[-1].longitude/2)

            location = str(location) + ",0' AMSL"
            radius = str(np.linalg.norm(startCoords - endCoords)) + 'm'

            if startCoords.tolist() == endCoords.tolist():
                radius = '10m'

            return [location, radius]




    # Request
    def sendRequests(self):
        # URL for blockchain 
        URLpost = "http://127.0.0.1:1317/skyy/cylinder"
        
        # Get generated points
        plans = self.getPoints()

        # Loop through each point in plan and send to blockchain
        for plan in plans.values():
            # Convert the points to blockchain format
            dataBC = self.pointConverter(plan)
            
            # data 
            data = {
                "base_req": {
                    "chain_id": "skyyNetwork",
                    "from": "skyy14a5vmle5xwjz7tcawcgt0leu3vp90vugt9ugry",
                    "gas": "auto"
                },
                "start_time": self.getStartTime(),
                "expire_time": self.getEndTime(),
                "location": dataBC[0],
                "radius": dataBC[1],
                "height": self.getHeight()
            }


            # POST 
            resp = requests.post(URLpost, json=data)

            # Check if request is sent to blockchain
            if resp.status_code == 200:

                print("APPROVED")
            else:
                print("DENIED")
                return None
                
        return 1

    def setQuadtreePlans(self, plans):
        pass

    def setRTreePlans(self):
        pass

    def setKDTreePlans(self):
        pass