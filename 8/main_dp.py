program = [
    (x[0], int(x[1]))
    for x in 
    [
        x.strip().split(' ')
        for x in open('input.txt', 'r').readlines()
    ]
]

N = len(program)

dp = []

for i in range(N + 1):
	dp.append([-1, -1])

dp[N][0] = 0
dp[N][1] = 1


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
    return instruction


def calc(ip, ac):
	if dp[ip][ac] == -1:
		operation, value = program[ip]
		# no podemos llegar hasta que no se demuestre lo contrario
		dp[ip][ac] = 0
		# sin cambiar la instruccion (el acc nos la suda de momento)
		_, new_ip = exec_instruction(program[ip], 0, ip)
		dp[ip][ac] = calc(new_ip, ac)
		# cambiando la instruccion (si es que aun no lo hemos hecho)
		if ac == 0:
			_, new_ip = exec_instruction([swap_instruction(operation), value], 0, ip)
			dp[ip][ac] = max(dp[ip][ac], calc(new_ip, 1))
	return dp[ip][ac]

# empezamos por la primera instruccion sin haber cambiado nada
# con esto llenamos toda la matriz
calc(0, 0)

ip, acc, ac = 0, 0, 0

print(len(program))

while ip < N:
	operation, value = program[ip]
	# miramos si llegamos al final sin swapear la instruccion
	new_acc, new_ip = exec_instruction(program[ip], acc, ip)
	# si no es 1 no hemos llegado sin swapear, hacemos swap
	if ac == 0 and dp[new_ip][0] == 0:
		new_acc, new_ip = exec_instruction(
			[swap_instruction(operation), value],
			acc,
			ip)
		# ya hemos swapeado, recordarlo
		ac = 1
		print(f'Swapeamos en {ip}')
	# asignamos las variables
	ip = new_ip
	acc = new_acc

print(acc)
