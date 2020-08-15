#%%
import matplotlib.pyplot as plt


class Point():
    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude
        # Dictionary that contains timestamp, x, y, altitude
        self.point = {}


    def getLat(self):
        return self.latitude


    def getLong(self):
        return self.longitude

# Node Class - leaf = data and no children, internal = has children
class Node:
    def __init__(self, depth, parent, bottomCoords, topCoords, code="", points=[], children=[]):
        self.bottomCoords = bottomCoords
        self.topCoords = topCoords
        self.points = points
        self.children = children
        self.parent = parent
        self.depth = depth
        self.state = 0    
        self.code = code                  # Initialize as empty leaf node

        # state == 1 if node has children
        if len(children) != 0:
            self.state = 1


    # Getters and Setters #

    # Return points
    def getPoints(self):
        return self.points

    # Return number of points
    def getNumPoints(self):
        return self.points.count

    # Add points and sort via timestamp datetime
    def setPoints(self, point):
        self.points.append(point)

    # Get bottom coords
    def getBottomCoords(self):
        return self.bottomCoords

    # Get top coords
    def getTopCoords(self):
        return self.topCoords



    # Returns children
    def getChildren(self):
        return self.children

    # Returns current state 
    def getState(self):
        return self.state

    def setChild(self, child):
        self.children.append(child)




class CylinderBoundingBox():
    def __init__(self, Points, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.Points = Points
        self.Coords = [[bottomLeft_X, bottomLeft_Y], [topRight_X, topRight_Y]]
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]

    def getPoints(self):
        return self.Points
    
    def getCoords(self):
        return self.Coords

    # Get bottom coords
    def getBottomCoords(self):
        return self.bottomCoords

    # Get top coords
    def getTopCoords(self):
        return self.topCoords

class RTree():
    def __init__(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]
        self.depth = 1 # Maximum level of resolution
        self.root = Node(0, 0, self.bottomCoords, self.topCoords)

    def insert(self, CylinderBoundingBox):
        Box = CylinderBoundingBox.getCoords()

        bottomCoords = [Box[0], [ Box[1][0], Box[0][1] ]]
        topCoords = [[ Box[0][0], Box[1][1] ], Box[1]]


        newNode = Node(self.depth, 0, bottomCoords, topCoords, points=CylinderBoundingBox.getPoints() )
        self.root.setChild(newNode)
        x = 1


    # Get bottom coords
    def getBottomCoords(self):
        return self.bottomCoords

    # Get top coords
    def getTopCoords(self):
        return self.topCoords

    





############################################################

def main():
    # Initialize Quadtree
    rtree = RTree(0,0,10,10)

    # # Children of quadtree
    # children = quadtree.arrayOfChildren  
    

    
    # Print children
    # for kids in children:
    #     kids.getTopCoords
    #     kids.getBottomCoords

    #     print(str(kids.getTopCoords)) 

    point1 = Point(4.5,1)
    point2 = Point(4.5,2)
    point3 = Point(4.5,3)
    point4 = Point(4.5,4)

    points = [point1, point2, point3, point4]

    bottomLeft_X = points[0].getLong() - 0.5
    bottomLeft_Y = points[0].getLat() - 0.5
    topRight_X = points[3].getLong() + 0.5
    topRight_Y = points[3].getLat() + 0.5

    boundingBox = CylinderBoundingBox(points, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y)
    
    rtree.insert(boundingBox)
    x = 1

    ## plotting

    bottomCoords = rtree.getBottomCoords()
    topCoords = rtree.getTopCoords()


    # plotting as dots
    # plt.plot(bottomCoords[0],bottomCoords[1], 'bo')
    # plt.plot(bottomCoords[2],bottomCoords[3], 'bo')
    # plt.plot(topCoords[0],topCoords[1], 'bo')
    # plt.plot(topCoords[2],topCoords[3], 'bo')

    # plotting as line
    plt.plot([bottomCoords[1],bottomCoords[0]], [bottomCoords[3],bottomCoords[2]], 'b')
    plt.plot([bottomCoords[3],bottomCoords[2]], [topCoords[3],topCoords[2] ], 'b')
    plt.plot([bottomCoords[2],bottomCoords[2]], [topCoords[0],topCoords[3]], 'b')
    plt.plot([bottomCoords[2],bottomCoords[0]], [topCoords[0],topCoords[0]], 'b')

    # plt.plot([10,0], [0,0], 'b')
    # plt.plot([10,10], [0,10], 'b')
    


    bottomCoords = boundingBox.getBottomCoords()
    topCoords = boundingBox.getTopCoords()

    plt.plot(bottomCoords[0],bottomCoords[1], 'ro')
    plt.plot(bottomCoords[2],bottomCoords[3], 'ro')
    plt.plot(topCoords[0],topCoords[1], 'ro')
    plt.plot(topCoords[2],topCoords[3], 'ro')

    # plt.plot([bottomCoords[1],bottomCoords[0]], [bottomCoords[3],bottomCoords[2]], 'r')
    # plt.plot([bottomCoords[3],bottomCoords[2]], [topCoords[3],topCoords[2] ], 'r')
    # plt.plot([bottomCoords[2],bottomCoords[2]], [topCoords[0],topCoords[3]], 'r')
    # plt.plot([bottomCoords[2],bottomCoords[0]], [topCoords[0],topCoords[0]], 'r')

    # plt.plot([2,0], [10,8], 'r')
    # plt.plot([2,0], [10,8], 'r')
    # plt.plot([2,0], [10,8], 'r')
    # plt.plot([2,0], [10,8], 'r')




    x = []
    y = []
    for points in boundingBox.getPoints():
        # x.append(points.getLong())
        # y.append(points.getLat())
        plt.plot(points.getLong(),points.getLat(), 'ko')

    plt.ylabel('Y-Axis (Meters)')
    plt.xlabel('X-Axis (Meters)')

    plt.title('R-Tree With A Single Leaf Node')

    # plt.plot(0,10, 'bo')

    




    plt.show


if __name__ == "__main__":
    # execute only if run as a script
    main()  



#%%
import matplotlib.pyplot as plt
