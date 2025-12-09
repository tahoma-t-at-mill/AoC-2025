#!/usr/bin/python3

# <https://adventofcode.com/2025/day/2>

class Bank1:

    def __init__(self, batteries : str):
        self.batteries = batteries

    def __repr__(self) -> str:
        return f"Bank1(batteries = {self})"

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


example = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"]

def validate(banks):
    for b in banks:
        print(f"{repr(b)} -> {b.max_joltage()}")
    total = 0
    for b in banks:
        max_joltage = b.max_joltage()
        total += max_joltage
        print(f"{repr(b)} -> {max_joltage}")
    print(f"\t= {total}")

validate([Bank1(e) for e in example])

    
def day_3_part_1():
    total = 0
    with open("input.txt", 'r') as f:
        for line in f:
            b = Bank1(line.strip())
            total += b.max_joltage()
    print(f"day 3 part 1: what is the total output joltage? -> {total}")

day_3_part_1()

    
class Bank2(Bank1):

    def __repr__(self) -> str:
        return f"Bank2(batteries = {self})"

    def pick_max(self, start_idx : int, leave_n : int) -> (int, int):
        val = 0
        idx = 0
        end_idx = len(self.batteries) - leave_n
        for i in range(start_idx, end_idx):
            digit = int(self.batteries[i])
            if digit > val:
                val = digit
                idx = i
        return (val, idx)

    def max_joltage(self) -> int:
        total = 0
        idx = 0
        for leave_n in reversed(range(0, 12)):
            total *= 10
            val, pos = self.pick_max(idx, leave_n)
            total += val
            idx = pos + 1
        return total


validate([Bank2(e) for e in example])


def day_3_part_2():
    total = 0
    with open("input.txt", 'r') as f:
        for line in f:
            b = Bank2(line.strip())
            total += b.max_joltage()
    print(f"day 3 part 2: what is the new total output joltage? -> {total}")

day_3_part_2()
