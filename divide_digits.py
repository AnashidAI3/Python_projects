"""Write a program that reads a two-digit number and displays the result of the first digit to the power of the \
    second digit and the second digit to the power of the first digit."""


number = input("enter the number consist of 2 digits: ")
result1 = int(number[0])**int(number[1])
result2 = int(number[1])**int(number[0])
print(result1)
print(result2)