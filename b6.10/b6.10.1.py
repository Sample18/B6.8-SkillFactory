class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
    def get_rectangle_str(self):
        return 'Rectangle (' + str(self.x) +', '+ str(self.y) +', '+ str(self.width) +', '+ str(self.heigth) + ')'

rectangle = Rectangle(5, 10, 50, 100)

print(rectangle.get_rectangle_str())