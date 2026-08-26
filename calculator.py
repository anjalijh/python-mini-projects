# Mini project no.01 : Calculator

def calculate(a, b):
    """Perform basic arithmetic operations on two numbers."""
    print("Add =", a + b)
    print("Subtract =", a - b)
    print("Multiply =", a * b)

    if b != 0:
        print("Divide =", a / b)
    else:
        print("Divide = Cannot divide by zero")

def main():
    try:
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
    except ValueError:
        print("Please enter valid whole numbers.")
        return

    calculate(a, b)

if __name__ == "__main__":
    main()
