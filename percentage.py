#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program converts grade level to percentage


def calculate_volume(length: int, width: int) -> int:
    # calculate area

    area = length * width

    return area

def calculate_perimeter(length: int, width: int) -> int:
    # calculate perimeter

    perimeter = 2 * (length + width)

    return perimeter

def main():
    # this function gets length and width

    # input
    length_from_user = int(input("Enter the length of a rectangle (cm): "))
    width_from_user = int(input("Enter the width of a rectangle (cm): "))
    print("")

    #call functions
    calculated_area = calculate_area(length_from_user, width_from_user)
    calculated_perimeter = calculate_perimeter(length_from_user, width_from_user)

    print("The area is {0} cm²".format(calculated_area))
    print("The perimeter is {0} cm".format(calculated_perimeter))


if __name__ == "__main__":
    main()
