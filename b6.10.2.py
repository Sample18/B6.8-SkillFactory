class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    def get_rectangle(self):
        return self.width * self.heigth

rectangle = Rectangle(10, 20)

print(rectangle.get_rectangle())