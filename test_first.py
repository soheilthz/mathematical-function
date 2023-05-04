import re

input_func = "+25"
index = 0
sign_of_result = 0
variable_x = 2
result = 0


def how_many(ind):
    y = []
    global index
    index = ind

    f = input_func[index - 1:]
    for j in f:
        if f[index].isdigit():
            y.append(f[index])
            index += 1
        else:
            break
    num = ''.join(y)
    return num


def init_char(ind):
    global index, variable_x
    index = ind
    number = 0
    if input_func[index].isdigit():
        number = how_many(index)
    elif input_func[index + 1] == '^':
        index += 1
    return number


def init_sing(ind):
    global sign_of_result
    global index
    index = ind
    if input_func[index] == '+':
        sign_of_result = 1
    elif input_func[index] == '-':
        sign_of_result = 0
    index += 1


def main():
    global input_func, index, variable_x, sign_of_result, result
    string = "+2x+3x-4x"
    p = re.split(r'(?=[+-])', string)
    i = len(p)
    for q in range(1, i):
        input_func = p[q]
        index = 0
        print(input_func)
        init_sing(index)
        number = init_char(index)
        variable_x *= int(number)

        if sign_of_result == 1:
            result += variable_x
        else:
            result -= variable_x
        variable_x = 2
        print(result)


main()
