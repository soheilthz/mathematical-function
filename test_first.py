import re

# import pdb
#
# pdb.set_trace()
input_func = ""
index = 0
sign_of_result = 0
variable_x = 2
result = 0


def how_many(ind):
    y = []
    global index
    index = ind
    num = 0
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
    global index, variable_x, input_func
    index = ind
    number = 0
    print("i am init_char", input_func)
    if input_func[index].isdigit():
        number = how_many(index)
    # elif input_func[index + 1] == '^':
    #     index += 1
    print("i am init_char done!!")
    return number


def init_sing(ind):
    global sign_of_result, input_func
    global index
    index = ind
    print("i am init_sign ", input_func)
    if input_func[index] == '+':
        sign_of_result = 1
    elif input_func[index] == '-':
        sign_of_result = 0
    index += 1
    print("i am init_sign done!!!", )


def main():
    global input_func, index, variable_x, sign_of_result, result
    string = "sasas"
    string = input("enter your function correctly \n")
    input_x = int(input("enter amount of x \n"))
    variable_x = input_x
    p = re.split(r'(?=[+-])', string)
    i = len(p)
    for q in range(1, i):
        print(p[q])
        input_func = p[q]
        index = 0




        # power
        if input_func.find("^") != -1:
            index = input_func.find("^") + 1
            power = input_func[index:]
            print("this is power", power)
            index = 0
            variable_x **= int(power)
            print("this is variable x after powering", variable_x)






        # primary
        if input_func.find("x") != -1:
            # print(input_func)
            init_sing(index)
            number = init_char(index)
            print("this is primary", number)
            print("before primary with variable x and number", variable_x, number)

            if number == 0:
                print("nothing")
                number = int(input_x)
            else:
                variable_x *= int(number)
            print("variable x is ", variable_x)
            # sum
            if input_func[0] == '+':
                result += variable_x
            else:
                result -= variable_x
            variable_x = input_x
            print("result after primary", result)

        else:
            index = input_func.find("^") + 1
            sum_num = int(input_func[index:])
            print(input_func, "this is sum", sum_num)
            if result == 0:
                result = sum_num
            else:
                if input_func[0] == '-':
                    result -= int(sum_num)
                else:
                    result += int(sum_num)
                index = 0

        variable_x = input_x
        print("final is result ", result)
        print("---------------------------------------------")


main()
