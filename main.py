from operations import add, sub, mult, div
import sys

def main():
    if len(sys.argv) != 4:
        print("Calculate <num1> <operator> <num2>")
        sys.exit(1)

    _, num1, op, num2 = sys.argv
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid numbers")
        sys.exit(1)

    try:
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = sub(num1, num2)
        elif op == "*":
            result = mult(num1, num2)
        elif op == "/":
            result = div(num1, num2)
        else:
            print("Invalid operator. Use +, -, *, /")
            sys.exit(1)
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()
