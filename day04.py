import re
from datetime import datetime

class Guard (object):
    def __init__(self, id=0):
        self.id = id
        self.asleep = []
        self.awake = []

    def is_asleep (self, t):
        return sum([1 if t1 <= t < t2 else 0 for t1, t2 in zip(self.asleep, self.awake)])

    def time_asleep (self):
        return sum([t2 - t1 for t1, t2 in zip(self.asleep, self.awake)])

    def minute_array (self):
        min_array = [0] * 60
        for t1, t2 in zip(self.asleep, self.awake):
            min_array[t1:t2] = [a+1 for a in min_array[t1:t2]]
        return min_array

    def best_time(self):
        arr = self.minute_array()
        return arr.index(max(arr))


def load_data (file):
    data = {}
    regex = re.compile("\[(.+)\] (.+)")
    with open(file, "r") as f:
        for line in f.read().splitlines():
            match = regex.match(line)
            timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
            action = match.group(2)
            data[timestamp] = action

    guards = {}
    curr_guard = 0
    m = re.compile ("(\d+)")
    for timestamp, action in sorted(data.items()):
        match = m.search(action)
        if match:
            curr_guard = int(match.group(1))
            if curr_guard not in guards:
                guards[curr_guard] = Guard(curr_guard)
        else:
            if "asleep" in action:
                guards[curr_guard].asleep.append(timestamp.minute)
            else:
                guards[curr_guard].awake.append(timestamp.minute)
    return guards

def part_1(guards):
    longest_time = 0
    score = 0
    for g in guards.values():
        t = g.time_asleep()
        if t > longest_time:
            longest_time = t
            score = g.id * g.best_time()
        print ("{}: {}".format(g.id, g.time_asleep()))
    print (score)

def part_2(guards):
    max_asleep = 0
    g_id = 0
    target_minute = 0
    for g in guards.values():
        minute_array = g.minute_array()
        if max(minute_array) > max_asleep:
            max_asleep = max(minute_array)
            target_minute = minute_array.index(max_asleep)
            g_id = g.id
    print (g_id * target_minute)

guards = load_data("day04.txt")
part_1(guards)
part_2(guards)


