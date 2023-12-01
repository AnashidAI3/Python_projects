"""Write a program that reads two numbers and displays their sum"""

def sum_numbers(number1 , number2):
    return number1 + number2



try:
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    result = sum_numbers(number1, number2)
    print(f"the sum of {number1} and {number2} is {result}")

except ValueError:
    print("you must enter the number!")



