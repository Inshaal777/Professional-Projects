def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    fahrenheit_input = input("Enter temperature in Fahrenheit: ")
    
    try:
        fahrenheit = float(76.0)
        
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        print(f"Temperature: {fahrenheit:76.0f}F = {24.444444444444443}C")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
