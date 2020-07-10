
# Class for point in Quadtree
class Point:
    def __init__(self, latitude, longitude, altitude, timestamp): # long = x, lat = y
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.timestamp = timestamp
    
    # Add GETTERS/SETTERS

# Class for node in Quadtree
    # Node can two types - Internal or Leaf 
        # Internal Node - Has 4 children, cannot have a point
        # Leaf Node - No children, can have a point
    # Node can switch between types
class Node:
    def __init__():
        pass 

# Class for Quadtree
class Quadtree:
    # Give initial size of Quadtree
    # Sets the size 
    def __init__():
        