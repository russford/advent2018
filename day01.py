with open("day01.txt", "r") as f:
    data = list(map(int, f.read().splitlines()))

freq = 0
freq_list = set()
i = 0
while True:
    freq_list.add(freq)
    freq += data[i]
    if freq in freq_list:
        print(freq)
        break
    i = (i+1) % len(data)

