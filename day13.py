import re

dirs = [( 1, 0),
        ( 0,-1),
        (-1, 0),
        ( 0, 1)]

dir_symbols = { "<": (-1, 0),
                ">": ( 1, 0),
                "v": ( 0, 1),
                "^": ( 0,-1) }

class Pos (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Pos (self.x + other[0], self.y + other[1])

    def __getitem__(self, item):
        if item == 0: return self.x
        elif item == 1: return self.y
        else:
            raise IndexError("invalid index {}".format(item))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

class Cart (object):
    id = 1
    def __init__(self, position, char):
        self.state = 0
        self.pos = Pos(*position)
        self.char = char
        self.id = Cart.id
        self.crashed = False
        Cart.id += 1

    def __repr__(self):
        return "{}: {} {} {}".format(self.id, self.pos, self.char, self.state)

    def __lt__(self, other):
        return self.pos < other.pos

class Grid (object):
    def __init__(self, w, h, g):
        self.width = w
        self.height = h
        self.grid = g

    def __getitem__(self, item):
        return self.grid[item[1]*self.width + item[0]]

    def print(self, carts):
        str = list('\n'.join(''.join(self.grid[i * self.width:(i + 1) * self.width]) for i in range(self.height)))
        for c in carts:
            str[c.pos[0] + c.pos[1] * (self.width+1)] = c.char
        print (''.join(str))


def load_grid (filename):
    carts = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    width = max(len(l) for l in lines)
    height = len(lines)
    grid = [" "] * (width * height)

    replace_sym = { "^": "|", "v": "|", "<": "-", ">": "-"}
    for y, l in enumerate(lines):
        grid[y * width: y * width + len(l)] = l
        for match in re.finditer("([<>^v])", l):
            x = match.start()
            cart_sym = match.group(1)
            carts.append (Cart((x, y), cart_sym))
            grid[y*width+x] = replace_sym[cart_sym]

    return Grid(width, height, grid), carts

def advance_cart (cart, grid):
    symbol_step = { "/^": ">",  "/<": "v",  "/v":  "<", "/>":  "^",
                    "\\^": "<", "\\<": "^", "\\v": ">", "\\>": "v" }

    cart.pos += dir_symbols[cart.char]
    if grid[cart.pos] == "/" or grid[cart.pos] == "\\":
        cart.char = symbol_step[grid[cart.pos] + cart.char]

    if grid[cart.pos] == "+":
        turns = "^<v>"  # up left down right
        state_arr = [1, 0, -1]  # turn left, straight, right
        cart.char = turns[(turns.index(cart.char)+state_arr[cart.state]) % 4]
        cart.state = (cart.state + 1) % 3



def part_1(grid, carts):
    crash = None
    while crash is None:
        carts.sort()
        for c in carts:
            advance_cart(c, grid)
            if c.pos in [c2.pos for c2 in carts if c2 != c]:
                crash = c.pos
                print("crash detected: {}".format(c.pos))
                break

def carts_remaining (carts):
    return sum([0 if c.crashed else 1 for c in carts])

def part_2(grid, carts):
    while carts_remaining(carts) > 1:
        carts.sort()
        for c in carts:
            if not c.crashed:
                advance_cart(c, grid)
                for c2 in [c for c in carts if not c.crashed]:
                    if c.pos == c2.pos and c.id != c2.id:
                        c.crashed = True
                        c2.crashed = True

        # carts = [c for c in carts if not c.crashed]
        # grid.print(carts)
    print (len(carts))
    for c in carts:
        if not c.crashed:
            print (c)

grid, carts = load_grid ("day13.txt")
part_2 (grid, carts)










