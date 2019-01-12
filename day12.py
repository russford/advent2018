from collections import defaultdict

class PlantRow (object):
    def __init__(self, initial):
        self.plants = defaultdict(bool)
        for i,s in enumerate(initial):
            if s == "#": self.plants[i] = True

    def __repr__(self):
        min_p = sorted(self.plants.keys())[0]
        max_p = sorted(self.plants.keys())[-1]
        return ''.join(['#' if self.plants[i] else "." for i in range(min_p, max_p+1)])

    def next_gen (self, rules):
        min_p = sorted(self.plants.keys())[0]
        max_p = sorted(self.plants.keys())[-1]

        p2 = {}
        match = "".join(['#' if self.plants[i] else "." for i in range(min_p-4, min_p+1)])
        for i in range(min_p-2, max_p+3):
            print (i, match)
            if match in rules:
                p2[i] = rules[match]
            match = match[1:] + ("#" if self.plants[i+3] else ".")

def next_gen(s, rules):
    s = "...." + s + "...."
    s2 = ""
    for i in range(len(s)-3):
        match = s[i:i+5]
        if match in rules:
            s2 += rules[match]
        else:
            s2 += "."
    return s2.strip("."), 2-(len(s2)-len(s2.lstrip(".")))

def score (s, loc):
    return sum ([i-loc for i in range(len(s)) if s[i] == "#"])

def part_1(state, rules, iters):
    states = [(state, 0)]
    xtra = 0
    for i in range(iters):
        state, x_i = next_gen(state, rules)
        xtra += x_i
        states.append((state, xtra))
    max_xtra = max([s[1] for s in states])

    for i,s in enumerate (states):
        print (" {:>2}: {}{} {} {} {}".format(i, " "*(max_xtra-s[1]), s[0], s[1], score(s[0], s[1]), score(s[0],s[1]) - score(states[i-1][0], states[i-1][1])))

def part_2(state, rules, iters):
    states = {}
    xtra = 0
    i = 0
    while True:
        state, x_i = next_gen (state, rules)
        xtra += x_i
        if state in states:
            print ("matched: ", states[state], i, xtra)
            last_score = score(state, states[state][1])
            score_diff = score (state, xtra) - last_score
            print ((iters-i)*score_diff + last_score)
            break
        else:
            states[state] = (i, xtra)
        i += 1

rules = {}
with open ("day12.txt", "r") as f:
    data = f.read().splitlines()
    state = data[0][data[0].index(":")+2:]
    for d in data[2:]:
        k, v = d.split(" => ")
        rules[k] = v

part_1(state, rules, 20)
part_2(state, rules, 50000000000)


