# Задание 1.  Доделать реализацию функции eval со скобками

def reduction_correct_form_expression(func):
    f_work = func.replace('^', '**')
    f_work = f_work.replace(' ', '')
    #f_work = f_work.replace(',', '.')
    return f_work

# def arithmetic_action():


def identification_numbers_right(simbol, expression, index):
    right_num = ''
    if simbol == '**':
        a = index + 2
    else:
        a = index +1 
    for i in range(a, len(expression)):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            right_num = bb + right_num
        else:
            break
    print(right_num)
    return float(right_num)

def identification_numbers_left(expression, index):
    left_num = ''
    for i in range(index-1, -1, -1):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            left_num = bb + left_num
        else:
            break
    print(left_num)
    return float(left_num)



# simbol = ['**', '*', '/', '+', '-']

#func = '(12/3+(2+3)**3-7)*2-16 / (4 +4)+(11-7*((8/4)**2 +6)/5)'
func = '2.2/1.1+2**3-7+5+10/2.0*4+2**2'
#r = eval(func)
#print(f'{r = }')
f_work = reduction_correct_form_expression(func)
print(f'{f_work = }')
#print(eval(f_work))
simbol = '/'
K = f_work.count('**')
index = f_work.find(simbol)
print(index)
#aa = '/'
#print(f'{aa = }')
# left_num = ''
# for i in range(index-1, -1, -1):
#     bb = (f_work[i])
#     if bb.isdigit() or bb == '.':
#         left_num = bb + left_num
#     else:
#         break
# left_num = float(left_num)
# print(left_num)
#aa = left_num + aa
#print(f'{aa = }')
left_num = identification_numbers_left(f_work, index)
right_num = identification_numbers_right(simbol, f_work, index)

# right_num = ''
# for i in range(index+1, len(f_work)):
#     bb = (f_work[i])
#     if bb.isdigit() or bb == '.':
#         right_num = bb + right_num
#     else:
#         break
# print(right_num)
# right_num = float(right_num)
res = left_num/right_num
print(res)
#aa = aa + right_num
#print(f'{aa = }')

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