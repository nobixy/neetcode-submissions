from typing import Dict  # this adds type hinting for Dict


def count_characters(word: str) -> Dict[str, int]:
    char_occ = {}
    for char in word:
        if char not in char_occ:
            char_occ[char] = 1
        else:
            char_occ[char] += 1

    return char_occ


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
