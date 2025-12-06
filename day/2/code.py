#!/usr/bin/python3

# <https://adventofcode.com/2025/day/2>

class Id:

    def __init__(self, value : int = 0):
        self.value = value

    def __repr__(self) -> str:
        return f"Id(value = {self})"

    def __str__(self) -> str:
        return f"{self.value}"

    def is_valid(self) -> bool:
        digits = str(self.value)
        
        # odd count of digits in value is always a valid id
        count = len(digits)
        if count % 2 == 1:
            return True
        
        # first half of digits equal to second half of digits is the
        # invalid id pattern
        half = int(count / 2)
        if digits[:half] == digits[half:]:
            return False

        # all other patterns of even count of digits are valid
        return True

    
def id_ranges(desc : str):
    for range in desc.split(','):
        span = range.split('-')
        if len(span) == 2:
            current = int(span[0])
            last = int(span[1])
            while True:
                yield Id(current)
                if current == last:
                    break
                current += 1

def count_invalid_ids(desc : str):
    return sum(int(not id.is_valid()) for id in id_ranges(desc))

def sum_invalid_ids(desc : str):
    return sum(id.value for id in id_ranges(desc) if not id.is_valid())



def validate():
    example_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    for id in id_ranges("11-22,95-115"):
        print(f"{repr(id)} -> {id.is_valid()}")
    
    invalid_count = count_invalid_ids("11-22,95-115")
    print(f"count_invalid_ids(\"11-22,95-115\") -> {invalid_count}")
    
    invalid_sum = sum_invalid_ids("11-22")
    print(f"sum_invalid_ids(\"11-22\") -> {invalid_sum}")

#validate()

    
def do_part_one():
    print(f"day 2 part 1: What do you get if you add up all of the invalid IDs?")
    with open("input.txt", 'r') as f:
        for line in f:
            sum = sum_invalid_ids(line)
            print(f"\t\"{line}\" -> {sum}")

do_part_one()
