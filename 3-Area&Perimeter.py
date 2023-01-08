from math import sqrt, pi
type = input("Write your wanted shape\n")

if type == "triangle":
    edge1 = float(input("Give the size of each edges.\n"))
    edge2 = float(input())
    edge3 = float(input())
    peri = edge1 + edge2 + edge3
    area = sqrt((peri/2)*(peri/2 - edge1)*(peri/2 - edge2)*(peri/2 - edge3))

elif type == "rectangle":
    edge1 = float(input("Give the size of edges of rectangle.\n"))
    edge2 = float(input())
    peri = 2*(edge1 + edge2)
    area = edge1 * edge2

elif type == "square":
    edge = float(input("Give the size of edge of square.\n"))
    peri = 4 * edge
    area = edge**2

elif type == "circle":
    r = float(input("Give the radius of circle.\n"))
    peri = 2*pi*r
    area = pi*r**2

print(f"The perimeter of given {type} is: {peri}\nThe area of given {type} is: {area}")