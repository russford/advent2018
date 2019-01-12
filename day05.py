import string

def process(s):
    is_chain = lambda a, b: a.upper() == b.upper() and a != b
    buf = []
    for c in s:
        if buf and is_chain (c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)

def part_1(s):
    print (process(s))

def part_2(s):
    print (min([process(s.replace(c,"").replace(c.upper(),"")) for c in string.ascii_lowercase]))

with open("day05.txt", "r") as f:
  s = f.read().splitlines()[0]

part_1 (s)
part_2 (s)
