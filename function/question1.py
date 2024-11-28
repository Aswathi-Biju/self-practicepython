#Write a function to calculate the factorial of a number.
import math
#1st way
def factorial(number_1):
    return math.factorial(number_1)
result_1=factorial(5)
print(result_1)
#2nd way
def factorial():
    number_2=int(input("Enter a number: "))
    result_2=math.factorial(number_2)
    print(result_2)
factorial()
#3rd way
def factorial(number_3):
    result_3=math.factorial(number_3)
    print(result_3)
factorial(6)
