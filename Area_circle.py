"""Write a program that takes the radius of a circle and displays the area of the circle"""


import math   #import the math moudule for use the pi number!

def Area_circle(radius):
    return math.pi * (radius**2)



try:
    radius = float(input("enter your radius number: "))
    Area = Area_circle(radius)
    print(f"radius of circle is {radius} and the Area of circle must be {Area}")

except ValueError:
    print("the radius must be a number!")