
# Class for point in Quadtree
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

    def getAll(self):
        return [self.id, self.sequence, self.longitude, self.latitude, self.altitude, self.time]
    
    def getCoords(self):
        return [self.longitude, self.latitude]

    def setID(self, identification):
        self.id = identification
    
    def setSequence(self, sequence):
        self.sequence = sequence
    
    def setLong(self, longitude):
        self.longitude = longitude
    
    def setLat(self, latitude):
        self.latitude = latitude
    
    def setAlt(self, altitude):
        self.altitude = altitude

    def setTime(self, time):
        self.time = time


# Class for node in Quadtree
    # Node can two types - Internal or Leaf 
        # Internal Node - Has 4 children, cannot have a point
        # Leaf Node - No children, can have a point
    # Node can switch between types
    # Node can only store points with same coords
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
        self.points = []
     
    def purgeChildren(self):
        self.children = []

    def removePoint(self, point):
        key = (point.getLong(), point.getLat())
        self.points[key].remove(point)

        if len(self.points[key]) == 0:
            self.points.pop(key)
    
    def isRoot(self):
        return self.root



# Class for Quadtree
class Quadtree:
    # Give initial size of Quadtree
    # Creates root node
    def __init__(self, latitude1, longitude1, latitude2, longitude2, maxPoints): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.maxPoints = maxPoints # Max points before decomposition
        self.root = Node(bL, tR, root = 1) # Create root node

    ############# BODY METHODS #################


    # Helper (Insert): Subdivide nodes into 4 children                 
    def subdivide(self, node):
        # Check if the nodes points is less than the max points
        if node.getNumPoints() <= self.maxPoints and len(node.getChildren()) == 0:
            return

        # Get corners for each quadrant 
        nodeCoords = node.getCoords()   # Root node coords
        bL = nodeCoords[0]              # Bottom left coords
        tR = nodeCoords[1]              # Top right coords
        midH = (tR[1] - bL[1]) / 2      # Mid height
        midL = (tR[0] - bL[0]) / 2      # Mid length

        # Setting children coords
        p = self.movePoints([bL[0], midH], [midL, tR[1]], node )        # Get points within child node    
        one = Node( [bL[0], midH], [midL, tR[1]], p, parent = node )    # Create child node with points
        self.subdivide(one)                                             # Recursively subdivide

        p = self.movePoints([midL, midH],tR, node)        
        two = Node( [midL, midH],tR, p, parent = node )
        self.subdivide(two)

        p = self.movePoints(bL, [midL, midH], node )
        three = Node( bL, [midL, midH], p, parent = node )
        self.subdivide(three)

        p = self.movePoints([midL, bL[1]], [tR[0], midH], node )
        four = Node( [midL, bL[1]], [tR[0], midH], p, parent = node )
        self.subdivide(four)


        # List of children
        node.setChildren([one, two, three, four])

    # Helper (subdivide): From a list of points return all points within boundary
    def movePoints(self, bottomLeft, topRight, node):
        
        pts = {}
       
        # Loop through all points and place them into child
        points = node.getPoints()
        for key, value in points.items():
            longitudePoint = key[0]    # Longitude (X) of point
            latitudePoint = key[1]      # Latitude (Y) of point
            # Check if point is within quadrant
            if longitudePoint >= bottomLeft[0] and longitudePoint <= topRight[0] and latitudePoint >= bottomLeft[1] and latitudePoint <= topRight[1]:
                pts[key] = value
        
        if pts != {}:
            # Create dic of points that are not in pts
            remainingPoints =  {k: v for k, v in points.items() if k not in pts}
            # Set as new points for node
            node.setPoints(remainingPoints)

              
        return pts  # Return point list







     # Helper (Query): Recursively search current node
    
    # Traverse tree to find node with given point
    def traverseNode(self, node, point):
        result = None
        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0 or len(node.getChildren()) <= 0 and point not in node.getPoints():
            return  # Return None

        # Loop through all children of current node
        for child in node.getChildren():
            longitudePoint = point.getLong()    # Longitude (X) of point
            latitudePoint = point.getLat()      # Latitude (Y) of point
            bottomLeft = child.getCoords()[0]     # Bottom left coords of node
            topRight = child.getCoords()[1]       # Top right coords of node

            # Check if point is within child
            if longitudePoint >= bottomLeft[0] and longitudePoint <= topRight[0] and latitudePoint >= bottomLeft[1] and latitudePoint <= topRight[1]:
                # Check if child has children
                if len(child.getChildren()) == 0:
                    return child    # Return node
                else:
                    result = self.traverseNode(child, point)  # Recurse method again with child node

        return result # Return node
    
    # From a list containing Points, return the given point
    def pointFromList(self, pointList, point):
        result = None
        # Loop through all the points in the pointList
        for existingPoint in pointList:
            # Check if point == existingPoint
            if existingPoint.getAll() == point.getAll():
                result = existingPoint
    
        return result   # Point

    # Helper (Delete): Recursively delete levels upwards if level is filled with leaf nodes
    def purgeLevel(self, node):
        # Get parent of node
        parent = node.getParent()
        # Bool to check if children should be purged
        purgeChildren = True

        # If node is root then return
        if node.isRoot():
            return

        # Check if current node is leaf node as well as neighbouring nodes
        for child in parent.getChildren():
            # Check if child has a point or children
            if len(child.getChildren()) > 0 or child.getNumPoints() > 0:
                purgeChildren = False

        # If no children has points or children, delete all children
        if purgeChildren:
            # Purge children 
            parent.purgeChildren()
            # Recurse method
            self.purgeLevel(parent)



    #### MAIN FUNCTIONALITIES ####

    # Insert a point into a node
    def Insert(self, point):

        # Initialize node as root
        node = self.root

        # Check if point is already in tree
        if self.Query(point) != None:
            print("Insert Failed: Point: ", point.getAll(), " already exists")
            return

        

        # Check if root node has children, else find node to add point
        if len(node.getChildren()) == 0:
            node.setPoint(point)   # Add point to root
        else:
            node = self.traverseNode(node, point)   # Find node suitable to add point
            node.setPoint(point)                    # Add point to node

        self.subdivide(node)   # Subdivide node



        # Print confirmations
        # Find node that the point was just added to
        if node != self.root:
            node = self.traverseNode(self.root, point)
        
        # Check if point is actually in node
        if node.getNumPoints() != 0 and point in node.getPoints()[(point.getLong(), point.getLat())] or node == self.root and node.getNumPoints !=0 :
            print("Insert Successful: Point:", point.getAll(), "located in Node:", node.getCoords())
        else:
            print("Insert Unsuccessful")    



    # Search for number of points in area
    def Query(self, point, allPoints = False):        
        result = None   # Initialize result
        node = self.root
        key = (point.getLong(), point.getLat()) # Key for dictionary with list of points

        # Check if point exists in root
        if key in node.getPoints():
            # Get point roots pointsList
            result = self.pointFromList(node.getPoints()[key],point)

        # Search children recursively
        if result == None:
            node = self.traverseNode(node, point)   # Do a resursive search and return result of points found    
            
        # Check if a node exists with point
        if node != None:
            # Check if all points of same coords are wanted or just a single point
            if allPoints == True:
                result = node.getPoints()
            elif key in node.getPoints():
                result = self.pointFromList(node.getPoints()[key],point)
    

        # Print confirmations
        if result == None:
            print("Query Failed: Point: ", point.getAll(), " does not exist!")
        elif allPoints == True:
            print("Query Successful: Points with (X,Y) = ", key, "located in Node: ", node.getCoords())
        else:
            print("Query Successful: Point: ", result.getAll(), "located in Node: ", node.getCoords())


        
        return result   # Point or list of points with same Long, Lat



    # Delete an existing node
    def Delete(self, point):

        result = None   # Initialize result
        node = self.root
        key = (point.getLong(), point.getLat()) # Key for dictionary with list of points

        # Check if point exists in root
        if key in node.getPoints() and len(node.getPoints()) > 0: 
            # Get point roots pointsList
            pointDelete = self.pointFromList(node.getPoints()[key],point)
            # Remove point
            node.removePoint(pointDelete)
            result = "Delete Successful: Point: {0} deleted from Node: {1}".format(point.getAll(), node.getCoords())    # Print statement            
        else:
            # Search children recursively
            node = self.traverseNode(node, point)   # Do a resursive search and return result of points found 
            
            # Check if the was a node found that contained point
            if node == None:
                result = "Delete Failed: Point: {0} does not exist!".format(point.getAll()) # Print statement

            else:
                # Check if point exists in list of nodes points
                pointDelete = self.pointFromList(node.getPoints()[key],point)
                # Print statements
                if pointDelete == None:
                    result = "Delete Failed: Point: {0} does not exist!".format(point.getAll()) # Print statement
                else:
                    # Remove point
                    node.removePoint(pointDelete)
                    # Recursively purge levels
                    self.purgeLevel(node)
                    result = "Delete Successful: Point: {0} deleted from Node: {1}".format(point.getAll(), node.getCoords())    # Print statement
                        
        # Print confirmations
        print(result)



    # Update existing node
    def Update(self, existingPoint, editedPoint):

        existingPoint = self.Query(existingPoint)

        if existingPoint == None:
            print("Update Failed: Point to update does not exist")
            return 
        elif existingPoint.getAll() == editedPoint.getAll():
            print("Update Failed: Updates do not change the select point")
            return
        else:
            # Delete existing point
            self.Delete(existingPoint)
            # Reinsert edited point
            self.Insert(editedPoint)
            x= 1
    


   



############################################################

def main():


    try:
        print(x)
    except:
        pass




    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10, 1)
    
    point1 = Point(1,1,1,1,2,3)
    point2 = Point(1,2,1,2,2,3)
    point3 = Point(1,3,1,3,1,1)
    point4 = Point(1,4,1,1,1,1)

### Query
    # quadtree.Insert(point1)     # Insert point1
    # quadtree.Query(point1, 1)   # Query point at root
    # quadtree.Query(point2, 1)   # Query point that doesn't exist
    # quadtree.Query(point1)      # Query point in children
    # quadtree.Query(point2)      # Query point in children

    # quadtree.Insert(point2)     # Insert point2
    # quadtree.Insert(point3)     # Insert point3
    # quadtree.Insert(point4)     # Insert point4

    # quadtree.Query(point1, 1)   # Query point in children
    # quadtree.Query(point1)      # Query point in children

### Delete
    # quadtree.Insert(point1)     # Insert point1
    # quadtree.Delete(point1)   # Query point at root
    # quadtree.Delete(point2)   # Query point that doesn't exist
    # quadtree.Delete(point1)      # Query point in children
    # quadtree.Delete(point2)      # Query point in children

    # quadtree.Insert(point2)     # Insert point2
    # quadtree.Insert(point3)     # Insert point3
    # quadtree.Insert(point4)     # Insert point4

    # quadtree.Delete(point1)   # Query point in children
    # quadtree.Delete(point1)      # Query point in children

    # quadtree.Insert(point1)
    # quadtree.Delete(point2)     # Insert point2
    # quadtree.Delete(point3)     # Insert point3
    # quadtree.Delete(point4)     # Insert point4
    # quadtree.Delete(point1)      # Query point in children

### Update

    quadtree.Insert(point1)         # Insert point1
    
    quadtree.Update(point1, point2) # Make point1 into point2
    quadtree.Update(point2, point2) # Make point2 into point2

    quadtree.Insert(point1)
    quadtree.Insert(point2)
    # quadtree.Insert(point3)

    quadtree.Update(point2, point3) # 
    # quadtree.Update(point1, point2) # yes
    # quadtree.Update(point2, point1) # yes
    # quadtree.Update(point3, point2) # no
    quadtree.Update(point3, point3) # 


    x = 1



############################################### old testing

    # # points = [point1, point2]

    # # quadtree.Delete(point1)

    # w = quadtree.Query(point1) #  no
    

    # quadtree.Insert(point1)
    
    # x = quadtree.Query(point1)  # yes

    # quadtree.Insert(point2) 

    # y = quadtree.Query(point3)  # no
    # z = quadtree.Query(point1)  # yes
    # zz = quadtree.Query(point2)  # yes


    # quadtree.Delete(point1)
    # quadtree.Delete(point2)

    # y = quadtree.Query(point3)  # no
    # z = quadtree.Query(point1)  # no
    # zz = quadtree.Query(point2)  # no


    # quadtree.Insert(point1)
    # quadtree.Insert(point2)
    # # quadtree.Insert(point3)

    # quadtree.Update(point2, point3) # 
    # # quadtree.Update(point1, point2) # yes
    # # quadtree.Update(point2, point1) # yes
    # # quadtree.Update(point3, point2) # no
    # quadtree.Update(point3, point3) # 


    # # point = Point(1,1,2,3)
    # # quadtree.movePoints(quadtree.root.children[0], point)
    # # y = quadtree.Query([0,0], [5,5])
    # x = 1


    # # points1 = [point1.getAll(), point2.getAll()]
    # # points1 = [point1, point2]
    # # points2 = [point1, Point(1,2,1,2,2,3) , Point(1,1,1,1,1,1)]

    # # quadtree.Update(points1, points2)

    # # for x in points2:
    # #     # print(x)
    # #     print(x.getAll())
    # #     if x.getAll() not in points:
    # #         print(x)
    #     # alteredPoints = [point for point in newPlan if point.getAll() not in oldPlan] 

    # # xx = [x for x in points2 if x.getAll() not in points1] 
    # # print(xx[0].getAll())





  


    # # print(point2.getAll() == xx.getAll()) 
    # # print(point2.getAll() is xx.getAll()) 

    


if __name__ == "__main__":
    # execute only if run as a script
    main()  