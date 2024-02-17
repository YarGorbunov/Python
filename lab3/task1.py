class Point():
    x,y = 0,0
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1,p2):
    if not isinstance(p1,Point) or not isinstance(p2,Point):
        return False
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**(0.5)

def isOnOneLine(p1, p2, p3):
    if not isinstance(p1,Point) or not isinstance(p2,Point) or not isinstance(p3,Point):
        return False
    if (p3.x - p1.x)*(p2.y - p1.y) == (p3.y - p1.y)*(p2.x - p1.x):
        return True
    return False

class Quad():
    listPoints = []
    def __init__(self, listPoints):
        if not isinstance(listPoints, list):
            return
        if len(listPoints) != 4:
            return
        pointsSet = set()
        for e in listPoints:
            if not isinstance(e,Point):
                return
            pointsSet.add((e.x,e.y))
        if len(pointsSet) != 4:
            return
        for i in range(len(listPoints)):
            for j in range(i+1,len(listPoints)):
                for k in range(j+1,len(listPoints)):
                    if isOnOneLine(listPoints[i],listPoints[j],listPoints[k]):
                        print(i,j,k)
                        return
        print("normQuad")
        self.listPoints = listPoints
    
    def move(self, vector):
        if not isinstance(vector, Point): 
            return
        for point in self.listPoints:
            point.x += vector.x
            point.y += vector.y

class Pentagon():
    listPoints = []
    def __init__(self, listPoints):
        if not isinstance(listPoints, list):
            return
        if len(listPoints) != 5:
            return
        pointsSet = set()
        for e in listPoints:
            if not isinstance(e,Point):
                return
            pointsSet.add((e.x,e.y))
        if len(pointsSet) != 5:
            return  
        for i in range(len(listPoints)):
            for j in range(i+1,len(listPoints)):
                for k in range(j+1,len(listPoints)):
                    if isOnOneLine(listPoints[i],listPoints[j],listPoints[k]):
                        return 
        print("normPent")
        self.listPoints = listPoints
    
    def move(self, vector):
        if not isinstance(vector, Point): 
            return
        for point in self.listPoints:
            point.x += vector.x
            point.y += vector.y

def is_intersect(quad, pent):
    if not isinstance(quad, Quad) or not isinstance(pent,Pentagon):
        return
    for i in range(len(quad.listPoints)):
        for j in range(i+1,len(quad.listPoints)):
            quadPoint1 = quad.listPoints[i]
            quadPoint2 = quad.listPoints[j]
            A1 = (quadPoint2.y - quadPoint1.y)
            B1 = (quadPoint1.x - quadPoint2.x)
            C1 = quadPoint1.y*(quadPoint2.x - quadPoint1.x) - quadPoint1.x*(quadPoint2.y - quadPoint1.y)
            for k in range(len(pent.listPoints)):
                for l in range(k+1,len(pent.listPoints)):
                    pentPoint1 = pent.listPoints[k]
                    pentPoint2 = pent.listPoints[l]
                    A2 = (pentPoint2.y - pentPoint1.y)
                    B2 = (pentPoint1.x - pentPoint2.x)
                    C2 = pentPoint1.y*(pentPoint2.x - pentPoint1.x) - pentPoint1.x*(pentPoint2.y - pentPoint1.y)
                    if (A1*B2-A2*B1) == 0:
                        continue
                    xIntersect = -(C1*B2-C2*B1)/(A1*B2-A2*B1)
                    yIntersect = -(A1*C2-A2*C1)/(A1*B2-A2*B1)
                    if xIntersect >= max(min(quadPoint1.x,quadPoint2.x),min(pentPoint1.x,pentPoint2.x)) and xIntersect <= min(max(quadPoint1.x,quadPoint2.x),max(pentPoint1.x,pentPoint2.x)):
                        if yIntersect >= max(min(quadPoint1.y,quadPoint2.y),min(pentPoint1.y,pentPoint2.y)) and yIntersect <= min(max(quadPoint1.y,quadPoint2.y),max(pentPoint1.y,pentPoint2.y)):
                            print(xIntersect)
                            return True         
    return False

quad = Quad([Point(0,0),Point(0,1),Point(1,1),Point(1,0)])
pent = Pentagon([Point(0.5,1.5),Point(0.5,2.5),Point(1.5,2.5),Point(2,2),Point(1.5,1.5)])
print(is_intersect(quad,pent))