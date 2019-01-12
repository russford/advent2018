from collections import defaultdict, deque
import re

class Worker(object):
    def __init__(self):
        self.task = "."
        self.timer = 0

    def assign(self, task, dur):
        self.task = task
        self.timer = ord(task) - ord("A") + 1 + dur

    def tick(self):
        if not self.task == ".":
            self.timer -= 1
            if self.timer == 0:
                t = self.task
                self.task = "."
                return t
        return ""

def build_rules(rule_list):
    pre_rules = defaultdict(list)
    post_rules = defaultdict(list)
    for r in rule_list:
        pre, post = re.findall (" (\w) ", r)
        pre_rules[pre].append(post)
        post_rules[post].append(pre)
    return pre_rules, post_rules

def part_1 (pre_rules, post_rules):
    key_list = set(list(pre_rules.keys()) + list(post_rules.keys()))
    completed = []
    while True:
        available = sorted([p for p in key_list if all([a in completed for a in post_rules[p]]) and not p in completed])
        if available:
            completed += available[0]
        else:
            break
    print (''.join(completed))

def part_2 (pre_rules, post_rules, n, dur):
    workers = [Worker() for i in range(n)]
    key_list = set(list(pre_rules.keys()) + list(post_rules.keys()))
    assigned = []
    completed = []
    ticks = 0
    while True:
        for w in workers:
            t = w.tick()
            if t: completed += t
        for w in workers:
            if w.task == ".":
                available = sorted([p for p in key_list if all([a in completed for a in post_rules[p]]) and not p in assigned])
                if available:
                    w.assign(available[0], dur)
                    assigned += available[0]
        if all([w.task == "." for w in workers]): break
        ticks += 1
        print (ticks, '\t'.join([w.task for w in workers]), ''.join(completed))
    print (ticks, ''.join(completed))



data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".splitlines()

with open("day07.txt", "r") as f:
    data = f.read().splitlines()



pre_rules, post_rules = build_rules(data)
# part_1 (pre_rules, post_rules)
part_2 (pre_rules, post_rules, 5, 60)



