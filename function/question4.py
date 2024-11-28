#Define a function that takes a list and returns the sum of its elements.
def sum_in_list():
    number_list=[]
    n = int(input("How many numbers do you want in your list?: "))
    for i in range(n):
        number_list.append(int(input(f"Enter number{i + 1}:")))
    print(number_list)
    return sum(number_list)
print(sum_in_list())
