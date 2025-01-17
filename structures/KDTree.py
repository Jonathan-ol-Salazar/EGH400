import datetime
# from structures import Custom_Exception


# Main Kd-Tree file containing classes: KDTree, Point and Node


# Class for point in KDTree
class Point:
    def __init__(self, identification, sequence, longitude, latitude, altitude, time): # long = x, lat = y
        self.id = identification
        self.sequence = sequence
        self.longitude = self.setLongitudeDirection(longitude)
        self.latitude = self.setLatitudeDirection(latitude)
        self.altitude = altitude
        self.time = time


    def setLongitudeDirection(self, longitude):
        # Longitude is -ve, so it's WEST of Prime Meridian
        if longitude < 0:
            self.longitudeDirection = "W"
            return longitude * -1
        # Longitude is +ve, so it's EAST of Prime Meridian
        self.longitudeDirection = "E"
        return longitude
    
    def setLatitudeDirection(self, latitude):
        # Latitude is -ve, so it's SOUTH of Equator
        if latitude < 0:
            self.latitudeDirection = "S"
            return latitude * -1
        # Latitude is +ve, so it's NORTH of Equator
        self.latitudeDirection = "N"
        return latitude
    
    def getLongitudeDirection(self):
        return self.longitudeDirection

    def getLatitudeDirection(self):
        return self.latitudeDirection

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
        # for attr in attrs:
        #     if self.checkInt(attr) == 1:
        #         allCorrectType = True
        #         break
        
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
        return (self.longitude, self.latitude)

    def setID(self, identification):
        # if self.checkInt(identification) == 1:
        self.id = identification
    
    def setSequence(self, sequence):
        # if self.checkInt(sequence) == 1:
        self.sequence = sequence
    
    def setLong(self, longitude):
        # if self.checkInt(longitude) == 1:
        self.longitude = longitude
    
    def setLat(self, latitude):
        # if self.checkInt(latitude) == 1:
        self.latitude = latitude
    
    def setAlt(self, altitude):
        # if self.checkInt(altitude) == 1:
        self.altitude = altitude

    def setTime(self, time):
        # if self.checkDatetime(time) == 1:
        self.time = time


    # def checkInt(self, input):
    #     try:
    #         if type(input) != int:
    #             raise Custom_Exception.typeNotInt()
    #         else:
    #             return 1 # Passed
    #     except Custom_Exception.typeNotInt():
    #         print("Input must be of type 'int' ")
    #         return 0 # Failed

# Class for node in KDTree. Contains Leaf nodes or Points
class Node:
    # New nodes will be type Leaf and store no points
    def __init__(self, longitude, latitude, splitAxis, points=[], children={}, leftChild = None, rightChild = None, root=0, parent = None, longitudeDirection="", latitudeDirection=""): 
        self.points = points
        # self.children = children // COMMENTED THIS OUT BUT MIGHT NEED IN FUTURE TO REPLACE leftChild/rightChild
        self.root = root
        self.longitude = longitude 
        self.latitude = latitude
        self.parent = parent
        self.splitAxis = splitAxis  # 0 = X-Axis, 1 = Y-Axis
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.longitudeDirection = longitudeDirection
        self.latitudeDirection = latitudeDirection


    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setLeftChild(self, child):
        self.leftChild = child

    def setRightChild(self, child):
        self.rightChild = child

    def setChild(self, child):
        # Get split axis
        # Check childs relevant axis
        # Set corresponding child location

        # Get childs split axis
        if self.splitAxis == 0:
            childAxis = child.getLong()
            nodeAxis = self.getLong()
        elif self.splitAxis == 1:
            childAxis = child.getLat()
            nodeAxis = self.getLat()

        else:
            return 0 # Insert Failed

        # Compare nodeAxis with relevant child axis 
        if nodeAxis > childAxis:
            if self.leftChild != None:
                return 0 # Insert Failed
            # self.leftChild = child  # Child is put in the left branch because it's smaller
            self.setLeftChild(child)
        elif nodeAxis <= childAxis:
            if self.rightChild != None:
                return 0 # Insert Failed
            # self.rightChild = child
            self.setRightChild(child)

        
        return 1    # Insert Successful


    def getLong(self):
        return self.longitude
    
    def getLat(self):
        return self.latitude

    def getParentSplitAxis(self):
        return self.getParent().getSplitAxis()

    def getChildSplitAxis(self):
        if self.splitAxis == 0: # If current split is X-Axis, child is Y-Axis
            return 1
        elif self.splitAxis == 1: # If current split is Y-Axis, child is X-Axis
            return 0
        else:
            return None # Current node does not have a valid split axis


    def getSplitAxis(self):
        return self.splitAxis

    def setRoot(self, root):
        self.root = root 


    def getNumPoints(self):
        return len(self.points)

    def getCoords(self):
        return (self.getLong(), self.getLat())

    # Setting new coords, assuming input is a tuple
    def setCoords(self, newCoords):
        self.longitude = newCoords[0]
        self.latitude = newCoords[1]

    # Replace all points
    def setPoints(self, points):
        self.points = points
    
    # Add a single point
    def setPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points
    
    def getParent(self):
        return self.parent


    def setChildren(self, child):
        pass
        

    def getChildren(self):
        # return self.children
        return (self.getLeftChild(), self.getRightChild())

    def hasChildren(self):
        if self.getLeftChild() != None or self.getRightChild() != None:
            return 1
        
        return 0

    def setParent(self, parent):
        self.parent = parent

    def purgePoints(self):
        self.points = {}
     
    def purgeChildren(self):
        self.children = {}

    def isRoot(self):
        return self.root

    def purgeChild(self, child):
        if self.getLeftChild() == child:
            self.setLeftChild(None)
            return 1
        elif self.getRightChild() == child:
            self.setRightChild(child)
            return 1
        else:
            return 0
            




# Class for KDTree
class KDTree:

    def __init__(self, startingSplit=0): # 0 = X-Axis, 1 = Y-Axis

        self.root = None
        self.startingSplit = startingSplit



    def getStartingSplit(self):
        return self.startingSplit
 

    # Traverse tree to find node where point should be added
    def traverseNode(self, node, point, query = 0):
        result = None

        if node == None:
            return result

        if node.isRoot() and node.hasChildren() == 0:
        # if node.isRoot() and len(node.getChildren()) == 0:
            return node

        # Check if current node shares same coords as point
        if node.getCoords() == point.getCoords():
            return node


        # Check split axis of point and compare with current node
        splitAxis = node.getSplitAxis()
        leftChild = node.getLeftChild()
        rightChild = node.getRightChild()


        # Get childs split axis
        if splitAxis == 0:         # 0 = X-Axis split
            childAxis = point.getLong()    # Get child x
            nodeAxis = node.getLong()
        elif splitAxis == 1:       # 1 = Y-Axis split 
            childAxis = point.getLat()    # Get child y
            nodeAxis = node.getLat()
        else:
            return None                    # Failed    

        # Compare nodeAxis with relevant child axis 
        if nodeAxis > childAxis:
            if leftChild == None:   # Check if left child is empty
                return node              # Return this node, point to be added to it  
            elif leftChild.getCoords() == point.getCoords():
                return leftChild    # Return this node, delete or query for this node 
            else:
                result = self.traverseNode(leftChild, point, query)  # Recurse with left node     
                # # Make resul
                # if result != None:
                #     if result.getCoords() != point.getCoords():
                #         result == None
     
        elif nodeAxis <= childAxis:
            if rightChild == None:  # Check if right child is empty
                return node             # Return this node, point to be added to it  
            elif rightChild.getCoords() == point.getCoords():
                return rightChild    # Return this node, delete or query for this node 
            else:
                result = self.traverseNode(rightChild, point, query)  # Recurse with left node          
                

        
        if query == 1 and result != None:
            if result.getCoords() != point.getCoords():
                return None

        return result   #  Failed
    
    # Traverse tree to find node with the minimum value for a given dimension
    def findMin(self, node, splitAxis, minValueChild):
        # get dimension
        # get value of dimension
        # traverse 

        result = minValueChild

        if node.getRightChild() != None:
            # Compare child coords in splitAxis with current minValue child
            if node.getRightChild().getCoords()[splitAxis] <= result.getCoords()[splitAxis]:
                result = node.getRightChild()
                result = self.findMin(node.getRightChild(), splitAxis, result)


        if node.getLeftChild() != None:
            # Compare child coords in splitAxis with current minValue child
            if node.getLeftChild().getCoords()[splitAxis] <= result.getCoords()[splitAxis]:
                result = node.getLeftChild()
                result = self.findMin(node.getLeftChild(), splitAxis, result)

        
        return result

    # Insert points into a node
    def Insert(self, point):
        # Get point coords
        pointLong = point.getCoords()[0]    # Point Long
        pointLat = point.getCoords()[1]     # Point Lat 
        pointLongDirection = point.getLongitudeDirection()
        pointLatDirection = point.getLatitudeDirection()

        # Inserting inital point
        if self.root == None:
            self.root = Node(pointLong, pointLat, self.startingSplit, points={(pointLong, pointLat):[point]}, root=1, longitudeDirection=pointLongDirection, latitudeDirection=pointLatDirection)
            # return self.root    # Return root 
            return 1
        
        # Inserting new points after root 
        else:
            # Traverse node and return node
            # Add point to node

            # Find node to add point to
            node = self.traverseNode(self.root, point)
            
            if node != None:                               
                # Make a new node and add point to it
                newChild = Node(pointLong, pointLat, node.getChildSplitAxis(), points={(pointLong, pointLat):[point]}, parent=node, longitudeDirection=pointLongDirection, latitudeDirection=pointLatDirection)
                # Add new node to parent found
                node.setChild(newChild)
                # return node # Return 
                return 1

        return None # Failure to Insert

    # Delete points
    def Delete(self, point):
        # find node

        # Check if its a leaf node
        # if it is, easy 
        # if not gluck, go through the if else statments
       

        # Return confirmation of result


        result = 0 # Placeholder for result

        # Find Node to be deleted
        node = self.traverseNode(self.root, point, query=1)

        if node == None:
            return result   # Delete failed
        elif node.hasChildren() == 0:
            node.getParent().purgeChild(node)   # Get node parent and delete child from parents children
            result = 1
        elif node.hasChildren() > 0:
            self.recursiveDelete(node)
            result = 1


        
        return result   # Delete failed


    def recursiveDeleteHelper(self, node, nodeChild):
        splitAxis = node.getSplitAxis() # Splitting axis of node to be deleted 

        # Find minimum node
        minNode = self.findMin(nodeChild, splitAxis, nodeChild)
    
        # Set new coords for node
        node.setCoords(minNode.getCoords())
        # Set new points
        node.setPoints(minNode.getPoints())

        # If minNode is a leaf node
        if minNode.hasChildren() == False:
            # Remove minNode from parent
            minNode.getParent().purgeChild(minNode)
        elif minNode.hasChildren() == True:
            # Recurse method
            self.recursiveDelete(minNode)


    # Recursively delete nodes in tree
    def recursiveDelete(self, node):

        # If there is a right child 
        if node.getRightChild() != None:               
            self.recursiveDeleteHelper(node, node.getRightChild())

        
        # If there is no right child
        elif node.getLeftChild() != None:

            # if node.getLeftChild().hasChildren() == False:
            #     node.setRightChild(node.getLeftChild())
            #     node.setLeftChild(None)
                
            # else:
            self.recursiveDeleteHelper(node, node.getLeftChild())

        if node.hasChildren() == False:
            if node.getParent().getLeftChild() == node:
                node.getParent().setRightChild(node)
                node.getParent().setLeftChild(None)

         

    # Query point and return node with that point

    def Query(self, point):
        node = self.traverseNode(self.root, point)
        
        # Check if a node was found
        if node == None:
            return 0    # Query Failed
        elif node.getCoords() != point.getCoords():
            return 0    # Query Failed
        elif [point] in list(node.points.values()):
            return point # Returning point found from node found
        
        return 0     # Query failed



############################################################

# EXAMPLE USAGE


def main():

    # Initialize KDTree
    kdtree = KDTree()
    



    # Dummy points 1 from GeeksforGeeks site on KDTree
        # (3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)
    point1 = Point(1,1,-3,-6,2,3)
    point2 = Point(1,2,17,15,2,3)
    point3 = Point(1,3,13,15,1,1)
    point4 = Point(1,4,6,12,1,1)
    point5 = Point(1,5,9,1,2,3)
    point6 = Point(1,6,2,7,1,1)
    point7 = Point(1,7,10,19,1,1)
    f1Points = [point1,point2,point3,point4,point5,point6,point7]    # List of points

    # # Dummy points 2 from Marko Berezovský
    # point1 = Point(2,1,30,40,2,3)
    # point2 = Point(2,2,5,25,2,3)
    # point3 = Point(2,3,70,70,1,1)
    # point4 = Point(2,4,10,12,1,1)
    # point5 = Point(2,5,50,30,1,1)
    # point6 = Point(2,6,35,45,1,1)
    # f2Points = [point1,point2,point3,point4,point5,point6]    # List of points


    # INSERT
    for point in f1Points: # Dummy points 1
        kdtree.Insert(point)
   
    # for point in f2Points:  # Dummy points 2
    #     kdtree.Insert(point)


    # QUERY - Return point
    one = kdtree.Query(point1)
    two = kdtree.Query(point2)
    three = kdtree.Query(point3)
    four = kdtree.Query(point4)
    five = kdtree.Query(point5)

    # DELETE -> x = 1(success), 0(failure)
    x = kdtree.Delete(point1)
    x = kdtree.Delete(point2)
    x = kdtree.Delete(point3)
    x = kdtree.Delete(point4)
    x = kdtree.Delete(point5)

    # QUERY - Return 0, for everything except the last point
    one = kdtree.Query(point1)
    two = kdtree.Query(point2)
    three = kdtree.Query(point3)
    four = kdtree.Query(point4)
    five = kdtree.Query(point5) # Should return a point because it is the root

    # Breakpoint variable
    x = 1



    


if __name__ == "__main__":
    # execute only if run as a script
    main()  