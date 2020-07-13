
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
        self.children.append(children)

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
        

    # Insert a point into a node
        # Traverse till a node is found, otherwise create a new one
    def Insert(self, Point):
        self.root.setPoint(Point)
        self.subdivide(self.root)

        # ROOT NODE

        # # If the root node has no children, add point
        # if len(self.root.children) == 0:
        #     self.root.setPoint(Point)
        # # else traverse through tree to find suitable node
        # # else create a new node 
        # else:
        #     self.subdivide(self.root)
        # # Check if root node has max points
        # if self.maxPoints <= self.root.getNumPoints():
        #     # Get corners for each quadrant 
        #     rootCoords = self.root.getCoords()  # Root node coords
        #     bL = rootCoords[0]                  # Bottom left coords
        #     tR = rootCoords[1]                  # Top right coords
        #     midH = (tR[1] - bL[1]) / 2          # Mid height
        #     midL = (tR[0] - bL[0]) / 2          # Mid length

        #     # Setting children coords
        #     one = Node( [bL[0], midH],[midL, tR[1]])
        #     two = Node([midL, midH],tR)
        #     three = Node(bL,[midL, midH])
        #     four = Node([midL, bL[1]],[tR[0], midH])

        #     # List of children
        #     children = [one, two, three, four]

        #     points = self.root.getPoints()
        #     # Remove children from root
        #     self.root.purgePoints()

        #     # # Loop through all children and place points
        #     # for child in children:
        #     #     pointsToAdd = self.movePoints(child, points )
        #     #     if len(pointsToAdd) != 0:
        #     #         for point in pointsToAdd:
        #     #             child.setPoint(point)
                
 

        #     # Add list of new children to root
        #     self.root.setChildren(children)
                        
        #TODO remove points from root
        #TODO find out why adding to children also adds to root
                
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
        Node.children = [one, two, three, four]

        # points = self.root.getPoints()
        # # Remove children from root
        # self.root.purgePoints()
        
        # # Loop through all children and place points
        # for child in children:
        #     pointsToAdd = self.movePoints(child, points )
        #     if len(pointsToAdd) != 0:
        #         for point in pointsToAdd:
        #             child.setPoint(point)




    # From a list of points return all points within quadrant
    def movePoints(self, bottomLeft, topRight, node):
        pts = []
        # coords = Node.getCoords()  # Coordinates of child node
        # bottomLeft = coords[0]      # Bottom left coords
        # topRight = coords[1]        # Top right coords

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
   



                


                
            

    # Update existing node
    def Update(self):
        pass

    # Delete an existing node
    def Delete(self):
        pass

    # ADD GETTERS/SETTERS



    def createChildren(self, bL, tR, points):
        pass 
        

    # Split node into 4 new nodes
        # Move points to corresponding nodes
        # Find node object to place children
    def decompose(self):
        pass 






############################################################

def main():

    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10, 1)
    
    point1 = Point(1,1,2,3)
    point2 = Point(1,2,2,3)

    points = [point1, point2]

    quadtree.Insert(point1)
    quadtree.Insert(point2)



    # point = Point(1,1,2,3)
    # quadtree.movePoints(quadtree.root.children[0], point)

    x = 1
if __name__ == "__main__":
    # execute only if run as a script
    main()  