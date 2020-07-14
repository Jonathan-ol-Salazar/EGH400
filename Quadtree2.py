
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
                       
    def subdivide(self, node):
        if node.getNumPoints() <= self.maxPoints:
            return

        # Get corners for each quadrant 
        nodeCoords = node.getCoords()  # Root node coords
        bL = nodeCoords[0]                  # Bottom left coords
        tR = nodeCoords[1]                  # Top right coords
        midH = (tR[1] - bL[1]) / 2          # Mid height
        midL = (tR[0] - bL[0]) / 2          # Mid length

        # Setting children coords
        p = self.movePoints([bL[0], midH], [midL, tR[1]], node )
        one = Node( [bL[0], midH], [midL, tR[1]], p )
        self.subdivide(one)

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

    # From a list of points return all points within quadrant
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

        for pt in pts:
            while pt in points:
                node.points.remove(pt)

        return pts
   
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
        # From the given area
        # Check if given node has children
        # if it has children, check within coords
        # if in coords, check for points
        # if it has points, add to list
        # else recurse again 
        pts = []
        return self.recursiveSearch(self.root, bottomLeft, topRight, pts)
        

    # ADD GETTERS/SETTERS

    def recursiveSearch(self, node, bottomLeftSearch, topRightSearch, ptsOld):
        if len(node.getChildren()) <= 0 and len(node.getPoints()) <= 0:
            return

        pts = []            # Initialise new list of points
        if len(ptsOld) > 0:
            pts.extend(ptsOld)  # Add previous list of points to new list

        # [bottomLeftNode, topRightNode] = node.getCoords()

        for child in node.getChildren():
            [bottomLeftNode, topRightNode] = child.getCoords()
            # if bottomLeft (x and y) are >= to boundaries AND topright (x and y) are <= boundaries (topRight)
            # if bottomLeftNode[0] >= bottomLeftSearch[0] and bottomLeftNode[1] >= bottomLeftSearch[1] and topRightNode[0] <= topRightSearch[0] and topRightNode[1] <= topRightSearch[1]:
            if bottomLeftNode[0] >= bottomLeftSearch[0] and bottomLeftNode[1] >= bottomLeftSearch[1] and topRightNode[0] <= topRightSearch[0] and topRightNode[1] <= topRightSearch[1]:
                if len(child.getPoints()) > 0:
                    pts.extend(child.getPoints())
                else:
                    traversePoints = self.recursiveSearch(child, bottomLeftSearch, topRightSearch, pts)
                    if traversePoints != None:
                        pts.extend(traversePoints)
               
                 

        return pts
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