"""Write a program that reads a number and converts it to base 2, 8 and 16 and displays it"""


try:
    number = int(input("enter your number: "))
    print(f"binary: {bin(number)}")
    print(f"octal: {oct(number)}")
    print(f"hexadecimal: {hex(number)}")
except ValueError:
    print("you must enter the number!")