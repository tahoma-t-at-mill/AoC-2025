#!/usr/bin/python3

# <https://adventofcode.com/2025/day/2>

class Bank:

    def __init__(self, batteries : str):
        self.batteries = batteries

    def __repr__(self) -> str:
        return f"Bank(batteries = {self})"

    def __str__(self) -> str:
        return f"{self.batteries}"

    def max_joltage(self) -> int:
        idx1 = val1 = idx0 = val0 = 0
        for i in range(0, len(self.batteries) - 1):
            digit = int(self.batteries[i])
            if digit > val1:
                val1 = digit
                idx1 = i
        for j in range(idx1 + 1, len(self.batteries)):
            digit = int(self.batteries[j])
            if digit > val0:
                val0 = digit
                idx0 = j
        return val1 * 10 + val0

def validate():
    example = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"]
    banks = [Bank(e) for e in example]
    for b in banks:
        print(f"{b} -> {b.max_joltage()}")

#validate()

    
def day_3_part_1():
    total = 0
    with open("input.txt", 'r') as f:
        for line in f:
            b = Bank(line.strip())
            total += b.max_joltage()
    print(f"day 3 part 1: what is the total output joltage? -> {total}")

day_3_part_1()
