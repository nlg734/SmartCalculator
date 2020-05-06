# calculator.py
# written by Natasha Graham
# JetBrains and Hyperskills Python course


def find_sign(minus):
    if len(minus) % 2 == 0:
        return "+"
    return "-"


def find_operation(op):
    if "+" in op:
        return "+"
    if "-" in op:
        return find_sign(op)


def get_total(equation):
    result = int(equation[0])
    for i in range(1, len(equation), 2):
        operation = find_operation(equation[i])
        if operation == "+":
            result += int(equation[i + 1])
        else:
            result -= int(equation[i + 1])
    return result


to_exit = False
while not to_exit:
    nums = input().split()
    if len(nums) == 1:
        if nums[0] == "/exit":
            to_exit = True
            print("Bye!")
            break
        if nums[0] == "/help":
            print("The program can add and subtract")
            continue
        print(nums[0])
    elif len(nums) != 0:
        total = get_total(nums)
        print(total)
