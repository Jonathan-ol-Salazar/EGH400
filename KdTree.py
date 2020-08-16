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
        return (self.longitude, self.latitude)

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
    def __init__(self, longitude, latitude, splitAxis, points={}, children={}, leftChild = None, rightChild = None, root=0, parent = None): 
        self.points = points
        self.children = children
        self.root = root
        self.longitude = longitude 
        self.latitude = latitude
        self.parent = parent
        self.splitAxis = splitAxis  # 1 = X-Axis, 0 = Y-Axis
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setChild(self, child):
        # Get split axis
        # Check childs relevant axis
        # Set corresponding child location

        # Get childs split axis
        if self.splitAxis == 1:
            childAxis = child.getLong()
            nodeAxis = self.getLong()
        elif self.splitAxis == 0:
            childAxis = child.getLat()
            nodeAxis = self.getLat()

        else:
            return 0 # Insert Failed

        # Compare nodeAxis with relevant child axis 
        if nodeAxis > childAxis:
            if self.leftChild != None:
                return 0 # Insert Failed
            self.leftChild = child  # Child is put in the left branch because it's smaller
        elif nodeAxis <= childAxis:
            if self.rightChild != None:
                return 0 # Insert Failed
            self.rightChild = child
        
        return 1    # Insert Successful


    def getLong(self):
        return self.longitude
    
    def getLat(self):
        return self.latitude

    def getParentSplitAxis(self):
        return self.getParent().getSplitAxis()

    def getChildSplitAxis(self):
        if self.splitAxis == 1: # If current split is X-Axis, child is Y-Axis
            return 0
        elif self.splitAxis == 0: # If current split is Y-Axis, child is X-Axis
            return 1
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

    def __init__(self, startingSplit=1): # 1 = X-Axis, 0 = Y-Axis

        self.root = None
        self.startingSplit = startingSplit



    def getStartingSplit(self):
        return self.startingSplit
 

    # Traverse tree to find node with given points
    def traverseNode(self, node, point):

        # Compare alternating axis
        # Traverse till reach leaf node

        # Compare with current nodes axis split, decide left or right
            # if no child to put in, make new child, return child
            # get child recurse method, 

        # Functions used for:
            # Insert -> return node to add child to
                # node will be the parent of the new point
               

            # Delete -> return node with same input coords 
            # Query -> return node with same input coords 


        # Puesdo Code

            # before proceeding next section of tree, check if there is a child there, if not return parent
            # Did axis check and want to go left
            # Check if current node has left child 
            # If not, return parent to add child
            # else, select left child and recurse


   

        if node.isRoot() and len(node.getChildren()) == 0:
            return node

        # Check split axis of point and compare with current node
        splitAxis = node.getSplitAxis()
        leftChild = node.getLeftChild()
        rightChild = node.getRightChild()


        # Get childs split axis
        if splitAxis == 1:         # 1 = X-Axis split
            childAxis = point.getLong()    # Get child x
            nodeAxis = node.getLong()
        elif splitAxis == 0:       # 0 = Y-Axis split 
            childAxis = point.getLat()    # Get child y
            nodeAxis = node.getLat()
        else:
            return None                    # Failed    

        # Compare nodeAxis with relevant child axis 
        if nodeAxis > childAxis:
            if leftChild == None:   # Check if left child is empty
                return              # Return this node, point to be added to it  
            elif leftChild.getCoords() == point.getCoords():
                return leftChild    # Return this node, delete or query for this node 
            else:
                self.traverseNode(leftChild, point)  # Recurse with left node          
        elif nodeAxis <= childAxis:
            if rightChild == None:  # Check if right child is empty
                return              # Return this node, point to be added to it  
            elif rightChild.getCoords() == point.getCoords():
                return rightChild    # Return this node, delete or query for this node 
            else:
                self.traverseNode(rightChild, point)  # Recurse with left node          
        
        return None   # Insert Failed




        # # Return if node has no children or points
        # if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0 or len(node.getChildren()) <= 0 and points not in node.getPoints():
        #     return  # Return None

        # # Loop through all children of current node
        # for child in node.getChildren().values():
        #     bottomLeftObject = points.getCoords()[0]
        #     topRightObject = points.getCoords()[1]
        #     bottomLeftNode = child.getCoords()[0]     # Bottom left coords of node
        #     topRightNode = child.getCoords()[1]       # Top right coords of node

        #     # Check if point is within child
        #     if bottomLeftNode[0] <= bottomLeftObject[0] and bottomLeftNode[1] <= bottomLeftObject[1] and topRightNode[0] >= topRightObject[0] and topRightNode[1] >= topRightObject[1]:
        #         # Check if child has children
        #         if len(child.getChildren()) == 0:
        #             return child    # Return node
        #         else:
        #             result = self.traverseNode(child, points)  # Recurse method again with child node
        
        # return result # Return node





    # Insert points into a node
    def Insert(self, point):
        # Get point coords
        pointLong = point.getCoords()[0]    # Point Long
        pointLat = point.getCoords()[1]     # Point Lat 

        # Inserting inital point
        if self.root == None:
            self.root = Node(point.getCoords()[0], point.getCoords()[1], self.startingSplit, points={(pointLong, pointLat):[point]}, root=1)
            return self.root    # Return root 
        
        # Inserting new points after root 
        else:
            # Traverse node and return node
            # Add point to node

            # Find node to add point to
            node = self.traverseNode(self.root, point)
            
            if node != None:                               
                # Make a new node and add point to it
                newChild = Node(pointLong, pointLat, node.getChildSplitAxis(), points={(pointLong, pointLat):[point]})
                # Add new node to parent found
                node.setChild(newChild)
                return node # Return node

        return None # Failure to Insert

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

    # Dummy points from GeeksforGeeks site on KDTree
        # (3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)
    point1 = Point(1,1,3,6,2,3)
    point2 = Point(1,2,17,15,2,3)
    point3 = Point(1,3,13,15,1,1)
    point4 = Point(1,4,6,12,1,1)
    point5 = Point(1,5,9,1,2,3)
    point6 = Point(1,6,2,7,1,1)
    point7 = Point(1,7,10,19,1,1)
    f1Points = [point1,point2,point3,point4,point5,point6,point7]    # List of points


    for point in f1Points:
        kdtree.Insert(point)


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