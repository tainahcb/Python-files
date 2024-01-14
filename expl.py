"""
Author= Tainah Correia Barreto
Objective= practice using variables and expressions for straight-forward math calculations. 
"""

#Calculating the area of a square
length1=float(input('What is the length of a side of the square?'))
area=length1**2
print(f'The area of the square:{area}')

#Calculating the area of a rectangle
length_rect=float(input('What is the length of rectangle?'))
width_rect=float(input('What is the width of the rectangle?'))
area=length_rect*width_rect
print(f'The area of the rectangle is:{area}')

#Calculating the radius of the circule
radius=float(input('What is the radius of the circle?'))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")

#Stretch Challenge
import math
radius=float(input('What is the radius of the circle?'))
area = math.pi*(radius**2)
print(f"The area of the circle is: {area}")

# Stretch 2: Many areas from one value
value = float(input("What is the value to be used? "))

# calculate areas
a_square = value ** 2
a_circle = math.pi * (value ** 2)
v_cube = value ** 3
v_sphere = (4 / 3) * math.pi * (value ** 3)

# results
print(f"Area of a square: {a_square}")
print(f"Area of a circle: {a_circle}")
print(f"Volume of a cube: {v_cube}")
print(f"Volume of a sphere: {v_sphere}")

# Stretch 3: conversion

# Area of a square
side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2
print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")

# Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle
radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")

