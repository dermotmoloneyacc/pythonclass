#!/usr/bin/python
# lab2.py
# this program will calculate the cost of ownership of a house over 5 years


def main():
    # declare variables
    k = 0
    while (k < 3):
        icost = int(input("What is the initial cost of the house ?; "))
        fuelcost = int(input("What is the annual fuel cost ?"))
        taxrate = float(input("What is the tax rate ?:"))
        total_cost = icost + ((icost * taxrate) + fuelcost * 5)
        k = k + 1
        print ("Total cost for house ", k, "is ", total_cost)


main()
