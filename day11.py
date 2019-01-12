def power_level (x, y, serial):
    rack_id = x+10
    p = (y*(x+10)+serial)*(x+10)
    p = (p // 100) % 10
    return p-5


def gen_grid (serial, n):
    grid = [[0] * n for i in range(n)]
    for x in range(n):
        for y in range(n):
            grid[x][y] = power_level(x+1, y+1, serial)
    return grid

def find_max (g, n):
    max_p = 0
    spot = None
    for x in range(len(g)-n+1):
        for y in range(len(g)-n+1):
            p = sum([sum([g[x+i][y+j] for i in range(n)]) for j in range(n)])
            if p > max_p:
                max_p = p
                spot = (x+1,y+1)
    return spot, max_p

# print (power_level(122,  79, 57))
# print (power_level(217, 196, 39))
# print (power_level(101, 153, 71))

g = gen_grid (18, 300)
find_max(g,3)

max_p = 0
max_size = 0
max_spot = 0
for i in range(1, 300):
    spot, p = find_max(g,i)
    if p > max_p:
        max_p = p
        max_spot = spot
        max_size = i
    print (i, "done")
print (max_spot, max_size, max_power)




