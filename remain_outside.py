"""Write a program that reads two integers and displays their inverse"""

def reminder(number1 , number2):
    remain = number1 % number2
    outside = number1 // number2
    print(f"the remain is {remain} and the outside is {outside}")


try:
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))
    reminder(number1, number2)
except ValueError:
    print("must choose the number!")
except ZeroDivisionError:
    print("number must be another number except zero")