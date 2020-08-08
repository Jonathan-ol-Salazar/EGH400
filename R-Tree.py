import Custom_Exception
import datetime 

# Main R-Tree file containing classes: Rtree, Point and Node



# Class for point in R-Tree
class Point:
    def __init__(self, identification, sequence, longitude, latitude, altitude, time): # long = x, lat = y
        self.id = identification
        self.sequence = sequence
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.time = time

    def getID(self):
        return self.id
    
    def getSequence(self):
        return self.sequence

    def getLong(self):
        return self.longitude

    def getLat(self):
        return self.latitude

    def getAlt(self):
        return self.altitude
    
    def getTime(self):
        return self.time
    
    def getKey(self):
        return (self.longitude, self.latitude)

    def getAll(self):
        return [self.id, self.sequence, self.longitude, self.latitude, self.altitude, self.time]

    def setAll(self, attrs):

        allCorrectType = False
        
        # Loop through all attrs and check if they are all the correct types
        for attr in attrs:
            if self.checkInt(attr) == 1:
                allCorrectType = True
                break
        
        # Check if there is a correct number of attrs to change
        if len(attrs) != len(self.getAll()) and allCorrectType == True:
            print("Not enough attributes, did not update point")
        elif allCorrectType == True:
            for i, attr in enumerate(attrs):
                # Switch statement of somesort, via if-statements
                if i == 0:  # ID
                   self.id = attr                  
                elif i == 1: # Sequence
                    self.sequence = attr                 
                elif i == 2: # Long
                    self.longitude = attr                      
                elif i == 3: # Lat
                    self.latitude = attr                   
                elif i == 4: # Alt
                    self.altitude = attr                    
                elif i == 5: # Time
                    self.time = attr
    
    def getCoords(self):
        return [self.longitude, self.latitude]

    def setID(self, identification):
        if self.checkInt(identification) == 1:
            self.id = identification
    
    def setSequence(self, sequence):
        if self.checkInt(sequence) == 1:
            self.sequence = sequence
    
    def setLong(self, longitude):
        if self.checkInt(longitude) == 1:
            self.longitude = longitude
    
    def setLat(self, latitude):
        if self.checkInt(latitude) == 1:
            self.latitude = latitude
    
    def setAlt(self, altitude):
        if self.checkInt(altitude) == 1:
            self.altitude = altitude

    def setTime(self, time):
        # if self.checkDatetime(time) == 1:
        self.time = time


    def checkInt(self, input):
        try:
            if type(input) != int:
                raise Custom_Exception.typeNotInt()
            else:
                return 1 # Passed
        except Custom_Exception.typeNotInt():
            print("Input must be of type 'int' ")
            return 0 # Failed


# Class for node in R-Tree
class Node:
    # New nodes will be type Leaf and store no points
    def __init__(self, bL, tR, points={}, children=[], root=0, parent = None): 
        self.points = points
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR
        self.parent = parent



    # Add a single points to points dict
    def setPoint(self, newPoint):
       
        key = (newPoint.getLong(), newPoint.getLat())

        if key in self.points.keys():
            self.points[key].append(newPoint)
        else:
            self.points[key] = [newPoint]
        
    # Replace existing points dict
    def setPoints(self, newPointDict):
        self.points = newPointDict

    def getNumPoints(self):
        return len(self.points)

    def getCoords(self):
        return self.bL, self.tR

    def getPoints(self):
        return self.points
    
    def getParent(self):
        return self.parent

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def purgePoints(self):
        self.points = {}
     
    def purgeChildren(self):
        self.children = []

    def removePoint(self, point):
        key = (point.getLong(), point.getLat())
        self.points[key].remove(point)

        if len(self.points[key]) == 0:
            self.points.pop(key)
    
    def isRoot(self):
        return self.root


# Class for object in R-Tree. Represents a flight plan, which is a set of points
class Object:
    def __init__(self, latitude1, longitude1, latitude2, longitude2, points = []):
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)
        self.points = points



    def setPoint(self, point):
        self.points.append(point)

    def getPoint(self, point):
        if point in self.points:
            return point

        return None
        
    def removePoint(self, point):
        if self.getPoint(point) != None:
            self.points.remove(point)
            return 1
        return None






# Class for R-Tree
class RTree:
    # Give initial size of R-Tree
    # Creates root node
    def __init__(self, latitude1, longitude1, latitude2, longitude2, maxPoints): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.maxPoints = maxPoints # Max points before decomposition
        self.root = Node(bL, tR, root = 1) # Create root node













def main():





    # # Initialize R-Tree
    # rtree = RTree(0,0,10,10, 1)
    
    # point1 = Point(1,1,1,1,2,3)
    # point2 = Point(1,2,1,2,2,3)
    # point3 = Point(1,3,1,3,1,1)
    # point4 = Point(1,4,1,1,1,1)





### Query


### Delete


### Update



    x = 1



    


if __name__ == "__main__":
    # execute only if run as a script
    main()  