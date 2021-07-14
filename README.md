# Created By : Sriram Iyengar
# EPAI Session 10 : Sequences

1. A regular strictly convex polygon is a polygon that has the following characteristics:
    1. All interior angles are less than 180
    2. All sides have equal length

> ![My Image](https://github.com/rsriramiyengar/EPAi3-session10-rsriramiyengar/blob/master/images/Image01.png)

2. For a regular strictly convex polygon with:
    * n edges (=n vertices)
    * R circumradius
    * interiorAngle=(n−2)⋅(180/n) 
    * edgeLength,s=2⋅R⋅sin(π/n)
    * apothem,a=R⋅cos(πn)
    * area=(1/2)⋅n⋅s⋅a
    * perimeter=n⋅s

3.  Objective 1 [pts:400]:
    1. Create a Polygon Class:
        1. where initializer takes in:
            1. number of edges/vertices
            2. circumradius
        2. that can provide these properties:
            1. '#edges
            2. '#vertices
            3. interior angle
            4. edge length
            5. apothem
            6. area
            7. perimeter
        3. that has these functionalities:
            1.  a proper \____repr____ function
            2.  implements equality (==) based on # vertices and circumradius (\____eq____)
            3.  implements > based on number of vertices only (\____gt____)
    2. Objective 2 [pts:600]:
        1. Implement a Custom Polygon sequence type:<br/>
            1. where initializer takes in:
                * number of vertices for largest polygon in the sequence
                *common circumradius for all polygons 
        2. That can provide these properties:
            1. max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
        3. that has these functionalities:
            1. functions as a sequence type (\____getitem____)
            2.  supports the len() function (\____len____)
            3. has a proper representation (\____repr____)
    2. Results:
        1. Implement these 2 classes as a separate module. Access these modules in Google Colab or Deep Note or local Notebook (late you'd need to upload to GitHub)
        2. Run Objective 1 module to show that the functionalities are implemented properly
        3. Run Objective 2 module and show which polygon is efficient for n = 25
        4. You are submitting a link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them on GitHub Actions.
        5. All your code must be publicly accessible (make sure to open all links in an incognito window before submitting)