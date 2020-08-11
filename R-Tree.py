import Custom_Exception
import datetime 


# Main R-Tree file containing classes: Rtree, Point and Node

FANOUT = 2


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
    def __init__(self, latitude1, longitude1, latitude2, longitude2, orientation, points = []):
        self.bL = (longitude1, latitude1) # Bottom left corner (X,Y)
        self.tR = (longitude2, latitude2) # Top right corner (X,Y)
        self.points = points
        self.orientation = orientation # 0 = Horizontal, 1 = Vertical



    def setPoint(self, point):
        self.points.append(point)

    def getPoint(self, point):
        if point in self.points:
            return point
        return None

    def getCoords(self):
        return (self.bL, self.tR)

    def getOrientation(self):
        return self.orientation
        
    def removePoint(self, point):
        if self.getPoint(point) != None:
            self.points.remove(point)
            return 1
        return None


# Class for node in R-Tree. Contains Leaf nodes or Objects
class Node:
    # New nodes will be type Leaf and store no objects
    def __init__(self, bL, tR, fanout=FANOUT, objects={}, children={}, root=0, parent = None): 
        self.objects = objects
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR
        self.parent = parent
        self.fanout = fanout


    def setRoot(self, root):
        self.root = root

    # Add a single objects to objects dict
    def setObject(self, newObject):
       
        key = newObject[0].getCoords()

        if key in self.objects.keys():
            self.objects[key].append(newObject)
        elif isinstance(newObject, list):
            self.objects[key] = newObject
        else:
            self.objects[key] = [newObject]
        

        # Find parent to change the key to this node
        # self.parent.getChildren()[self.findAreaObjects()] = self.parent.getChildren().pop(key)
        if self in self.parent.getChildren().values():
            self.parent.getChildren()[self.findAreaObjects()] = self.parent.getChildren().pop((self.bL, self.tR))

        # Set new coords
        self.bL, self.tR = self.findAreaObjects()




    # Replace existing objects dict
    def setObjects(self, newPointDict):
        self.objects = newPointDict

        if self in self.parent.getChildren().values():
            self.parent.getChildren()[self.findAreaObjects()] = self.parent.getChildren().pop((self.bL, self.tR))

        self.bL, self.tR = self.findAreaObjects()


    def getNumObjects(self):
        return len(self.objects)

    def getCoords(self):
        if len(self.children) == 0:         # if current node is a leaf node, return minimum bounding box of objects
            # self.bL, self.tR = self.findAreaObjects()
            return self.findAreaObjects()
        else:
            # self.bL, self.tR = self.findAreaChildren()
            return self.findAreaChildren()  # return MBB of children


    def setCoords(self):
        if len(self.children) == 0:         # if current node is a leaf node, return minimum bounding box of objects
            self.bL, self.tR = self.findAreaObjects()
            return self.findAreaObjects()
        else:
            self.bL, self.tR = self.findAreaChildren()
            return self.findAreaChildren()  # return MBB of children

    def getArea(self):
        x1 = self.getCoords()[0][0]
        y1 = self.getCoords()[0][1]
        x2 = self.getCoords()[1][0]
        y2 = self.getCoords()[1][1]
        
        # Area of rectangle => L*W
        return  abs((x2-x1)*(y2-y1))

    def getObjects(self):
        return self.objects
    
    def getParent(self):
        return self.parent

    def getFanout(self):
        return self.fanout

    def setChildren(self, child):
        # addChild = self.children + [child]
        # self.children = addChild


        # dictionary -> 2 lists  (k,v)
        # add item to lists 
        # convert back to dictionary

        keys = list(self.children.keys())
        values = list(self.children.values())

        keys = keys + [child.getCoords()]
        values = values + [child]

        self.children = dict(zip(keys, values))

        # Set new coords
        self.bL, self.tR = self.findAreaChildren()


    def getChildren(self):
        return self.children


    def setParent(self, parent):
        self.parent = parent

    def purgeObjects(self):
        self.objects = {}
     
    def purgeChildren(self):
        self.children = {}

    def removeObjects(self, object):
        key = object.getCoords()        # Get key for object
        self.objects[key].remove(object)# Use key to remove from object list

        if len(self.objects[key]) == 0: # Check if key has any values
            self.objects.pop(key)       # Delete key


    
    def isRoot(self):
        return self.root


    def findAreaObjects(self):
        # Return a tuple with area (bL, tR)
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        start = True
        for item in self.objects.keys():
            bL = item[0]
            tR = item[1]

            if start == True:
                x1 = bL[0]
                y1 = bL[1]
                x2 = tR[0]
                y2 = tR[1]
                start = False
            elif bL[0] < x1:    # if object x1 < current x1
                x1 = bL[0]
            elif bL[1] < y1:    # if object y1 < current y1
                y1 = bL[1]
            elif tR[0] > x2:    # if object x2 > currnet x2
                x2 = tR[0]
            elif tR[1] > y2:    # if object y2 > current y2
                y2 = tR[1]

        return ((x1,y1),(x2,y2))
         

    def findAreaChildren(self):
        # Return a tuple with area (bL, tR)
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        start = True
        for item in self.children:
            bL = item[0]
            tR = item[1]

            if start == True:
                x1 = bL[0]
                y1 = bL[1]
                x2 = tR[0]
                y2 = tR[1]
                start = False
            elif bL[0] < x1:    # if object x1 < current x1
                x1 = bL[0]
            elif bL[1] < y1:    # if object y1 < current y1
                y1 = bL[1]
            elif tR[0] > x2:    # if object x2 > currnet x2
                x2 = tR[0]
            elif tR[1] > y2:    # if object y2 > current y2
                y2 = tR[1]

        return ((x1,y1),(x2,y2))





# Class for R-Tree
class RTree:
    # Give initial size of R-Tree
    # Creates root node
    def __init__(self, longitude1, latitude1, longitude2, latitude2, fanout): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.fanout = fanout # Max points before decomposition. FANOUT
        self.root = Node(bL, tR, fanout=fanout, root = 1) # Create root node

    def createObject(self, points):
        start = (points[0].getLong(), points[0].getLat()) # Start coords
        end = (points[-1].getLong(), points[-1].getLat())   # End coords

        if points[0].getLat() == points[-1].getLat():
            return Object(start[0], start[1], end[0], end[1], 1, points=points)   # Object with points, Horizontal, Y-axis the same
        else:
            return Object(start[0], start[1], end[0], end[1], 0, points=points)   # Object with points, Vertical, X-Axis the same


        return None


    # Traverse tree to find node with given object
    def traverseNode(self, node, object):
        result = None

        if node.isRoot() and len(node.getChildren()) == 0:
            return node

        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getObjects()) <= 0 or len(node.getChildren()) <= 0 and object not in node.getObjects():
            return  # Return None

        # Loop through all children of current node
        for child in node.getChildren().values():
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

    # Find the internal nodes that are the furthest apart
    def findSeedsInternal(self,node):

        children = node.getChildren()
        # Get keys, which are tuples of coords
        keys = children.keys()
        # Loop through all the keys and find the min and max for both axis
        minX = None
        maxX = None
        minY = None
        maxY = None
        minimumX = None
        maximumX = None
        minimumY = None
        maximumY = None
        startX = True
        startY = True

        for key in keys:
            valueX = key[0][0]
            if startX == True:
                minX = valueX
                maxX = valueX
                minimumX = key
                maximumX = key
                startX = False
            elif valueX < minX:   # value is less than the current minimum
                minX = valueX
                minimumX = key
            elif valueX > maxX:   # value is greater than the current maximum
                maxX = valueX
                maximumX = key

        # Y-axis, Horizontal (0)
        for key in keys:
            valueY = key[0][1]
            if startY == True:
                minY = valueY
                maxY = valueY
                minimumY = key
                maximumY = key
                startY = False
            elif valueY < minY:   # value is less than the current minimum
                minY = valueY
                minimumY = key
            elif valueY > maxY:   # value is greater than the current maximum
                maxY = valueY
                maximumY = key
    
        # Decide which gap is bigger on which axis
        if startX == True:
            return (children[maximumY], children[minimumY])     # If X-axis wasn't used
        elif startY == True:
            return (children[maximumX], children[minimumX])     # If Y-axis wasn't used
        elif (maxY-minY) > (maxX - minX):
            return (children[maximumY], children[minimumY])     # If Y gap larger than X
        elif (maxY-minY) < (maxX - minX):
            return (children[maximumX], children[minimumX])     # If X gap larger than Y
        else:
            return None



    # Find the objects that are the furthest apart
    def findSeedsLeaf(self, node):

        objects = node.getObjects()
        # Get keys, which are tuples of coords
        keys = objects.keys()
        # Loop through all the keys and find the min and max for both axis
        minX = None
        maxX = None
        minY = None
        maxY = None
        minimumX = None
        maximumX = None
        minimumY = None
        maximumY = None
        startX = True
        startY = True


        # X-axis, Vertical (1)
        for key in keys:
            if objects[key][0].getOrientation() == 1:

                valueX = key[0][0]
                if startX == True:
                    minX = valueX
                    maxX = valueX
                    minimumX = key
                    maximumX = key
                    startX = False
                elif valueX < minX:   # value is less than the current minimum
                    minX = valueX
                    minimumX = key
                elif valueX > maxX:   # value is greater than the current maximum
                    maxX = valueX
                    maximumX = key
        

        # Y-axis, Horizontal (0)
        for key in keys:
            if objects[key][0].getOrientation() == 0:
                valueY = key[0][1]
                if startY == True:
                    minY = valueY
                    maxY = valueY
                    minimumY = key
                    maximumY = key
                    startY = False
                elif valueY < minY:   # value is less than the current minimum
                    minY = valueY
                    minimumY = key
                elif valueY > maxY:   # value is greater than the current maximum
                    maxY = valueY
                    maximumY = key


        # Decide which gap is bigger on which axis
        if startX == True:
            # return (objects[maximumY], objects[minimumY])     # If X-axis wasn't used
            return (maximumY, minimumY)     # If X-axis wasn't used
            
        elif startY == True:
            # return (objects[maximumX], objects[minimumX])     # If Y-axis wasn't used
            return (maximumX, minimumX)     # If Y-axis wasn't used

        elif (maxY-minY) > (maxX - minX):
            # return (objects[maximumY], objects[minimumY])     # If Y gap larger than X
            return (maximumY, minimumY)     # If Y gap larger than X

        elif (maxY-minY) < (maxX - minX):
            # return (objects[maximumX], objects[minimumX])     # If X gap larger than Y
            return (maximumX, minimumX)     # If X gap larger than Y

        else:
            return None



    def linearSplit(self, node):
        # Find objects that are furthest apart along both axis
        # Create node
        # Randomly assign objects to each node via requiring the least enlargement
            # Find the area of the current nodes
            # Compare which one will increase the least from adding new object
        

        if len(node.getChildren()) > node.getFanout():

            # INTERNAL NODE SPLIT
            seeds = self.findSeedsInternal(node)

            # Check if seeds were found
            if seeds == None:
                return 0 # THIS MEANS NO SEEDS WERE FOUND
        
            # Get parent
            parent = node.getParent()

            if parent == None and node.isRoot() == 1:
                newRoot = Node(node.getCoords()[0], node.getCoords()[1], children={node.getCoords():node}, root=1)
                node.setRoot(0)
                node.setParent(newRoot)
                parent = newRoot
                self.root = newRoot

            # Assign current nodes objects to placeholder
            children = node.getChildren()

            # Remove seeds from placeholder
            children.pop(seeds[0].getCoords())
            children.pop(seeds[1].getCoords())


            # Clear the current nodes objects
            node.purgeChildren()

            # Assign seeds
            node.setChildren(seeds[0])

            
            # Create new node and add to parent
            newNode = Node(seeds[1].getCoords()[0], seeds[1].getCoords()[1], children={seeds[1].getCoords():seeds[1]}, parent=parent)
            
           
                
            
            parent.setChildren(newNode)

            # Assign remaining objects based on least enlargement
            for item in children:
                if self.findEnlargement(node,item) > self.findEnlargement(newNode, item):
                    newNode.setChildren(children[item])
                elif self.findEnlargement(node,item) == self.findEnlargement(newNode, item):
                    if node.getArea() > newNode.getArea():
                        newNode.setChildren(children[item])
                    else:
                        node.setChildren(children[item])
                else:
                    node.setChildren(children[item])

        else:

            # LEAF NODE SPLIT

            # Get seeds
            seeds = self.findSeedsLeaf(node)

            # Check if seeds were found
            if seeds == None:
                return 0 # THIS MEANS NO SEEDS WERE FOUND
        
            # Get parent
            parent = node.getParent()

            # Assign current nodes objects to placeholder
            objects = node.getObjects()
            seed0 = objects[seeds[0]]
            seed1 = objects[seeds[1]]

            # Remove seeds from placeholder
            objects.pop(seeds[0])
            objects.pop(seeds[1])


            # Clear the current nodes objects
            node.purgeObjects()

            # Assign seeds
            node.setObjects({seeds[0]:seed0})

            
            # Create new node and add to parent
            newNode = Node(seeds[1][0], seeds[1][1], objects={seeds[1]:seed1}, parent=parent)
            parent.setChildren(newNode)

            # Assign remaining objects based on least enlargement
            for item in objects:
                if self.findEnlargement(node,item) > self.findEnlargement(newNode, item):
                    newNode.setObject(objects[item])
                elif self.findEnlargement(node,item) == self.findEnlargement(newNode, item):
                    if node.getArea() > newNode.getArea():
                        newNode.setObject(objects[item])
                    else:
                        node.setObject(objects[item])
                else:
                    node.setObject(objects[item])


        # Check if parent needs a split
        if len(parent.getChildren()) > node.getFanout():
            self.linearSplit(parent)



    # Find enlargement for a given node, return expect size of box
    def findEnlargement(self, node, item):
        x1 = node.getCoords()[0][0]
        y1 = node.getCoords()[0][1]
        x2 = node.getCoords()[1][0]
        y2 = node.getCoords()[1][1]
        
        # Area of rectangle => L*W
        originalArea = node.getArea()

        bL = item[0]
        tR = item[1]
        if bL[0] < x1:    # if object x1 < current x1
            x1 = bL[0]
        if bL[1] < y1:    # if object y1 < current y1
            y1 = bL[1]
        if tR[0] > x2:    # if object x2 > currnet x2
            x2 = tR[0]
        if tR[1] > y2:    # if object y2 > current y2
            y2 = tR[1]
        
        newArea = abs((x2-x1)*(y2-y1))

        # Return area enlargement
        return abs(newArea-originalArea)





    # Insert object into a node
    def Insert(self, object):
        node = self.root
        result = 0
        # Check if object exists
        
        # if object doesn't exist, add to node or make one
        if len(self.root.getChildren()) == 0:
            # Create new leaf node with object 
            newChild = Node(object.getCoords()[0], object.getCoords()[1], fanout=self.fanout, objects={object.getCoords():[object]}, parent=node)
            # Add leaf node to root
            node.setChildren(newChild)
            result = 1
        else:
            # Find leaf node
            node = self.traverseNode(self.root, object)
            # Check if there is a node
            if node != None:
                # Add object to node 
                node.setObject([object])
            
                # Check if node is too big, if so split it
                if len(node.getObjects()) > self.fanout:
                    self.linearSplit(node)

                # Check if node has too many children


        # node = self.traverseNode(self.root, object)

        # self.linearSplit(node)

    # Delete object
    def Delete(self, object):
        # Find the object 
        # Delete it from leaf node 
        # Go up the to change the sizes of parents, until you reach root


        # If leaf is empty, delete it (or below minimum size)
        # If parent of leaf is empty, delete it (or below minimum size)

        node = self.traverseNode(self.root, object)

        node.removeObjects(object)

        parent = None
        while parent.isRoot() == 0:
            parent = node.getParent()
            parent.getCoords()

            node = parent

        





def main():



    # # Initialize R-Tree
    rtree = RTree(0,0,1000,1000, FANOUT)
    

### Insert


    point1 = Point(1,1,1,1,2,3)
    point2 = Point(1,2,1,2,2,3)
    point3 = Point(1,3,1,3,1,1)
    point4 = Point(1,4,1,4,1,1)
    f1Points = [point1,point2,point3,point4]    # List of points

    point1 = Point(2,1,2,1,2,3)
    point2 = Point(2,2,2,2,2,3)
    point3 = Point(2,3,2,3,1,1)
    point4 = Point(2,4,2,4,1,1)
    f2Points = [point1,point2,point3,point4]    # List of points

    point1 = Point(3,1,3,1,2,3)
    point2 = Point(3,2,3,2,2,3)
    point3 = Point(3,3,3,3,1,1)
    point4 = Point(3,4,3,4,1,1)
    f3Points = [point1,point2,point3,point4]    # List of points

    point1 = Point(4,1,4,1,2,3)
    point2 = Point(4,2,4,2,2,3)
    point3 = Point(4,3,4,3,1,1)
    point4 = Point(4,4,4,4,1,1)
    f4Points = [point1,point2,point3,point4]    # List of points

    point1 = Point(5,1,5,1,2,3)
    point2 = Point(5,2,5,2,2,3)
    point3 = Point(5,3,5,3,1,1)
    point4 = Point(5,4,5,4,1,1)
    f5Points = [point1,point2,point3,point4]    # List of points





    f1 = rtree.createObject(f1Points)
    f2 = rtree.createObject(f2Points)
    f3 = rtree.createObject(f3Points)
    f4 = rtree.createObject(f4Points)
    f5 = rtree.createObject(f5Points)



    rtree.Insert(f1)
    rtree.Insert(f2)
    rtree.Insert(f3)
    rtree.Insert(f4)
    rtree.Insert(f5)


    # rtree.traverseNode(rtree,f1)



### Query


### Delete

    rtree.Delete(f1)


    x = 1



    


if __name__ == "__main__":
    # execute only if run as a script
    main()  