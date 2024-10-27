C = 2999792458

def calculate_energy(mass):
    return mass * C ** 2
def get_mass_input():
    while True:
        user_input = input("Enter kilos of mass (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return None
        try:
            mass = float(user_input)
            if mass < 0:
                print("Mass cannot be negative. Please enter a valid mass. ")
                continue
            return mass
        except ValueError:
            print("Invalid input. Please enter a number for mass. ")
def main():
    print("Welcome to the Mass-Energy Equivalence Calculator!")
    while True:
        mass = get_mass_input()
        if mass is None:
            print("Exiting the program. Goodbye!")
            break

        energy = calculate_energy(mass)
        print(f"\ne = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy:.2e} joules of energy!\n")

if __name__ == "__main__":
    main()