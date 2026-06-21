def add_two_numbers() -> int:
    numbers_input = input()
    str_list = numbers_input.split(",")
    int_list = [int(x) for x in str_list]
    return sum(int_list)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
