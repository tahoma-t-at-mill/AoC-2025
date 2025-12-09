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
        count = len(digits)
        
        # odd count of digits in value is always a valid id
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
        elif len(span) == 1:
            solo = int(span[0])
            yield Id(solo)

def count_invalid_ids(desc : str):
    return sum(int(not id.is_valid()) for id in id_ranges(desc))

def sum_invalid_ids(desc : str):
    return sum(id.value for id in id_ranges(desc) if not id.is_valid())


def validate(example):
    for id in id_ranges(example):
        print(f"{repr(id)} -> {id.is_valid()}")
    print(f"count_invalid_ids(\"{example}\") -> {count_invalid_ids(example)}")
    print(f"sum_invalid_ids(\"{example}\") -> {sum_invalid_ids(example)}")

#validate("11-22,95-115")
#validate("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")

    
def day_2_part_1():
    print(f"day 2 part 1: What do you get if you add up all of the invalid IDs?")
    with open("input.txt", 'r') as f:
        for line in f:
            sum = sum_invalid_ids(line)
            print(f"\tline = \"{line.strip()}\"")
            print(f"\t-> {sum}")

day_2_part_1()


class Id2(Id):

    def __init__(self, value : int = 0):
        super().__init__(value)

    def __repr__(self) -> str:
        return f"Id2(value = {self})"

    def is_valid(self) -> bool:

        # patterns with repeating identical chunks are invalid
        digits = str(self.value)
        count = len(digits)
        half = int(count / 2)
        for div in range(1, half + 1):
            chunks = [digits[div * step:div * (step + 1)] for step in range(0, int(count / div)) if count % div == 0]
            if len(set(chunks)) == 1:
                return False

        # all other patterns of digits are valid
        return True

    
def id2_ranges(desc : str):
    for range in desc.split(','):
        span = range.split('-')
        if len(span) == 2:
            current = int(span[0])
            last = int(span[1])
            while True:
                yield Id2(current)
                if current == last:
                    break
                current += 1
        elif len(span) == 1:
            solo = int(span[0])
            yield Id2(solo)

def count_invalid_id2s(desc : str):
    return sum(int(not id2.is_valid()) for id2 in id2_ranges(desc))

def sum_invalid_id2s(desc : str):
    return sum(id2.value for id2 in id2_ranges(desc) if not id2.is_valid())


def validate2(example):
    for id2 in id2_ranges(example):
        print(f"{repr(id2)} -> {id2.is_valid()}")
    print(f"count_invalid_id2s(\"{example}\") -> {count_invalid_id2s(example)}")
    print(f"sum_invalid_id2s(\"{example}\") -> {sum_invalid_id2s(example)}")

#validate2("11-22,101010-101011")
#validate2("2121212118-2121212124")
#validate2("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")

    
def day_2_part_2():
    print(f"day 2 part 2: What do you get if you add up all of the invalid IDs using these new rules?")
    with open("input.txt", 'r') as f:
        for line in f:
            sum = sum_invalid_id2s(line)
            print(f"\tline = \"{line.strip()}\"")
            print(f"\t-> {sum}")

day_2_part_2()
