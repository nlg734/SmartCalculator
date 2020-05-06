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
    result = False
    try:
        result = int(equation[0])
    except TypeError:
        print("Invalid expression")
    try:
        for i in range(1, len(equation), 2):
            operation = find_operation(equation[i])
            if operation == "+":
                result += int(equation[i + 1])
            else:
                result -= int(equation[i + 1])
    except IndexError:
        print("Invalid expression")
        result = False
    return result


while True:
    nums = input().split()
    if len(nums) == 1:
        if nums[0] == "/exit":
            print("Bye!")
            break
        if nums[0] == "/help":
            print("The program can add and subtract")
            continue
        if "/" == nums[0][0]:
            print("Unknown command")
            continue
        try:
            print(int(nums[0]))
        except ValueError:
            print("Invalid expression")
    elif len(nums) != 0:
        total = get_total(nums)
        if type(total) is int:
            print(total)
