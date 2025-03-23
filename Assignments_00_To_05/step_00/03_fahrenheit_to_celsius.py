"""program which prompts the user for a temperature in Fahrenheit
 (this can be a number with decimal places!) and outputs the temperature converted to Celsius."""

def main():
    temp_in_fahrenheit : float = input("Enter the temperature in fahrenheit: ")
    user_input :float = float(temp_in_fahrenheit)
    temp_in_celcius :float = (user_input - 32) * 5.0/9.0
    print(f"Temperature: \033[1;3m{temp_in_fahrenheit}\033[0mF = {temp_in_celcius}C")


if __name__ == "__main__":
    main()