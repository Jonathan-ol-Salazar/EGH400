import json
import requests
from structures import Quadtree

# Script to generate flight plans and interact with Skyy Network blockchain


# PARAMETERS

# # Example Times, ISO-8601
# start_time = "2020-09-29T00:00:00Z"
# expire_time =   "2020-09-29T00:10:00Z"

# location = "42,-70,0' AMSL" 
# radius = "1m" 
# height = "20m"



# # URL for blockchain 
# URLpost = "http://127.0.0.1:1317/skyy/cylinder"

# # data 
# data = {
#     "base_req": {
#         "chain_id": "skyyNetwork",
#         "from": "skyy14a5vmle5xwjz7tcawcgt0leu3vp90vugt9ugry",
#         "gas": "auto"
#     },
#     "start_time": start_time,
#     "expire_time": expire_time,
#     "location": location,
#     "radius": radius,
#     "height": height
# }




# # POST 
# resp = requests.post(URLpost, json=data)

# if resp.status_code == 200:
#     print("APPROVED")
#     # Convert to points
#     # Add to data structure
# else:
#     print("DENIED")



class FlightPlanGenerator:
    def __init__(self, start_time, expire_time, location, radius, height, generateRandom=False):
        self.generateRandom = generateRandom
        self.start_time = start_time
        self.expire_time = expire_time
        self.location = location
        self.radius = radius
        self.height = height
        # Possibly add function to convert Point to point
    
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


    # Random Point Generator
    def randomGenerator(self):
        pass
        # Generate random points for sendRequest

    # Request
    def sendRequest(self):
        # URL for blockchain 
        URLpost = "http://127.0.0.1:1317/skyy/cylinder"

        # data 
        data = {
            "base_req": {
                "chain_id": "skyyNetwork",
                "from": "skyy14a5vmle5xwjz7tcawcgt0leu3vp90vugt9ugry",
                "gas": "auto"
            },
            "start_time": self.start_time,
            "expire_time": self.expire_time,
            "location": self.location,
            "radius": self.radius,
            "height": self.height
        }




        # POST 
        resp = requests.post(URLpost, json=data)

        if resp.status_code == 200:
            print("APPROVED")
            # Convert to points
            # Add to data structure
            return 1
        else:
            print("DENIED")
            return None


    def setQuadtreePlans(self, plans):
        pass

    def setRTreePlans(self):
        pass

    def setKDTreePlans(self):
        pass