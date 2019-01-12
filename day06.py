class Point (object):
    def __init__(self, id, p):
        self.p = [int(a) for a in p.split(",")]
        self.id = id

    def dist (self, p2):
        return abs(self.p[0]-p2[0])+abs(self.p[1]-p2[1])

    def score(self, points):
        return sum([self.dist(p) for p in points])


def closest (p1, points):
    dist_list = sorted([(p.dist(p1), p.id) for p in points])
    if dist_list[0][0] == 0: return dist_list[0][1]
    return dist_list[0][1] if dist_list[0][0] < dist_list[1][0] else 0


def part_1(points):
    min_x = min([a.p[0] for a in points])
    max_x = max([a.p[0] for a in points])
    min_y = min([a.p[1] for a in points])
    max_y = max([a.p[1] for a in points])

    w = (max_x - min_x) // 2 + 1
    h = (max_y - min_y) // 2 + 1

    dist_map = {}
    edges = []
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            c = closest((x,y), points)
            dist_map[(x,y)] = c
            if x == min_x or x == max_x or y == min_y or y == max_y:
                if not c in edges: edges.append(c)
    print (', '.join([str(e) for e in edges]))

    potentials = [p for p in points if p.id not in edges]


    vals = list(dist_map.values())
    pot_dist = [(vals.count(p.id), p.id) for p in potentials]
    print ('\n'.join([str(a) for a in sorted(pot_dist)]))

    # print ('\n'.join([''.join([str(dist_map[(x,y)]) for x in range(min_x, max_x+1)]) for y in range(min_y, max_y+1)]))

def part_2 (points, n):
    min_x = min([a.p[0] for a in points])
    max_x = max([a.p[0] for a in points])
    min_y = min([a.p[1] for a in points])
    max_y = max([a.p[1] for a in points])

    w = (max_x - min_x) // 2 + 1
    h = (max_y - min_y) // 2 + 1

    edge = n // len(points)+1

    count = 0
    for x in range(min_x-edge, max_x+edge + 1):
        for y in range(min_y-edge, max_y+edge + 1):
            score = sum([p.dist((x,y)) for p in points])
            if score < n: count += 1

    print (count)

points = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".splitlines()

with open("day06.txt", "r") as f:
    points = f.read().splitlines()

points = [Point(i+1, l) for i, l in enumerate(points)]
part_2(points, 10000)