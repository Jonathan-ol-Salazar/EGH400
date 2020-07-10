
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
    
    # ADD GETTERS/SETTERS
    def addPoint(self, newPoints):
        self.points.append(newPoints)

# Class for Quadtree
class Quadtree:
    # Give initial size of Quadtree
    # Creates root node
    def __init__(self, latitude1, longitude1, latitude2, longitude2, maxPoints): # 1 = bottom left corner, 2 = top right corner
        bL = [longitude1, latitude1] # Bottom left corner (X,Y)
        tR = [longitude2, latitude2] # Top right corner (X,Y)

        self.maxPoints = maxPoints # Max points before decomposition
        self.root = Node(bL, tR, root = 1) # Create root node
        

    # Split node into 4 new nodes
        # Move points to corresponding nodes
    def Decompose(self):
        pass



    # Insert a point into a node
    def Insert(self, longitude, latitude, altitude, time):
        # Create a point object
        point = Point(longitude,latitude, altitude, time)

        # Add point to tree
        self.root.addPoint(point)

    # Update existing node
    def Update(self):
        pass

    # Delete an existing node
    def Delete(self):
        pass

    # ADD GETTERS/SETTERS





############################################################

def main():

    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10, 1)

    quadtree.Insert(1,1,2,3)

    x = 1
if __name__ == "__main__":
    # execute only if run as a script
    main()  