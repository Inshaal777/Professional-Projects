def get_side_lengths():
    sides = []
    for i in range(1, 4):
        while True:
            try:
                length = float(input(f"What is the length of side {i}? "))
                if length <= 0:
                    raise ValueError("Length must be a positive number.")
                sides.append(length)
                break

            except ValueError as e:
                print(e)
                print("Please enter a valid number.")
    return tuple(sides)

def calculate_perimeter(sides):
    return sum(sides)

def main():
    sides = get_side_lengths()
    perimeter = calculate_perimeter(sides)
    print(f"The perimeter of the triangle is {perimeter:.2f}")

if __name__ == "__main__":
    main()