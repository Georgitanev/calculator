from typing import Optional, Dict, Iterable, Union


# This function add two numbers
def add(x: float, y: float) -> float:
    """sum x + y"""
    return x + y


# This function subtracts two numbers
def subtract(x: float, y: float) -> float:
    """substract x + y"""
    return x - y


# This function multiplies two numbers
def multiply(x: float, y: float) -> float:
    """multiply x + y"""
    return x * y


# This function divides two numbers
def divide(x: float, y: float) -> float:
    """divide x / y"""
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


# Take input from the user

# Optional[float]:


def calc() -> Union[float, str, None]:
    choice: int = int(input("Enter choice(1/2/3/4): "))  # Example 1
    num1: Union[float, int] = float(input("Enter first number: "))  # Example 10
    num2: Union[float, int] = float(input("Enter second number: "))  # Example 10
    print(
        '{0} is {1} {2} is {3}{4} is {5}'.format(str(choice), str(type(choice)), str(num1), str(type(num1)), str(num2),
                                                 str(type(num2))))
    if type(choice) is int and type(num1) is float and type(num2) is float:
        if choice is 1:
            print(num1, "+", num2, "=", add(num1, num2))
            return add(num1, num2)
        elif choice is 2:
            print(num1, "-", num2, "=", subtract(num1, num2))
            return add(num1, num2)
        elif choice is 3:
            print(num1, "*", num2, "=", multiply(num1, num2))
            return add(num1, num2)
        elif choice is 4:
            print(num1, "/", num2, "=", divide(num1, num2))
            return add(num1, num2)
        else:
            print('Invalid choice input')
            return 'Invalid choice input'
    else:
        print("Invalid input")
        return 'invalid'


if __name__ == "__main__":
    calc()
