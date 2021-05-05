#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program tells you if you number is positive, negative or zero
#    with numbers inputted from the user


def main():
    # This function guesses your number

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process/output
    if integer > 0:
        print("{} is a positive number".format(integer))
    elif integer < 0:
        print("{} is a negative number".format(integer))
    else:
        print("{} is just zero".format(integer))
    print("\nDone.")


if __name__ == "__main__":
    main()
