#Week 1 Let's Analyze

a = float(input("Enter Length of the Base (A): "))
b = float(input("Enter Length of the Base (B): "))
height = float(input("Enter Length of the Height: "))

# Calculate the area of the triangle
triangle_area = (height * b) / 2

# Calculate the area of a trapezoid
trapezoid_area = ((a + b) / 2) * height

print(f"The Area of a Triangle is {triangle_area}")
print(f"The Area of a Trapezoid is {trapezoid_area}")

