from converters import celsius_to_fahrenheit, km_to_miles
import sys


def main():
    print("=== Standalone Unit Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")

    choice = input("\nSelect option: ")

    try:
        if choice == '1':
            val = float(input("Enter Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(val)} F")
        elif choice == '2':
            val = float(input("Enter KM: "))
            print(f"Result: {km_to_miles(val)} Miles")
    except ValueError:
        print("Error: Please enter a numeric value.")

    print("\n" + "-" * 30)
    input("Press ENTER to close this window...")


if __name__ == "__main__":
    main()