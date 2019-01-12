import re

def load_data (file):
    return [list(map(int, re.findall("\d+", l))) for l in file.splitlines()]


with open ("day03.txt", "r") as f:
    data = load_data (f.read())

# test_data = """#1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# """
# data = load_data(test_data)

max_w = max([d[1]+d[3] for d in data])
max_h = max([d[2]+d[4] for d in data])

s = [[0]*max_h for i in range(max_w)]
c = 0
for d in data:
    for i in range(d[1], d[1]+d[3]):
        for j in range(d[2], d[2]+d[4]):
            if s[i][j] == 1: c += 1
            s[i][j] += 1
print (c)

for d in data:
    if all([all([s[i][j] == 1 for i in range(d[1], d[1]+d[3])]) for j in range(d[2], d[2]+d[4])]):
        print (d[0])



