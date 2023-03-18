class Shape():
    def areas(self):
        print(0)

class rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
 
l = int(input())
w = int(input())

rect = rectangle(l, w)
print(rect.area())