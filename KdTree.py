import datetime
import Custom_Exception


# Main Kd-Tree file containing classes: KdTree, Point and Node


# Class for point in KdTree
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

# Class for node in KdTree. Contains Leaf nodes or Points
class Node:
    # New nodes will be type Leaf and store no points
    def __init__(self, bL, tR, splitAxis, points={}, children={}, root=0, parent = None): 
        self.points = points
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR
        self.parent = parent
        self.splitAxis = splitAxis


    def getParentSplitAxis(self):
        return self.getParent().getSplitAxis()

    def getSplitAxis(self):
        return self.splitAxis

    def setRoot(self, root):
        self.root = root 


    def getNumPoints(self):
        return len(self.points)

    def getCoords(self):
               pass


    def setCoords(self):
               pass


    def getPoints(self):
        return self.points
    
    def getParent(self):
        return self.parent


    def setChildren(self, child):
        pass
        

    def getChildren(self):
        return self.children


    def setParent(self, parent):
        self.parent = parent

    def purgePoints(self):
        self.points = {}
     
    def purgeChildren(self):
        self.children = {}

  

    
    def isRoot(self):
        return self.root




# Class for KdTree
class KdTree:
    # Give initial size of KdTree
    # Creates root node
    def __init__(self, startingSplit=1): # 1 = X-Axis, 0 = Y-Axis
        # bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        # tR = [longitude2, latitude2] # Top right corner (X,Y)

        # self.root = Node(bL, tR, root = 1) # Create root node
        self.root = None
        self.startingSplit = startingSplit



    def getStartingSplit(self):
        return self.startingSplit
 

    # Traverse tree to find node with given points
    def traverseNode(self, node, points):

        # Compare alternating axis
        # Traverse till reach leaf node



        result = None

        if node.isRoot() and len(node.getChildren()) == 0:
            return node

        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0 or len(node.getChildren()) <= 0 and points not in node.getPoints():
            return  # Return None

        # Loop through all children of current node
        for child in node.getChildren().values():
            bottomLeftObject = points.getCoords()[0]
            topRightObject = points.getCoords()[1]
            bottomLeftNode = child.getCoords()[0]     # Bottom left coords of node
            topRightNode = child.getCoords()[1]       # Top right coords of node

            # Check if point is within child
            if bottomLeftNode[0] <= bottomLeftObject[0] and bottomLeftNode[1] <= bottomLeftObject[1] and topRightNode[0] >= topRightObject[0] and topRightNode[1] >= topRightObject[1]:
                # Check if child has children
                if len(child.getChildren()) == 0:
                    return child    # Return node
                else:
                    result = self.traverseNode(child, points)  # Recurse method again with child node
        
        return result # Return node





    # Insert points into a node
    def Insert(self, points):
        # Inserting inital point
        if self.root == None:
            self.root = Node(points.getCoords()[0], points.getCoords()[1], self.startingSplit)
        # Inserting new points after root 
        else:
            # Traverse node and return node
            # Add point to node
            pass 
    # Delete points
    def Delete(self, points):
        pass
       

    # Query points and return node with that points
    def Query(self, points):
        pass




def main():



    # # Initialize KdTree
    kdtree = KdTree()
    

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







    # kdtree.Insert(f1)
    # kdtree.Insert(f2)
    # kdtree.Insert(f3)
    # kdtree.Insert(f4)
    # kdtree.Insert(f5)


    # kdtree.traverseNode(kdtree,f1)

### Query

    # Query something existing, should return points
    # one = kdtree.Query(f1)
    # two = kdtree.Query(f2)
    # three = kdtree.Query(f3)
    # four = kdtree.Query(f4)
    # five = kdtree.Query(f5)




### Delete

    # kdtree.Delete(f1)
    # kdtree.Delete(f5)
    # kdtree.Delete(f2)
    # kdtree.Delete(f4)
    # kdtree.Delete(f3)


### Query

    # Query something that doesn't exist, should return 0
    # one = kdtree.Query(f1)
    # two = kdtree.Query(f2)
    # three = kdtree.Query(f3)
    # four = kdtree.Query(f4)
    # five = kdtree.Query(f5)




    x = 1



    


if __name__ == "__main__":
    # execute only if run as a script
    main()  