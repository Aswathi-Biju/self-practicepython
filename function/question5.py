#Write a function to reverse a string.
#fixed input
def reverse_string(string):
    string=string[::-1]
    return string
result=reverse_string("Hello World!")
print(result)
#user input
def reversing_a_string():
    string_2= input("Enter a string: ")
    string_2=string_2[::-1]
    print(string_2)
reversing_a_string()
