import math

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def cosine(x):
    return math.cos(math.radians(x))

def sine(x):
    return math.sin(math.radians(x))

def tangent(x):
    if x % 180 == 90:  # Undefined for 90, 270, etc.
        raise ValueError("Tangent is undefined for this input.")
    return math.tan(math.radians(x))


# # Main function for user input
# def main():
#     print("Welcome to the Scientific Calculator!")
#     print("Choose an operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Cosine")
#     print("6. Sine")
#     print("7. Tangent")
    
#     try:
#         choice = int(input("Enter the number corresponding to your choice: "))
#         if choice in [1, 2, 3, 4]:
#             a = float(input("Enter the first number: "))
#             b = float(input("Enter the second number: "))
#             if choice == 1:
#                 print("Result:", add(a, b))
#             elif choice == 2:
#                 print("Result:", subtract(a, b))
#             elif choice == 3:
#                 print("Result:", multiply(a, b))
#             elif choice == 4:
#                 print("Result:", divide(a, b))
#         elif choice in [5, 6, 7]:
#             x = float(input("Enter the number in radians: "))
#             if choice == 5:
#                 print("Result:", cosine(x))
#             elif choice == 6:
#                 print("Result:", sine(x))
#             elif choice == 7:
#                 print("Result:", tangent(x))
#         else:
#             print("Invalid choice. Please try again.")
#     except ValueError as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     main()
