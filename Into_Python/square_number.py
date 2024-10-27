def main():
    try:
        number = float(input("Type a number to see its square: "))
        square = calculate_square(number)
        print_result(number, square)

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def calculate_square(num):
    return num ** 2

def print_result(num, square):
    print(f"{num} squared is {square}")

if __name__ == "__main__":
    main()