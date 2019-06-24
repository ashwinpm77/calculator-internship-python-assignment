# Program to test the Calculator class

from Calculator import Calculator


def main():
    calc = Calculator()
    exp = input("Enter the expression (in the form op1 operator op2):")
    res = calc.evaluate(exp)
    print("The result is", res)
    input("Press any key to exit")

main()
