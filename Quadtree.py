
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
    def __init__(self, bL, tR, points=[], children=[], root=0): 
        self.points = points
        self.children = children
        self.root = root
        self.bL = bL
        self.tR = tR
    
    # ADD GETTERS/SETTERS
    def setPoint(self, newPoint):
        self.points.append(newPoint)

    
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
        if node.getNumPoints() <= self.maxPoints:
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
        pts = []
       
        # Loop through all points and place them into child
        points = node.getPoints()
        for point in points:
            longitudePoint = point.getLong()    # Longitude (X) of point
            latitudePoint = point.getLat()      # Latitude (Y) of point
            # Check if point is within quadrant
            if longitudePoint >= bottomLeft[0] and longitudePoint <= topRight[0] and latitudePoint >= bottomLeft[1] and latitudePoint <= topRight[1]:
                pts.append(point)
        # Loop through each point in points list
        for pt in pts:
            # While the point is still in the nodes point list
            while pt in points:
                node.points.remove(pt)  # Remove points from point list

        return pts  # Return point list
   

     # Helper (Query): Recursively search current node
    
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
        self.root.setPoint(point)   # Add point to root
        self.subdivide(self.root)   # Subdivide root

                                                         

    # Update existing node
    def Update(self, oldPlan, newPlan):

        # Convert list of Points to list of Point attr
        for i, point in enumerate(oldPlan):
            oldPlan[i] = point.getAll()
    
        # Check if new plan is the same length as the old plan
        if len(oldPlan) == len(newPlan):
            self.sameLengthUpdate(oldPlan, newPlan)         # Same length
        else:
            self.differentLengthUpdate(oldPlan, newPlan)    # Different length
        
        

    
    def sameLengthUpdate(self, oldPlan, newPlan):
       pass
       # same length so need to find the differences for each point

    def differentLengthUpdate(self, oldPlan, newPlan):

        # Change existing points first

        # New plan has more points
        if len(oldPlan) < len(newPlan):
            # Get list of altered points from the new flight plan
            alteredPoints = [point for point in newPlan if point.getAll() not in oldPlan] 
            print(alteredPoints[0].getAll()) # Print
            
            # Add points using insert function

        # New plan has less points
        else:
            alteredPoints = [point for point in oldPlan if point.getAll() not in newPlan] 

            # Find what to delete
                # If point at end, delete
                # If point before, change existing point and change sequence for points after

    def updateExistingPoints(self, oldPlan, newPlan, alteredPoints):
        # Find specific differences in attrs
        # Use getters/setters to change them

        # Double for-loop to find out the exact differences in attr

        # Loop through alteredPoints
        for alteredPoint in alteredPoints:

            # Loop through existing points
            for point in oldPlan:

                # Check if alteredPoint is an existing point
                if point.getSequence() == alteredPoint.getSequence():
                    
                    # If x or y is changed, find and delete it, then reinsert
                    if point.getLong() != alteredPoint.getLong() or point.getLat() != alteredPoint.getLat():
                        self.Delete(point)          # Delete old point
                        self.Insert(alteredPoint)   # Add new point
                    
                    # If altitude or time is changed, find and use get/set to change
                    if point.getAlt() != alteredPoint.getAlt():
                        # self.Query(point.getCoords(), point.getCoords())
                        pass 
                    # If sequence changed, change the sequence for all the other points
      
      
  


        # Check if points need to be added to the end
        # if points added before end, the rest of the points need to change their sequence

        # 1. Add points before end
        # 2. Then add points at end (sequence will already be set)

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
    point3 = Point(1,3,1,1,1,1)
    # points = [point1, point2]

    # quadtree.Delete(point1)

    w = quadtree.Query(point1) #  no
    

    quadtree.Insert(point1)
    
    x = quadtree.Query(point1)  # yes

    quadtree.Insert(point2) 

    y = quadtree.Query(point3)  # no
    z = quadtree.Query(point1)  # yes
    zz = quadtree.Query(point2)  # yes


    quadtree.Delete(point1)
    quadtree.Delete(point2)

    y = quadtree.Query(point3)  # no
    z = quadtree.Query(point1)  # yes
    zz = quadtree.Query(point2)  # yes



    # point = Point(1,1,2,3)
    # quadtree.movePoints(quadtree.root.children[0], point)
    # y = quadtree.Query([0,0], [5,5])
    x = 1


    points1 = [point1.getAll(), point2.getAll()]
    points1 = [point1, point2]
    points2 = [point1, Point(1,2,1,2,2,3) , Point(1,1,1,1,1,1)]

    # quadtree.Update(points1, points2)

    # for x in points2:
    #     # print(x)
    #     print(x.getAll())
    #     if x.getAll() not in points:
    #         print(x)
        # alteredPoints = [point for point in newPlan if point.getAll() not in oldPlan] 

    # xx = [x for x in points2 if x.getAll() not in points1] 
    # print(xx[0].getAll())





  


    # print(point2.getAll() == xx.getAll()) 
    # print(point2.getAll() is xx.getAll()) 

    


if __name__ == "__main__":
    # execute only if run as a script
    main()  