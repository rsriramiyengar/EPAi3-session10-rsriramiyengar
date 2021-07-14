import math
from functools import lru_cache


class CustomPolygon :
    """
    Creates custom polygon sequence starting from number of vertices = 3 till the maximum specified number of vertices and common circum radius.
            Parameters : 
                max_vertices : Maximum number of edges/vertices of polygon in sequence
                common_circum_radius : Circum radius of polygon
            Returns : 
                efficiency : List comprising efficiency values (area/perimeter) for all the polygons in sequence
                max_efficiency : Returns the Polygon with the highest area : perimeter ratio
    """
    
    def __init__(self,max_vertices,common_circum_radius):
        self.max_vertices = max_vertices
        self.max_edges = max_vertices
        self.common_circum_radius = common_circum_radius

    @property
    def max_vertices(self):
        'intiates vertices'
        # print("Getting Edges...")
        return self._max_vertices

    @max_vertices.setter
    def max_vertices(self, max_vertices):
        'This Class Function assigns Vertices value by taking only interger part of value'
        # print("Setting edges value...")
        if max_vertices < 3:
            raise ValueError("Minimum number of Vertices required to form a polygon is 3")
        elif type(max_vertices) != int:
            print(f'Number of vertices cannot be non interger only interger part taken vertices={int(max_vertices)}')
            self._max_vertices = int(max_vertices)
        else:
            self._max_vertices = max_vertices

    @property
    def common_circum_radius(self):
        # print("Getting Cirum radius ...")
        return self._common_circum_radius

    @common_circum_radius.setter
    def common_circum_radius(self, common_circum_radius):
        'This Class Function assigns circum_radius value'
        if common_circum_radius < 0:
            raise ValueError("Cirumradius cannot be negative")
        self._common_circum_radius = common_circum_radius
    
    def __len__(self):
        'calculates the length of table storing efficiency'
        return self.max_vertices - 2
        
    def __getitem__(self,s):
        if isinstance(s,int):
            if s < 3 or s >= (self.__len__()+2):
                raise IndexError
            else:
                return CustomPolygon._efficiency(s,self.common_circum_radius)
        if isinstance(s,slice):
            start,stop,step = s.indices(self.__len__())
            rng = range(start,stop,step)
            return [CustomPolygon._efficiency(i+3,self.common_circum_radius) for i in rng]

    @lru_cache(2**10)     
    def _edgeLength(common_circum_radius,vertices):
        'This function calculates the edge length for given circumradius and number of vertices'
        return(2*common_circum_radius * math.sin(math.pi/vertices))
    
    @lru_cache(2**10)     
    def _apothem(common_circum_radius,vertices):
        'This function calculates the edge length for given circumradius and number of vertices'
        return(common_circum_radius*math.cos(math.pi/vertices))
    
    @lru_cache(2**10)
    def _efficiency(vertices,common_circum_radius):
        'This Function calculates the efficiency of the given number of vertices and common circumradius'
        area = 0.5 * vertices * CustomPolygon._edgeLength(common_circum_radius,vertices) * CustomPolygon._apothem(common_circum_radius,vertices)
        perimeter = vertices * CustomPolygon._edgeLength(common_circum_radius,vertices)
        return (area/perimeter)
    
    @property
    def max_efficiency(self):
        'This Module calculates max efficiency for given number of vertices and circumradius'
        slices = slice(0,self.__len__())
        efficiency = self.__getitem__(slices)
        max_efficiency = max(efficiency)
        print(f'Maximum efficiency polygon has Vertices : {efficiency.index(max_efficiency) + 3} and Circum Radius : {self.common_circum_radius} ')
        return efficiency.index(max_efficiency) + 3
    
    def __repr__(self):
        return f'CustomPolygon(Maximum Vertices = {self.max_vertices}, Circum Radius = {self.common_circum_radius})'
