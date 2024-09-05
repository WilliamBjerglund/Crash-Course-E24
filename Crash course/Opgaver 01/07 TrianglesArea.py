import math

def CalculateTriangleArea():
    g = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))

    area = 0.5 * g * h
    print(f"The Area of your Triangle is: {area}")

CalculateTriangleArea()