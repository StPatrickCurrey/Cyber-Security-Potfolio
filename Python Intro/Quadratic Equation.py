# Input coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant (the value inside the square root)
discriminant = (b ** 2) - (4 * a * c)

# Check if the discriminant is non-negative (real solutions)
if discriminant >= 0:
    # Calculate the two solutions
    solution1 = (-b - discriminant ** 0.5) / (2 * a)
    solution2 = (-b + discriminant ** 0.5) / (2 * a)
    print(f"The solutions are {solution1} and {solution2}")
else:
    print("The equation has no real solutions.")
