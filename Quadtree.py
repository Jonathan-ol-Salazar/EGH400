import matplotlib.pyplot as plt

# Point that will be stored in a leaf node
class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.point = {}


# Node Class - leaf = data and no children, internal = has children
class Node:
    def __init__(self, depth, parent, bottomCoords, topCoords, code="", points=[], children=[]):
        self.bottomCoords = bottomCoords
        self.topCoords = topCoords
        self.points = points
        self.children = children
        self.parent = parent
        self.depth = depth
        self.state = 0                      # Initialize as empty leaf node

        # state == 1 if node has children
        if children != 0:
            self.state = 1


    # Getters and Setters #

    # Return points
    def getPoints(self):
        return self.points

    # Return number of points
    def getNumPoints(self):
        return self.points.count

    # Add points
    def setPoints(self, point):
        self.points.update(point)

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
    


# Quadtree Class, contains all the methods for data structure functionality 
class Quadtree:

    # Initialize Quadtree with specified size and create 4 children
    def __init__(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]

        # Get coordinates for children nodes
        childrenCoords = self.divideCoords(bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y)

        # Create children nodes
        one = Node(1, 0, childrenCoords[0][0], childrenCoords[0][1], 1)
        two = Node(1, 0, childrenCoords[1][0], childrenCoords[1][1], 2)
        three = Node(1, 0, childrenCoords[2][0], childrenCoords[2][1], 3)
        four = Node(1, 0, childrenCoords[3][0], childrenCoords[3][1], 4)


        # Add children to a list
        self.arrayOfChildren = [one, two, three, four] 

        # Create root node with children
        self.root = Node(0, 0, self.bottomCoords, self.topCoords, self.arrayOfChildren)
      

    # Divide a region into 4 quadrants and return coords  
    def divideCoords(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):

         # Mid points
        mid_X = topRight_X/2
        mid_Y = topRight_Y/2

        # Coordinates for each quadrant
        oneCoords = [[bottomLeft_X, mid_Y, mid_X, mid_Y], [bottomLeft_X, topRight_Y, mid_X, topRight_Y]]
        twoCoords = [[mid_X, mid_Y, topRight_X, mid_Y], [mid_X, topRight_Y, topRight_X, topRight_Y]]
        threeCoords = [[bottomLeft_X, bottomLeft_Y, mid_X, bottomLeft_Y], [bottomLeft_X, mid_Y, mid_X, mid_Y]]
        fourCoords = [[mid_X, bottomLeft_Y, topRight_X, bottomLeft_Y], [mid_X, mid_Y, topRight_X, mid_Y]]

        # Return coordinates for each node
        return [oneCoords, twoCoords, threeCoords, fourCoords]
    


############################################################

def main():
    # Initialize Quadtree
    quadtree = Quadtree(0,0,10,10)

    # Children of quadtree
    children = quadtree.arrayOfChildren  
    

    
    # Print children
    for kids in children:
        kids.getTopCoords
        kids.getBottomCoords

        print(str(kids.getTopCoords)) 


if __name__ == "__main__":
    # execute only if run as a script
    main()






















# Plotting


class plottingGrid:
    def __init__(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]
        plt.plot(self.topCoords, self.bottomCoords) 
        plt.show()



#%%
import matplotlib.pyplot as plt

x1 = [0,1] 
y1 = [0,1] 
# plotting the line 1 points  
# plt.plot(x1, y1, 'bo') 
#####################

class NodePlot:
    def __init__(self, depth, parent, bottomCoords, topCoords, points=0, code=""):
        self.bottomCoords = bottomCoords
        self.topCoords = topCoords
        self.points = points
        self.children = []
        self.parent = parent
        self.depth = depth


    # Getters and Setters #

    def getPoints(self):
        return self.points

    def getBottomCoords(self):
        return self.bottomCoords

    def getTopCoords(self):
        return self.topCoords

    def setPoints(self, point):
        self.points.update(point)

    # def plot(self):
    #     x = [self.bottomCoords(1), self.bottomCoords(3), self.topCoords(1), self.topCoords(3)]
    #     y = [self.bottomCoords(2), self.bottomCoords(4), self.topCoords(2), self.topCoords(4)]

    #     plt.plot(x, y, 'bo')
       


class QuadtreePlot:
    def __init__(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]
        self.children = 4
        # self.root = NodePlot(0, 0, self.bottomCoords, self.topCoords)
        # self.root.children = self.children

        mid_X = topRight_X/2
        mid_Y = topRight_Y/2

        one = NodePlot(1, 0, [bottomLeft_X, mid_Y, mid_X, mid_Y], [bottomLeft_X, topRight_Y, mid_X, topRight_Y], 1)
        two = NodePlot(1, 0, [mid_X, mid_Y, topRight_X, mid_Y], [mid_X, topRight_Y, topRight_X, topRight_Y], 2)
        three = NodePlot(1, 0, [bottomLeft_X, bottomLeft_Y, mid_X, bottomLeft_Y], [bottomLeft_X, mid_Y, mid_X, mid_Y], 3)
        four = NodePlot(1, 0, [mid_X, bottomLeft_Y, topRight_X, bottomLeft_Y], [mid_X, mid_Y, topRight_X, mid_Y], 4)

        nodes = [one, two, three, four] 

        self.y = []
        self.x = []
        for node in nodes:
            x = [node.bottomCoords[0], node.bottomCoords[2], node.topCoords[0], node.topCoords[2]]
            y = [node.bottomCoords[1], node.bottomCoords[3], node.topCoords[1], node.topCoords[3]] 
            # print(x)
            # print(y)
            plt.plot(x,y,'bo')
        plt.show
        # print(x)
        # print(y)

QuadtreePlot(0,0,100,100)
