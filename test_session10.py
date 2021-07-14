import pytest
import random
import string
import pytest

import session10
from session10 import Polygon
from session10 import CustomPolygon
import os
import inspect
import re
import math
from math import isclose
import random
import decimal
from decimal import Decimal
import time


def test_Polygon_edges_1():
    """
    This Test function checks if created class stores and calculates
    number of edges less than 3
    """
    with pytest.raises(ValueError) as execinfo:
        a = Polygon(2, 2)


def test_Polygon_circum_radius_2():
    """
    This Test function checks if created class stores and calculates
     with circum radius less 0.
    """
    with pytest.raises(ValueError) as execinfo:
        a = Polygon(3, -10)


def test_Polygon_edges_3():
    """
    This Test function checks if created class stores and calculates
    number of edges correctly
    """
    a = Polygon(10, 10)
    assert a.edges == 10, "Number of edges cannot be different"


def test_Polygon_vertices_4():
    """
    This Test function checks if created class stores and calculates
    number of vertices correctly
    """
    a = Polygon(10, 10)
    assert a.vertices == 10, "Number of vertices cannot be different"


def test_Polygon_interiorAngle_5():
    """
    This Test function checks if created class stores and calculates
    number of interiorAngle correctly
    """
    a = Polygon(10, 10)
    assert a.interiorAngle == 144, "wrongly calculates interiorAngle"


def test_Polygon_edgeLength_6():
    """
    This Test function checks if created class stores and calculates
    number of edgeLength correctly
    """
    a = Polygon(3, 3)
    assert a.edgeLength == (2 * 3 * math.sin(math.pi / 3)), "wrongly calculates edgeLength"


def test_Polygon_apothem_7():
    """
    This Test function checks if created class stores and calculates
    number of apothem correctly
    """
    a = Polygon(4, 4)
    assert a.apothem == (4 * math.cos(math.pi / 4)), "wrongly calculates apothem"


def test_Polygon_area_8():
    """
    This Test function checks if created class stores and calculates
    number of area correctly
    """
    a = Polygon(5, 5)
    assert a.area == 0.5 * 5 * (2 * 5 * math.sin(math.pi / 5)) * (5 * math.cos(math.pi / 5)), "wrongly calculates area"


def test_Polygon_perimeter_9():
    """
    This Test function checks if created class stores and calculates
    number of perimeter correctly
    """
    a = Polygon(6, 6)
    assert a.perimeter == 6 * (2 * 6 * math.sin(math.pi / 6)), "wrongly calculates perimeter"


def test_Polygon_repr_11():
    """
    This Test function checks if created class checks if repr function is written properly
    """
    a = Polygon(6, 6)
    assert a.__repr__ != None, "Repr cannot be None"


def test_Polygon_equal_11():
    """
    This Test function checks if created class checks if equal function is written properly
    """
    a = Polygon(6, 6)
    b = Polygon(6, 6)
    assert a == b, "Both Polygon are same"


def test_Polygon_gt_12():
    """
    This Test function checks if created class checks if gt function is written properly
    """
    a = Polygon(6, 6)
    b = Polygon(10, 6)
    assert a < b, "b cannot be less than a "


def test_CustomPolygon_edges_1():
    """
    This Test function checks if created class stores and calculates
    number of edges less than 3
    """
    with pytest.raises(ValueError) as execinfo:
        a = CustomPolygon(2, 2)


def test_CustomPolygon_circumradius_2():
    """
    This Test function checks if created class stores and calculates
     with circum radius less 0.
    """
    with pytest.raises(ValueError) as execinfo:
        a = CustomPolygon(3, -10)

def test_CustomPolygon_repr_3():
    """
    This Test function checks if created class checks if repr function is written properly
    """
    a = CustomPolygon(6, 6)
    assert a.__repr__ != None, "Repr cannot be None"


def test_CustomPolygon_len_4():
    """
    This Test function checks if created class checks if len function is written properly
    """
    a = CustomPolygon(7, 6)
    assert a.__len__() ==5, "Length of list is calculated correctly"

def test_CustomPolygon_max_efficiency_4():
    """
    This Test function checks if created class calculates max efficency correctly
    """
    a = CustomPolygon(7, 6)
    assert a.max_efficiency ==7, "Polygon with max Efficiecny not calculated correctly "

def test_CustomPolygon_max_efficiency_n_25_5():
    """
    This Test function checks if created class checks if len function is written properly
    """
    a = CustomPolygon(25, 6)
    assert a.max_efficiency ==25, "Polygon with max Efficiency not calculated correctly "

def test_CustomPolygon_getitem_6():
    """
    This Test function checks if created class checks if getitem function is written properly
    """
    a = CustomPolygon(25, 10)
    assert isclose(a.__getitem__(7), 4.504844339512096), "Polygon with max Efficiency not calculated correctly "

def test_CustomPolygon_getitem_n_eq_3_7():
    """
    This Test function checks if created class checks if len function is written properly
    """
    a = CustomPolygon(25, 10)
    with pytest.raises(IndexError) as execinfo:
        a.__getitem__(2)