from typing import List

def read_integers() -> List[int]:
    inte = input()
    inte_list = [int(x) for x in inte.split(",")]
    return inte_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
