
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
    def __init__(self, bL, tR, points={}, children=[], root=0): 
        self.points = points
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR



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

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def purgePoints(self):
        self.points = []
     
    def purgeChildren(self):
        self.children = []

    def removePoint(self, point):
        self.points.remove(point)



# Class for Quadtree
class Quadtree:
    # Give initial size of Quadtree
    # Creates root node
    def __init__(self, latitude1, longitude1, latitude2, longitude2, maxPoints): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.maxPoints = maxPoints # Max points before decomposition
        self.root = Node(bL, tR, root = 1) # Create root node

    # Helper (Insert): Subdivide nodes into 4 children                 
    def subdivide(self, node):
        # Check if the nodes points is less than the max points
        if node.getNumPoints() <= self.maxPoints and len(node.getChildren()) == 0:
            return

        # Get corners for each quadrant 
        nodeCoords = node.getCoords()  # Root node coords
        bL = nodeCoords[0]                  # Bottom left coords
        tR = nodeCoords[1]                  # Top right coords
        midH = (tR[1] - bL[1]) / 2          # Mid height
        midL = (tR[0] - bL[0]) / 2          # Mid length

        # Setting children coords
        p = self.movePoints([bL[0], midH], [midL, tR[1]], node )    # Get points within child node    
        one = Node( [bL[0], midH], [midL, tR[1]], p )               # Create child node with points
        self.subdivide(one)                                         # Recursively subdivide

        p = self.movePoints([midL, midH],tR, node)        
        two = Node( [midL, midH],tR, p )
        self.subdivide(two)

        p = self.movePoints(bL, [midL, midH], node )
        three = Node( bL, [midL, midH], p )
        self.subdivide(three)

        p = self.movePoints([midL, bL[1]], [tR[0], midH], node )
        four = Node( [midL, bL[1]], [tR[0], midH], p )
        self.subdivide(four)


        # List of children
        # node.children = [one, two, three, four]
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
    

    # Find a node
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

        return result # Return point
        
        
 




    def recursiveSearch(self, node, point):
        result = None
        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0 or len(node.getChildren()) <= 0 and point not in node.getPoints():
            return  # Return None

        # Check all children of node if point lies within its boundaries
        # if it does, then recurse method again, using said node
        # check if its got points, if so compare to search node

        # Loop through all children of current node
        for child in node.getChildren():
            longitudePoint = point.getLong()    # Longitude (X) of point
            latitudePoint = point.getLat()      # Latitude (Y) of point
            bottomLeft = child.getCoords()[0]     # Bottom left coords of node
            topRight = child.getCoords()[1]       # Top right coords of node

            # Check if point is within child
            if longitudePoint >= bottomLeft[0] and longitudePoint <= topRight[0] and latitudePoint >= bottomLeft[1] and latitudePoint <= topRight[1]:
                # Check if point is within the childs points 
                if point in child.getPoints():
                    return point    # Return point
                else:
                    result = self.recursiveSearch(child, point)  # Recurse method again with child node
                    # if point == result:
                    #     point = result
            # else:
            #     return  # Return None


        return result # Return point
    
    
    # Search for number of points in area
    def Query(self, point):        
        result = ""
        # Check point exists in root
        if point in self.root.getPoints():
            result = point
        elif len(self.root.getChildren()) == 0:
            result = None 

        # Search children recursively
        if result != None and result != point:
            result = self.recursiveSearch(self.root, point)   # Do a resursive search and return result of points found    

        # Print confirmations
        if result == None:
            print("Point does not exist")
        else:
            print("Point found: ", result.getAll())

        
        return result
        

    def recursiveDelete(self, point, node):
        # Check if node has no points and no children
        if node.getNumPoints() == 0 and len(node.getChildren()) == 0:
            return "Nothing to delete"  # Nothing to delete
            
        # Check if point is in node
        if point in node.getPoints():
            node.removePoint(point) # Remove point from node
            return "Deletion Successful"

        # Bool to check if nodes children should be deleted
        purgeChildren = True    # True if children have no kids or points
        internalNode = False    # True if node has children
        
        # Check if point is in node.point list      
        for child in node.getChildren():
            internalNode = True                 # Node has children
            self.recursiveDelete(point, child)  # Recurse method
            # Check if child has kids or points
            if len(child.getChildren()) > 0 or child.getNumPoints() > 0:
                purgeChildren = False           # Child has kids or points
                
        # Check if bools are true
        if purgeChildren and internalNode:
            node.purgeChildren()    # Delete nodes children

        return "Deletion Successful" # Something was deleted



    # Insert a point into a node
    def Insert(self, point):
        
        node = self.root
        
        if len(self.root.getChildren()) == 0:
            node.setPoint(point)   # Add point to root
        else:
            node = self.traverseNode(self.root, point)
            node.setPoint(point)


        self.subdivide(node)   # Subdivide node

        # # Print confirmations
        # if node.getNumPoints() != 0 and node.getPointCoords() == [point.getLong(), point.getLat()]:
        #     print("Insert Successful: Point:", point.getAll(), "located in Node:", node.getCoords())
        # else:
        #     print("Insert Unsuccessful")    



                                                         

    # Update existing node
    def Update(self, existingPoint, editedPoint):
        
        # Find point to be changed
        # Find difference -> turn to set and find attr difference
        # if different, use get/set to change, return point and print
        # else return point and print statement
        # re-add point if x or y is changed


        existingPoint = self.Query(existingPoint)

        if existingPoint == None:
            print("Update Failed: Point to update does not exist")
            return 
        else:
            # find index of difference, and the value its supposed to be 
            
            reInsert = False

            # loop through each value and check 
            for i, attr in enumerate(editedPoint.getAll()):
                if attr != existingPoint.getAll()[i]:

                    # Switch statement of somesort, via if-statements
                    if i == 0:  # ID
                        existingPoint.setID(attr)
                    elif i == 1: # Sequence
                        existingPoint.setSequence(attr)
                    elif i == 2: # Long
                        existingPoint.setLong(attr)
                        reInsert = True
                    elif i == 3: # Lat
                        existingPoint.setLat(attr)
                        reInsert = True
                    elif i == 4: # Alt
                        existingPoint.setAlt(attr)
                    elif i == 5: # Time
                        existingPoint.setTime(attr)
       
            # If coords are changed, re-insert point
            if reInsert:
                self.Delete(existingPoint)
                self.Insert(existingPoint)


        # Check if edits were successful, with print statements
        if existingPoint.getAll() == editedPoint.getAll():
            print("Update Successful")
        else:
            print("Update Failed")

        return



    # Delete an existing node
    def Delete(self, point):
        # Prints result of deletion
        print(self.recursiveDelete(point, self.root))


   



############################################################

def main():

    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10, 1)
    
    point1 = Point(1,1,1,1,2,3)
    point2 = Point(1,2,1,2,2,3)
    point3 = Point(1,3,1,3,1,1)
    point4 = Point(1,4,1,1,1,1)


    quadtree.Insert(point1)
    quadtree.Insert(point2)
    quadtree.Insert(point3)
    quadtree.Insert(point4)



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