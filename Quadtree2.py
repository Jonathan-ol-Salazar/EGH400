
# Class for point in Quadtree
class Point:
    def __init__(self, longitude, latitude, altitude, time): # long = x, lat = y
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.time = time

    def getLong(self):
        return self.longitude

    def getLat(self):
        return self.latitude
    

    
    # Add GETTERS/SETTERS

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

    # Helper (subdivide): From a list of points return all points within quadrant
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
   
    # Insert a point into a node
        # Traverse till a node is found, otherwise create a new one
    def Insert(self, Point):
        self.root.setPoint(Point)
        self.subdivide(self.root)

    # Update existing node
    def Update(self):
        pass

    # Delete an existing node
    def Delete(self):
        pass


    # Search for number of points in area
    def Query(self, bottomLeft, topRight):
        pts = []
        return self.recursiveSearch(self.root, bottomLeft, topRight, pts)      

    # Helper (Query): Recursively search current node
    def recursiveSearch(self, node, bottomLeftSearch, topRightSearch, ptsOld):
        # Return if node has no children or points
        if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0:
            return

        pts = []                # Initialise new list of points
        if len(ptsOld) > 0:     # Check if previous points has a point
            pts.extend(ptsOld)  # Add previous list of points to new list

        # Loop through each child
        for child in node.getChildren():
            # Get child coords
            [bottomLeftNode, topRightNode] = child.getCoords()
            # Check if child coords is within search area
            if bottomLeftNode[0] >= bottomLeftSearch[0] and bottomLeftNode[1] >= bottomLeftSearch[1] and topRightNode[0] <= topRightSearch[0] and topRightNode[1] <= topRightSearch[1]:
                # If child has points, add to list
                if len(child.getPoints()) > 0:
                    pts.extend(child.getPoints())   # Add points
                else:
                    # Recurse the search with current child
                    traversePoints = self.recursiveSearch(child, bottomLeftSearch, topRightSearch, pts)
                    # If recurse doesn't return None, add to list. This is because it will return points
                    if traversePoints != None:
                        pts.extend(traversePoints)  # Add points
               
        return pts # Return list of points 



############################################################

def main():

    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10, 1)
    
    point1 = Point(1,1,2,3)
    point2 = Point(1,2,2,3)

    points = [point1, point2]

    quadtree.Insert(point1)
    quadtree.Insert(point2)
    y = quadtree.Query([0,0], [5,5])


    # point = Point(1,1,2,3)
    # quadtree.movePoints(quadtree.root.children[0], point)

    x = 1
if __name__ == "__main__":
    # execute only if run as a script
    main()  