import math


class Polygon:
    """
    Creates a polygon with specified number of vertices and circum radius.

            Input Parameters :
                number_edges : Number of edges/vertices of polygon
                circum_radius : Circum radius of polygon
    """

    def __init__(self, number_edges: '+ve integer', circum_radius: '+ve value '):
        self.edges = number_edges
        self.circum_rad = circum_radius

    @property
    def edges(self):
        # print("Getting Edges...")
        return self._number_edges

    @edges.setter
    def edges(self, number_edges):
        'This Class Function assigns Edge value by taking only interger part of value'
        # print("Setting edges value...")
        if number_edges < 3:
            raise ValueError("Minimum number of edges required to form a polygon is 3")
        elif type(number_edges) != int:
            print(f'Number of Edges cannot be non interger only interger part taken Edges={int(number_edges)}')
            self._number_edges = int(number_edges)
        else:
            self._number_edges = number_edges

    @property
    def circum_rad(self):
        # print("Getting Cirum radius ...")
        return self._circum_rad

    @circum_rad.setter
    def circum_rad(self, circum_radius):
        'This Class Function assigns circum_radius value'
        if circum_radius < 0:
            raise ValueError("Cirumradius cannot be negative")
        self._circum_rad = circum_radius

    @property
    def interiorAngle(self):
        'interiorAngle=(n−2)*180/n'
        return ((self.edges - 2) * 180 / self.edges)

    @property
    def vertices(self):
        'number of vertices are same as number of Edges'
        return self.edges

    @property
    def edgeLength(self):
        'edgeLength, s = 2 * R * sin(π / n)'
        return (2 * self.circum_rad * math.sin(math.pi / self.edges))

    @property
    def apothem(self):
        'apothem, a = R * cos(π / n)'
        return (self.circum_rad * math.cos(math.pi / self.edges))

    @property
    def area(self):
        'area=1/2*n*s*a'
        return (0.5 * self.edges * self.edgeLength * self.apothem)

    @property
    def perimeter(self):
        'perimeter=n*s'
        return (self.edges * self.edgeLength)

    def __repr__(self):
        return f'Polygon with (Number of Edges = {self.edges}, Circum_Radius = {self.circum_rad})'

    def __eq__(self, other):
        'implements equality (==) based on # vertices and circumradius (__eq__)'
        if isinstance(self, type(other)):
            return ((self.vertices == other.vertices) and self.circum_rad == other.circum_rad)
        else:
            raise TypeError(f"Cannot compare values of type {self.__class__} and {other.__class__}")

    def __gt__(self, other):
        'implements > based on number of vertices only (__gt__)'
        if isinstance(self, type(other)):
            return (self.vertices > other.vertices)
        else:
            raise TypeError(f"Cannot compare values of type {self.__class__} and {other.__class__}")
