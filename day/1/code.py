#!/usr/bin/python3

class Combination:

    def __init__(self, value : int = 0, position : int = 50, modulus : int = 100):
        self.modulus = modulus
        self.position = position % modulus
        self.password = abs(value)

    def __str__(self):
        return f"{self.password} ({self.position} / {self.modulus})"

    def __repr__(self):
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

    def parse(self, cmd : str) -> int:
        cmd = cmd.strip()
        direction = cmd[0]
        distance = cmd[1:]
        if direction == 'L':
            if distance.isdigit():
                self.left(int(distance))
        elif direction == 'R':
            if distance.isdigit():
                self.right(int(distance))
        return self.position

    def read(self, filename : str, verbose : bool = False) -> int:
        with open(filename, 'r') as f:
            for line in f:
                self.parse(line)
                if verbose:
                    print(f"{self}")
        return self.position


def test1() -> bool:
    c1 = Combination()
    print(f"c1 = {repr(c1)}")
    for n in [-50, -1, -9, 40]:
        m = c1.rotate(n)
        print(f"c1.rotate({n}) -> {m};\tc1 = {c1}")
    return c1.password == 1 and c1.position == 30 and c1.modulus == 100

def test2() -> bool:
    c2 = Combination(modulus = 50)
    print(f"c2 = {repr(c2)}")
    for cmd in ["L1", " L9", "foo", "R-10", "L 5", "bar", "L40 ", "R0"]:
        m = c2.parse(cmd)
        print(f"c2.parse(\"{cmd}\") -> {m};\tc2 = {c2}")
    return c2.password == 2 and c2.position == 0 and c2.modulus == 50

def test3() -> bool:
    c3 = Combination()
    print(f"c3 = {repr(c3)}")
    with open("test3.txt", 'w') as f:
        for cmd in ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]:
            f.write(cmd)
            f.write("\n")
    m = c3.read("test3.txt", verbose = True)
    print(f"c3.read(\"test3.txt\", verbose = True) -> {m};\tc3 = {c3}")
    return c3.password == 3 and c3.position == 32 and c3.modulus == 100

#print(f"test1() -> {test1()}")
#print(f"test2() -> {test2()}")
#print(f"test3() -> {test3()}")


def do_part_one():
    c = Combination()
    m = c.read("input.txt")
    print(f"day 1 part 1 password = {c.password}")

do_part_one()




