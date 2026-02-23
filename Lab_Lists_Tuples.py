numbers=[2, 3, 4, 5, 15, 1, 43, 20]

def sum_of_numbers(numbers):
    total=0
    for number in numbers:
        total+=number
    return total
def largest_number(numbers):
    largest_number=numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number=number
    return largest_number

def odd_numbers():
    odd_list=[number for number in range (1200, 2000,125) if number % 2 != 0]
    return odd_list
        
def list_Slicing (odd_list):
    return odd_list[0:5]


print(sum_of_numbers(numbers))
print(largest_number(numbers))
print(odd_numbers())
print(list_Slicing(odd_numbers()))

    