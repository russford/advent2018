class Map (object):
    def __init__(self, data, chars):
        self.width = len(data[0])
        self.height = len(data)
        self.grid = ''.join(data).replace("E", ".").replace("G",".")
        self.load_chars(chars)

    def __getitem__(self, item):
        return self.grid[item[0]+item[1]*self.width]

    def __setitem__(self, key, value):
        self.grid[key[0]+key[1]*self.width] = value

    def at (self, x, y):
        return self.grid[x+y*self.width]

    def load_chars (self, chars):
        self.char_dict = { (c.x, c.y):c for c in chars }

    def build_regions(self, chars):
        self.regions = [-1 if c == "." else 0 for c in self.grid]
        for c in chars:
            self.regions[c.x+c.y*self.width] = 0
        color = 1
        for i in range(self.width):
            for j in range(self.height):
                if self.regions[i + j * self.width] == -1:
                    stack = []
                    stack.append((i,j))
                    while stack:
                        (a,b) = stack.pop()
                        if self.regions[a+b*self.width] == -1:
                            self.regions[a+b*self.width] = color
                            if a > 0: stack.append((a-1,b))
                            if a < self.width-1: stack.append((a+1, b))
                            if b > 0: stack.append((a, b-1))
                            if b < self.height-1: stack.append((a, b+1))
                    color += 1

    def print_char (self, x, y, regions=False):
        c = self.grid[x+y*self.width]
        r = regions and self.regions[x+y*self.width]
        char = self.char_dict.get((x,y))
        if char: return char.char
        if regions and c == ".":
            return "#" if r == 0 else chr(96+r)
        else:
            return char or c

    def print (self, regions=False):
        print ('\n'.join([''.join([self.print_char(i,j,regions) for i in range(self.width)]) for j in range(self.height)]))

class Character (object):
    id = 1
    def __init__(self, char, x, y, hp=0):
        self.id = Character.id
        Character.id += 1
        self.char = char
        self.x = x
        self.y = y
        self.hp = hp or 200

    def __repr__(self):
        return "{}: {} ({}, {}) {}".format(self.id, self.char, self.x, self.y, self.hp)

with open("day15test.txt", "r") as f:
    data = f.read().splitlines()
chars = []
w = len(data[0])
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c in "EG":
            chars.append(Character(c, j, i))
m = Map(data, chars)

m.print()
m.build_regions(chars)
m.print(True)
