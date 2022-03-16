class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

x1 = int(input("Enter your first x value: "))
y1 = int(input("Enter your first y value: "))
x2 = int(input("Enter your second x value: "))
y2 = int(input("Enter your second y value: "))
coordinate1 = (x1,y1)
coordinate2 = (x2,y2)
li = Line(coordinate1,coordinate2)
print("Two cordinate distance value : ",li.distance())
print("Two cordinate slope value : ",li.slope())