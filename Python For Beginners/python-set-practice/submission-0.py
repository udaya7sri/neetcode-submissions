from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    my_list_without_duplicates = list(my_set)
    if len(words)==len(my_list_without_duplicates):
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
