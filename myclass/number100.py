#!/usr/bin/env python3
try:
    number = int(input("Enter a number: "))
    if number < 100:
        print("The number is less than 100")
    elif number>=100 and number<1000:
        print("The number is more than 100 and less than 1000")
    else:
        print("The number is more than 100")
except ValueError:
    print("The input is not a number")

