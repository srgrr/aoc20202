from copy import deepcopy

program = [
    (x[0], int(x[1]))
    for x in 
    [
        x.strip().split(' ')
        for x in open('input.txt', 'r').readlines()
    ]
]


def exec_instruction(ins_line, acc, ip):
    instruction, value = ins_line
    if instruction == 'acc':
        return acc + value, ip + 1
    elif instruction == 'jmp':
        return acc, ip + value
    else:
        return acc, ip + 1



def swap_instruction(instruction):
    if instruction == 'jmp':
        return 'nop'
    elif instruction == 'nop':
        return 'jmp'



def exec_program(p_lines, acc, visit_cnt, ip, nd=False):
    while ip >= 0 and ip < len(p_lines):
        instruction, value = p_lines[ip]
        if nd and instruction != 'acc':
            p_lines[ip] = (swap_instruction(instruction), value)
            exec_program(p_lines, acc, deepcopy(visit_cnt), ip, False)
            p_lines[ip] = (instruction, value)
        visit_cnt[ip] += 1
        if visit_cnt[ip] == 2: break
        acc, ip = exec_instruction(p_lines[ip], acc, ip)
    if all(x < 2 for x in visit_cnt) and ip == len(p_lines):
        print(f'loopless execution:{acc}')
    elif nd:
        print(f'infinite loop execution:{acc}')


exec_program(program, 0, [0] * len(program), 0, True)
