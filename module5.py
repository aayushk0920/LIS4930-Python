class Point:
    """A class to represent a point in 2D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """A class to manufacture rectangle objects."""
    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h."""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def create_rectangle(x, y, width, height):
    """Create a new instance of Rectangle."""
    posn = Point(x, y)
    return Rectangle(posn, width, height)

def str_rectangle(rect):
    """Convert given Rectangle instance into string of form (x, y, width, height)."""
    return "({0}, {1}, {2}, {3})".format(rect.corner.x, rect.corner.y, rect.width, rect.height)

def shift_rectangle(rect, dx, dy):
    """Change the x and y coordinates of the given Rectangle instance."""
    rect.corner.x += dx
    rect.corner.y += dy

def offset_rectangle(rect, dx, dy):
    """Create a new Rectangle instance which is offset from the given instance in x and y coordinates by dx and dy respectively."""
    new_x = rect.corner.x - dx
    new_y = rect.corner.y - dy
    return Rectangle(Point(new_x, new_y), rect.width, rect.height)

# Testing the functions
r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))

shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1))
print(str_rectangle(r2))
