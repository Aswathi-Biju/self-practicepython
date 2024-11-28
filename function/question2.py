#Create a function to check if a given number is prime.
def prime_or_not():
    while True:
        number = int(input("Enter a number: "))
        for i in range(2, number):
            if number % i == 0:
                print(number, "is not Prime number")
                break
        else:
            print(number, "is Prime number")
prime_or_not()
