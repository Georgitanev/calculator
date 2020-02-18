from typing import Union, Optional, List  # Optional, Dict, Iterable, Tuple


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
print("5.Put 2 numbers between 0 to 10 - to add and multiply them")


# Optional[float]:

# Tuple[float, float] # Union[float, None]
def calc() -> Optional[float]:  # , None
    choice: int = int(input("Enter choice(1/2/3/4/5): "))  # Example 1
    num1: float = float(input("Enter first number: "))  # Example 10
    num2: float = float(input("Enter second number: "))  # Example 10
    # choice, num1, num2 = input_nums()
    if choice is 1:
        print(num1, "+", num2, "=", add(num1, num2))
        return None  # add(num1, num2)
    elif choice is 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
        return None  # subtract(num1, num2)
    elif choice is 3:
        print(num1, "x", num2, "=", multiply(num1, num2))
        return None  # multiply(num1, num2)
    elif choice is 4:
        print(num1, "/", num2, "=", divide(num1, num2))
        return None  # divide(num1, num2)
    elif choice is 5:
        if num1 <= 10 and num2 <= 10:
            for i in range(int(num1), int(num2)):
                print(i, "+", i+1, "=", add(i, i+1))
            for i in range(int(num1), int(num2)):
                print(i, "x", i+1, "=", multiply(i, i+1))
            return None  # List[add(i, i+1), multiply(i, i+1)]
        else:
            print('put num1 between 0 < 10 and put num2 < 10')
            return None
    raise Exception('Invalid input')
    # return None


if __name__ == "__main__":
    try:
        calc()
    except Exception as e:
        print('exception', e)

