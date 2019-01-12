import re

dirs = [( 1, 0),
        ( 0,-1),
        (-1, 0),
        ( 0, 1)]

dir_symbols = { "<": (-1, 0),
                ">": ( 1, 0),
                "v": ( 0, 1),
                "^": ( 0,-1) }

class Cart (object):
    id = 1
    def __init__(self, position, char):
        self.state = 0
        self.pos = position
        self.char = char
        self.id = Cart.id
        Cart.id += 1

    def __repr__(self):
        return "{}: {} {} {}".format(self.id, self.pos, self.char, self.state)


def load_grid (filename, carts):

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

    return grid, width, height


carts = []
grid, width, height = load_grid ("day13test.txt", carts)

print ('\n'.join(''.join(grid[i*width:(i+1)*width]) for i in range(height)))
for c in carts:
    print(c)







