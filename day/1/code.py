#!/usr/bin/python3

# <https://adventofcode.com/2025/day/1>

class Combination:

    def __init__(self, value : int = 0, position : int = 50, modulus : int = 100):
        self.modulus = modulus
        self.position = position % modulus
        self.password = abs(value)

    def __str__(self) -> str:
        return f"{self.password} ({self.position} / {self.modulus})"

    def __repr__(self) -> str:
        return f"Combination(password = {self.password}, position = {self.position}, modulus = {self.modulus})"

    def left(self, ticks : int) -> int:
        return self.rotate(-ticks)

    def right(self, ticks : int) -> int:
        return self.rotate(ticks)

    def rotate(self, ticks : int) -> int:
        delta = ticks % self.modulus
        self.position = (self.position + self.modulus + delta) % self.modulus
        if self.position == 0:
            self.password += 1
        return self.position

    def parse(self, cmd : str, verbose : bool = False) -> int:
        cmd = cmd.strip()
        direction = cmd[0]
        distance = cmd[1:]
        if direction == 'L':
            if distance.isdigit():
                self.left(int(distance))
        elif direction == 'R':
            if distance.isdigit():
                self.right(int(distance))
        if verbose:
            print(f"{cmd} -> {self}")
        return self.position

    def read(self, filename : str, verbose : bool = False) -> int:
        with open(filename, 'r') as f:
            for line in f:
                self.parse(line, verbose)
        return self.position


def test1() -> bool:
    c1 = Combination()
    for n in [-50, -1, -9, 40]:
        m = c1.rotate(n)
    return c1.password == 1 and c1.position == 30 and c1.modulus == 100

def test2() -> bool:
    c2 = Combination(modulus = 50)
    for cmd in ["L1", " L9", "foo", "R-10", "L 5", "bar", "L40 ", "R0"]:
        m = c2.parse(cmd)
    return c2.password == 2 and c2.position == 0 and c2.modulus == 50

def test3() -> bool:
    c3 = Combination()
    with open("test3.txt", 'w') as f:
        for cmd in ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]:
            f.write(cmd)
            f.write("\n")
    m = c3.read("test3.txt")
    return c3.password == 3 and c3.position == 32 and c3.modulus == 100

def do_part_one():
    c = Combination()
    m = c.read("input.txt")
    print(f"day 1 part 1: password = {c.password}")


class Combination_0x434C49434B(Combination):

    def __repr__(self) -> str:
        return f"Combination_0x434C49434B(password = {self.password}, position = {self.position}, modulus = {self.modulus})"

    def rotate(self, ticks : int) -> int:
        preposition = self.position + ticks
        if preposition == 0:
            self.password += 1
        if preposition < 0 and self.position != 0:
            self.password += 1
        self.password += int(abs(preposition) / self.modulus)
        self.position = preposition % self.modulus
        return self.position


def test4() -> bool:
    c4 = Combination_0x434C49434B()
    for cmd in ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]:
        m = c4.parse(cmd)
    return c4.password == 6 and c4.position == 32 and c4.modulus == 100

def do_part_two():
    c = Combination_0x434C49434B()
    m = c.read("input.txt")
    print(f"day 1 part 2: password = {c.password}")


print(f"test1() -> {test1()}")
print(f"test2() -> {test2()}")
print(f"test3() -> {test3()}")
print(80 * '-')
do_part_one()
print(80 * '=')
print(f"test4() -> {test4()}")
print(80 * '-')
do_part_two()
