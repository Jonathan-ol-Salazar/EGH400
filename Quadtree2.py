
# Class for point in Quadtree
class Point:
    def __init__(self, longitude, latitude, altitude, time): # long = x, lat = y
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.time = time
    
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
    def addPoint(self, newPoint):
        self.points.append(newPoint)

    
    def getNumPoints(self):
        return self.points

    def getCoords(self):
        return self.bL, self.tR

    def getPoints(self):
        return self.points

    def setChildren(self, children):
        self.children.append(children)






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
    def Insert(self, point):
        # Create a point object
        # point = Point(longitude,latitude, altitude, time)

        # # Add point to tree
        # self.root.addPoint(point)

        # ROOT NODE

        # If the root node has no children, add point
        if len(self.root.children) == 0:
            self.root.addPoint(point)
        # else traverse through tree to find suitable node
        # else create a new node 

        # Check if root node has max points
        if self.maxPoints <= self.root.getNumPoints():
            # Get corners for each quadrant 
            rootCoords = self.root.getCoords()  # Root node coords
            bL = rootCoords[0]                  # Bottom left coords
            tR = rootCoords[1]                  # Top right coords
            midH = (tR[1] - bL[1]) / 2          # Mid height
            midL = (tR[0] - bL[0]) / 2          # Mid length

            # Setting children coords
            one = Node( [bL[0], midH],[midL, tR[1]])
            two = Node([midL, midH],tR)
            three = Node(bL,[midL, midH])
            four = Node([midL, bL[1]],[tR[0], midH])

            # List of children
            children = [one, two, three, four]

            # Add list of new children to root
            self.root.setChildren(children)
                        
            # Move existing points to suitable children
            points = self.root.getPoints()
                
                # loop through all points and place into new children
                # for point in points:
                
            

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

    quadtree.Insert(1,1,2,3)

    x = 1
if __name__ == "__main__":
    # execute only if run as a script
    main()  