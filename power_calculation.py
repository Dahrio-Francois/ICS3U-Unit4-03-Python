#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: April 2022
# This program finds the square of consecutive integers


def main():
    # this function finds the square of consecutive integers

    # this is to keep track of how many times you go through the loop
    loop_counter = 0

    # input
    try:
        integer = int(input("Enter a positive integer: "))

        # process & output
        print("\n", end="")
        if integer >= 0:
            for loop_counter in range(integer + 1):
                answer = loop_counter**2
                print("{0}² = {1}.".format(loop_counter, answer))
                loop_counter = loop_counter + 1
        else:
            print("Please enter a positive integer")
    except Exception:
        print("\nThis was not an integer")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
