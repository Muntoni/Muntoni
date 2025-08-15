

operands = list()
operators = list()
problems = list()

print('Insert your problems, when you are done just hit "enter": ')
while True:
    p = input()
    if len(p) < 1: break
    problems.append(p)

if len(problems) > 5:
    print('Error: Too many problems.')
    problems = problems[:5]

for problem in problems:
    if '+' in problem:
        operand = problem.split('+')
        operator = '+'
    elif '-' in problem:
        operand = problem.split('-')
        operator = '-'
    else:
        print("Error: Operator must be '+' or '-'.")
        continue

    try:
        operand1 = operand[0]
        operand2 = operand[1]
    except:
        print('Error: Numbers must only contain digits.')
        continue

    if len(operand1) > 4 or len(operand2) > 4:
        print('Error: Numbers cannot be more than four digits.')
        continue
    operand1 = int(operand1)
    operand2 = int(operand2)

    operators.append(operator)
    operands.append(operand1)
    operands.append(operand2)



print(operands)
print(operators)
