from typing import List

def contains_duplicate(words: List[str]) -> bool:
    set_count = len(set(words))
    list_count = len(words)
    if set_count < list_count:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
