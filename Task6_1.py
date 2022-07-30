# Задание 1.  Доделать реализацию функции eval со скобками

def reduction_correct_form_expression(func: str) -> str:
    f_work = func.replace('^', '**')
    f_work = f_work.replace(' ', '')
    f_work = f_work.replace(',', '.')
    return f_work

def identification_numbers_right(simbol: str, expression: str):
    index = expression.find(simbol)
    right_num = ''
    tipe = 0
    if simbol == '**':
        a = index + 2
    else:
        a = index +1 
    for i in range(a, len(expression)):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            right_num = right_num +bb
            if bb == '.':
                tipe += 1 
        else:
            break
    if tipe > 0:
        right_num = float(right_num)
    else:
        right_num = int(right_num)
    return right_num

def identification_numbers_left(simbol: str, expression: str):
    print(simbol)
    index = expression.find(simbol)
    left_num = ''
    t = 0
    for i in range(index-1, -1, -1):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            left_num = bb + left_num
            if bb == '.':
                t += 1 
            print(f'{bb = }, {t = }')
        else:
            break
    if t > 0:
        left_num = float(left_num)
    else:
        left_num = int(left_num)
    return left_num

def arithmetic_action(simbol: str, left_num, right_num):
    if simbol == '**':
        return left_num**right_num
    elif simbol == '*':
        return left_num*right_num
    elif simbol == '/':
        return left_num/right_num
    elif simbol == '+': 
        return left_num+right_num
    elif simbol == '-':
        return left_num-right_num

def expression_abbreviation(simbol: str, expression: str):
    index = expression.find(simbol)
    left_num = identification_numbers_left(simbol, expression)
    right_num = identification_numbers_right(simbol, expression)
    res = arithmetic_action(simbol, left_num, right_num)
    li = index - len(str(left_num))
    ri = li + len(str(left_num)+simbol+str(right_num))
    expression = expression[:li] + str(res) + expression[ri:]
    print(expression)
    return expression

def priority_of_operations(simbol_1: str, simbol_2: str, expression: str) -> str:
    if simbol_1 in expression and simbol_2 in expression:
        if expression.find(simbol_1) > expression.find(simbol_2):
            return simbol_2
        elif expression.find(simbol_1) < expression.find(simbol_2):
            return simbol_1
    elif simbol_1 in expression:
        return simbol_1
    elif simbol_2 in expression:
        return simbol_2

def performing_operations(expression: str):
    while '**' in expression:
        simbol = '**'
        expression = expression_abbreviation(simbol, expression)
    while '*' in expression or '/' in expression:
        simbol = priority_of_operations('*', '/', expression)
        expression = expression_abbreviation(simbol, expression)
    while '+' in expression or '-' in expression:
        simbol = priority_of_operations('+', '-', expression)
        expression = expression_abbreviation(simbol, expression)
    result = float(expression)
    if result % 1 == 0:
        result = int(result)
    return result

# simbol = ['**', '*', '/', '+', '-']

func = '(12/3+(2+3)**3-7)*2-16 / (4 +4)+(11-7*((8/4)**2 +6)/5)'
#func = '2.2/1.1+2.0**3-7+5+10/2.0*4+2**2'
#print(f'{func = }')
#print(eval(func))
expression = reduction_correct_form_expression(func)
print(f'{eval(expression) = }')
print(expression)

# while '**' in expression:
#     simbol = '**'
#     expression = expression_abbreviation(simbol, expression)
# while '*' in expression or '/' in expression:
#     simbol = priority_of_operations('*', '/')
#     expression = expression_abbreviation(simbol, expression)
# while '+' in expression or '-' in expression:
#     simbol = priority_of_operations('+', '-')
#     expression = expression_abbreviation(simbol, expression)
# result = float(expression)
# if result % 1 == 0:
#     result = int(result)
result = performing_operations(expression)
print(f'{result = }, {type(result)}')


# if f_work.count('(') == f_work.count(')'):
#     left_count = f_work.count('(')
#     right_count = f_work.count(')')
# else:
#     print(f'Заданное выражение {func} некорректно! Оно содержит не парные скобки!!!')
# left_index = [f_work.find('(')]
# left_pos = left_index[0]
# right_index = [f_work.find(')')]
# right_pos = right_index[0]
# for i in range(1, left_count):
#     left_index.append(f_work.find('(', left_pos+1))
#     left_pos = left_index[i]
# for j in range(1, right_count):
#     right_index.append(f_work.find(')', right_pos+1))
#     right_pos = right_index[j]
# print(left_index)
# print(right_index)
# el_exp = []
# j = 0
# for i in range(len(left_index)-1):
#     if left_index[i+1] > right_index[j]:
#         level = i+1
#         tuple = (left_index[i], right_index[j])
#         el_exp.append(level)
#         el_exp.append(tuple)
#         j = i+1
# print(el_exp)        