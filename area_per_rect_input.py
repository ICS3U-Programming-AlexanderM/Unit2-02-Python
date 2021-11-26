# Created by: Alexander Matheson
# Created on: Nov 26 2021
# This program asks for user input for the length and
# width of a rectangle in mm.
# It then calculates and displays the area and perimeter.
import math


def main():
    # Get user input
    print("Today we will calculate the area and perimeter of a rectangle")
    print("")
    # Set variables with input
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # Calculate variables
    area = length * width
    perimeter = 2*(length + width)

    # Print variables
    print("")
    print("Area = {} mm^2". format(area))
    print("Perimeter = {} mm". format(perimeter))


if __name__ == "__main__":
    main()
