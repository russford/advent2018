def has_repeat(s, n):
    return any([s.count(c) == n for c in s])

def count_repeat (data, n):
    return sum([1 if has_repeat(s,n) else 0 for s in data])

def one_off(s1, s2):
    c = -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if c == -1:
                c = i
            else:
                return ""
    return "" if c == -1 else s1[:c]+s1[c+1:]


def part_1(data):
    print (count_repeat(data, 2) * count_repeat(data, 3))

def part_2(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            s = one_off(data[i], data[j])
            if s:
                print (s)



with open("day02.txt", "r") as f:
    data = f.read().splitlines()

part_1(data)
part_2(data)

