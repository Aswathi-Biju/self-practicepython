#Create a function to check if a given number is odd or even.
def number_is_odd_or_even():
    while True:
        number=int(input("Enter a number: "))
        if number%2==0:
            print("Even")
        else:
            print("Odd")
            break
number_is_odd_or_even()
