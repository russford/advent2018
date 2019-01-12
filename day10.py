import re

class Point(object):
    id = 1
    def __init__ (self, v):
        self.id = id
        Point.id += 1
        self.p = v[:2]
        self.v = v[2:]

    def tick(self):
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]

    def advance(self, t):
        self.p[0] = self.p[0] + t * self.v[0]
        self.p[1] = self.p[1] + t * self.v[1]

def win_size (points):
    min_x = min([p.p[0] for p in points])
    max_x = max([p.p[0] for p in points])
    min_y = min([p.p[1] for p in points])
    max_y = max([p.p[1] for p in points])

    return min_x, max_x, min_y, max_y

def area (v):
    return (v[1]-v[0])*(v[3]-v[2])

def draw(points):
    min_x, max_x, min_y, max_y = win_size(points)
    grid = set()
    for p in points:
        grid.add((p.p[0], p.p[1]))
    print ('\n'.join([''.join(['#' if (x,y) in grid else "." for x in range(min_x, max_x+1)]) for y in range(min_y, max_y+1)]))

with open("day10.txt", "r") as f:
    data = [list(map(int, re.findall("(-?\d+)", l))) for l in f.read().splitlines()]

points = [Point(v) for v in data]

t = 0
t0 = 0
a = 0
while True:
    a2 = area(win_size(points))
    if t == 0 or a2 < a:
        t0 = t
        a = a2
    if a2 > a:
        print (t0, a)
        break
    for p in points:
        p.tick()
    t += 1

for p in points:
    p.advance(-1)

for i in range(2):
    draw(points)
    for p in points:
        p.tick()
    print()


