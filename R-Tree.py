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

# Class for object in R-Tree. Represents a flight plan, which is a set of points. This can be though of as a MINIMUM BOUNDING BOX
class Object:
    def __init__(self, latitude1, longitude1, latitude2, longitude2, points = []):
        self.bL = (longitude1, latitude1) # Bottom left corner (X,Y)
        self.tR = (longitude2, latitude2) # Top right corner (X,Y)
        self.points = points



    def setPoint(self, point):
        self.points.append(point)

    def getPoint(self, point):
        if point in self.points:
            return point
        return None

    def getCoords(self):
        return (self.bL, self.tR)
        
    def removePoint(self, point):
        if self.getPoint(point) != None:
            self.points.remove(point)
            return 1
        return None


# Class for node in R-Tree. Contains Leaf nodes or Objects
class Node:
    # New nodes will be type Leaf and store no objects
    def __init__(self, bL, tR, fanout, objects={}, children=[], root=0, parent = None): 
        self.objects = objects
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR
        self.parent = parent



    # Add a single objects to objects dict
    def setObject(self, newObject):
       
        key = newObject.getCoords()

        if key in self.objects.keys():
            self.objects[key].append(newObject)
        else:
            self.objects[key] = [newObject]
        
    # Replace existing objects dict
    def setObjects(self, newPointDict):
        self.objects = newPointDict

    def getNumObjects(self):
        return len(self.objects)

    def getCoords(self):
        return self.bL, self.tR

    def getObjects(self):
        return self.objects
    
    def getParent(self):
        return self.parent

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def purgeObjects(self):
        self.objects = {}
     
    def purgeChildren(self):
        self.children = []

    def removeObjects(self, point):
        key = (point.getLong(), point.getLat())
        self.objects[key].remove(point)

        if len(self.objects[key]) == 0:
            self.objects.pop(key)
    
    def isRoot(self):
        return self.root








# Class for R-Tree
class RTree:
    # Give initial size of R-Tree
    # Creates root node
    def __init__(self, longitude1, latitude1, longitude2, latitude2, fanout): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.fanout = fanout # Max points before decomposition. FANOUT
        self.root = Node(bL, tR, fanout, root = 1) # Create root node



    # Traverse tree to find node with given object
    def traverseNode(self, node, object):
        result = None

        if node.isRoot() and len(node.getChildren()) == 0:
            return node

        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getObjects()) <= 0 or len(node.getChildren()) <= 0 and object not in node.getObjects():
            return  # Return None

        # Loop through all children of current node
        for child in node.getChildren():
            bottomLeftObject = object.getCoords()[0]
            topRightObject = object.getCoords()[1]
            bottomLeftNode = child.getCoords()[0]     # Bottom left coords of node
            topRightNode = child.getCoords()[1]       # Top right coords of node

            # Check if point is within child
            if bottomLeftNode[0] <= bottomLeftObject[0] and bottomLeftNode[1] <= bottomLeftObject[1] and topRightNode[0] >= topRightObject[0] and topRightNode[1] >= topRightNode[1]:
                # Check if child has children
                if len(child.getChildren()) == 0:
                    return child    # Return node
                else:
                    result = self.traverseNode(child, object)  # Recurse method again with child node

        return result # Return node


    # Insert object into a node
    def Insert(self, object):

        # Check if object exists
        
        # if object doesn't exist, add to node or make one
        if len(self.root.getChildren()) == 0:
            # Create new leaf node with object 
            newChild = Node(object.getCoords()[0], object.getCoords()[1], self.fanout, objects=object, parent=self.root)
            # Add leaf node to root
            self.root.setChildren(newChild)
        else:
            # Find leaf node
            node = self.traverseNode(self.root, object)
            # Check if there is a node
            if node != None:
                # Add object to node 
                node.setObject(object)
            











def main():



    # # Initialize R-Tree
    rtree = RTree(0,0,1000,1000, 4)
    
    point1 = Point(1,1,1,1,2,3)
    point2 = Point(1,2,1,2,2,3)
    point3 = Point(1,3,1,3,1,1)
    point4 = Point(1,4,1,4,1,1)


    f1Points = [point1,point2,point3,point4]    # List of points
    start = (point1.getLong(), point1.getLat()) # Start coords
    end = (point4.getLong(), point4.getLat())   # End coords


    f1 = Object(start[0], start[1], end[0], end[1], f1Points)   # Object with points

    rtree.Insert(f1)




### Query


### Delete


### Update



    x = 1



    


if __name__ == "__main__":
    # execute only if run as a script
    main()  