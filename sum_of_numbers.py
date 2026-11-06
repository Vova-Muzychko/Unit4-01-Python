#!/usr/bin/env python3

# Created by: Vova
# Created on: 6 Nov 2026
# This program calculates the sum of whole numbers up to a positive integer using a while loop.


def main():
    # Input
    user_string = input("Enter a positive integer: ")

    # Process and Output
    try:
        user_number = int(user_string)

        if user_number > 0:
            counter = 0
            total_sum = 0

            # Use while loop to add whole numbers starting from 0
            while counter <= user_number:
                total_sum += counter
                counter += 1

            print(f"\nThe sum of whole numbers from 0 to {user_number} is {total_sum}.")
        elif user_number == 0:
            print("\n0 is not a positive integer.")
        else:
            print(
                f"\n{user_number} is a negative integer. Please enter a positive number."
            )

    except ValueError:
        print(f"\n{user_string} is not a valid integer.")


if __name__ == "__main__":
    main()
