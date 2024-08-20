# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Main part of the program
if __name__ == "__main__":
    # Input length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Call functions to calculate area and perimeter
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    # Print the results
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")
