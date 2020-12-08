import re

operations = {
    "addr": lambda a, b, r: r[a] + r[b],
    "addi": lambda a, b, r: r[a] + b,
    "mulr": lambda a, b, r: r[a] * r[b],
    "muli": lambda a, b, r: r[a] * b,
    "banr": lambda a, b, r: r[a] & r[b],
    "bani": lambda a, b, r: r[a] & b,
    "borr": lambda a, b, r: r[a] | r[b],
    "bori": lambda a, b, r: r[a] | b,
    "setr": lambda a, b, r: r[a],
    "seti": lambda a, b, r: a,
    "gtir": lambda a, b, r: 1 if a > r[b] else 0,
    "gtri": lambda a, b, r: 1 if r[a] > b else 0,
    "gtrr": lambda a, b, r: 1 if r[a] > r[b] else 0,
    "eqir": lambda a, b, r: 1 if a == r[b] else 0,
    "eqri": lambda a, b, r: 1 if r[a] == b else 0,
    "eqrr": lambda a, b, r: 1 if r[a] == r[b] else 0
}

def execute_code (regs, code):
    print (regs, code)
    regs[code[3]] = operations[code[0]](code[1], code[2], regs)
    return regs


def check_codes (codes, values, regs_before, regs_after):
    new_codes = []
    for c in codes:
        r = execute_code (regs_before.copy(), [c]+values)
        if r == regs_after: new_codes.append (c)
    return new_codes


def solve_codes (inputs):
    poss = {i: list(operations.keys()) for i in range(16)}
    for example in inputs.split('\n\n'):
        input = [int(a) for a in re.findall("\d+", example)]
        new_list = check_codes(poss[input[4]], input[5:8], input[:4], input[-4:])
        poss[input[4]] = new_list
        if len(new_list) == 1:
            for k, v in poss.items():
                if k != input[4] and new_list[0] in v: v.remove(new_list[0])
    return {k:v[0] for k,v in poss.items()}


with open("day16.txt", "r") as f:
    inputs, program = f.read().split("\n\n\n\n")

# part 1
three_plus = 0
codes = operations.keys()
for example in inputs.split('\n\n'):
    input = [int(a) for a in re.findall("\d+", example)]
    if len(check_codes(codes, input[5:8], input[:4], input[-4:])) >= 3:
        three_plus += 1
print (three_plus)

# part 2

opcode_map = solve_codes (inputs)

regs = [0, 0, 0, 0]
for line in program.split('\n'):
    code = [int(a) for a in line.split(" ")]
    execute_code(regs, [opcode_map[code[0]]]+code[1:])

print (regs[0])












