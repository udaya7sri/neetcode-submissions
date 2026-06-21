from typing import List

def read_integers() -> List[int]:
    input_str = input()
    str_list = input_str.split(",")
    int_list = [int(x) for x in str_list]
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
