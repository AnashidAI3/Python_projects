"""Write a program that receives your age in years and converts it to seconds, minutes and hours"""


def change_age(age):
    second = age * 3156e4
    minute = second / 60
    hour = second / 3600
    print(f"hour: {hour}")
    print(f"minute: {minute}")
    print(f"second: {second}")



try:
    age = int(input("Enter your age: "))
    change_age(age)

except ValueError:
    print("your age must be an integer number!")