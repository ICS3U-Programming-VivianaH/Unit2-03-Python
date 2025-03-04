#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 4 2025
# This program calculates and displays the area
# and perimeter for a given user input
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches):"))

    # process
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal = tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
