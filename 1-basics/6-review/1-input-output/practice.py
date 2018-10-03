import math

# Read radius from user
print("Please enter radius")
radius = float(input())

# Calculate area and cercumference
area = math.pi * (radius * radius)
# [Alt]area = math.pi * (radius ** 2)
# [Alt]area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius

# Display the result
print("Area is ", area)
# [Alt]print("Area is ", round(area, 2))
print("Circumference is ", circumference)
# [Alt]print("Area is ", round(circumference, 2))
