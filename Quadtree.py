import matplotlib.pyplot as plt


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.point = {}



class Node:
    def __init__(self, depth, parent, bottomCoords, topCoords, points=0, code="", children=[]):
        self.bottomCoords = bottomCoords
        self.topCoords = topCoords
        self.points = points
        self.children = children
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




class Quadtree:
    def __init__(self, bottomLeft_X, bottomLeft_Y, topRight_X, topRight_Y):
        self.bottomCoords = [bottomLeft_X, bottomLeft_Y, topRight_X, bottomLeft_Y]
        self.topCoords = [bottomLeft_X, topRight_Y, topRight_X, topRight_Y]
        self.children = 4
       
        # self.root.children = self.children

        mid_X = topRight_X/2
        mid_Y = topRight_Y/2

        one = Node(1, 0, [bottomLeft_X, mid_Y, mid_X, mid_Y], [bottomLeft_X, topRight_Y, mid_X, topRight_Y], 1)
        two = Node(1, 0, [mid_X, mid_Y, topRight_X, mid_Y], [mid_X, topRight_Y, topRight_X, topRight_Y], 2)
        three = Node(1, 0, [bottomLeft_X, bottomLeft_Y, mid_X, bottomLeft_Y], [bottomLeft_X, mid_Y, mid_X, mid_Y], 3)
        four = Node(1, 0, [mid_X, bottomLeft_Y, topRight_X, bottomLeft_Y], [mid_X, mid_Y, topRight_X, mid_Y], 4)


        self.arrayOfChildren = [one, two, three, four] 

        self.root = Node(0, 0, self.bottomCoords, self.topCoords, self.arrayOfChildren)
        # for initalChildren in range(self.children):
        #     Node(1, 0, )



def main():
    quadtree = Quadtree(0,0,10,10)
    children = quadtree.arrayOfChildren  
    
    top = []
    bottom = []
    
    
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
