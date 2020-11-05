# define point class
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# use point class => create an object
p = Point(15, 30)

print(f"{p.x}, {p.y}")
