def area_of_triangle(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = area_of_triangle(base, height)
print(f"The area of the triangle is: {area}")
