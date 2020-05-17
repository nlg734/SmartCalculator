# calculator.py
# written by Natasha Graham
# JetBrains and Hyperskills Python course

variables = dict()


def find_sign(minus):
    if len(minus) % 2 == 0:
        return "+"
    return "-"


def find_operation(op):
    if "+" in op:
        return "+"
    if "-" in op:
        return find_sign(op)
    if "/" == op:
        return "/"
    if "*" == op:
        return "*"
    return "Invalid expression"  # not here


def is_higher_prec(op1, op2):
    precedence = "*/+-"
    if precedence.find(op1) >= precedence.find(op2):
        return False
    return True


def to_postfix(expression):
    postfix = []
    operators = []
    open_count = 0
    for piece in expression:
        if piece.isalpha():
            try:
                postfix.append(int(variables[piece]))
            except Exception:
                return "Unknown variable"
        elif piece.isnumeric():
            postfix.append(int(piece))
        elif piece[0] == "(":
            operators.append("(")
            i = 1
            if len(piece) > 1:
                while "(" in piece[i:]:
                    operators.append("(")
                    open_count += 1
                    i += 1
                postfix.append(int(piece[i:]))
            open_count += 1
        elif piece[-1] == ")":
            if open_count == 0:
                return "Invalid expression"
            if len(piece) > 1:
                postfix.append(int(piece[:len(piece) - 1]))
            while len(operators) > 0:
                if operators[-1] == "(":
                    operators.pop()
                    open_count -= 1
                    break
                postfix.append(operators.pop())
        else:
            op = find_operation(piece)
            if len(operators) == 0:
                operators.append(op)
                continue
            if is_higher_prec(op, operators[-1]):
                operators.append(op)
            else:
                while not is_higher_prec(op, operators[-1]):
                    if operators[-1] == "(":
                        break
                    postfix.append(operators.pop())
                    if len(operators) == 0:
                        break
                operators.append(op)
    for i in range(0, len(operators)):
        if operators[-1] != "(":
            postfix.append(operators.pop())
        else:
            return "Invalid expression"
    return postfix


def get_total(equation):
    num_stack = []
    for piece in equation:
        if isinstance(piece, int):
            num_stack.append(piece)
            # print(num_stack)
        else:
            if len(num_stack) == 0 or len(num_stack) == 1:
                print("Empty stack, or just 1 number", num_stack)
                print(equation)
                continue
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            if piece == "+":
                num_stack.append(num1 + num2)
            elif piece == "-":
                num_stack.append(num1 - num2)
            elif piece == "*":
                num_stack.append(num1 * num2)
            elif piece == "/":
                num_stack.append(num1 // num2)
            # print(num_stack)
    if len(num_stack) == 0:
        return None
    return num_stack.pop()


def assign_variables(expression):
    if not expression[0].isalpha() and len(expression) > 1:
        print("Invalid identifier")
    elif len(expression) == 1:
        new_exp = expression[0].split("=")
        variables[new_exp[0]] = new_exp[1]
    elif len(expression) == 2:
        if not expression[1].isalpha() and not expression[1].isdigit():
            print("Invalid assignment")
        else:
            variables[expression[0].strip("=")] = expression[1].strip("=")
    elif len(expression) == 3:
        if expression[2].isalpha():
            variables[expression[0]] = variables[expression[2]]
        elif not expression[2].isalpha() and not expression[2].isdigit():
            print("Invalid assignment")
        else:
            variables[expression[0]] = expression[2]
    else:
        print("Invalid assignment")


def command(com):
    if com == "/exit":
        return "Bye!"
    if com == "/help":
        return "This is a smart calculator with many functions"
    return "Unknown command"


def main():
    while True:
        nums = input().split()
        if len(nums) == 1:
            if nums[0][0] == "/":
                print(command(nums[0]))
                if nums[0] == "/exit":
                    break
            elif "=" in nums[0]:
                assign_variables(nums)
                continue
            elif nums[0].isalpha():
                try:
                    print(variables[nums[0]])
                except Exception:
                    print("Unknown variable")
            elif nums[0].strip("-").isnumeric():
                print(nums[0])
            else:
                if isinstance(nums[0], str):
                    post = to_postfix(nums[0])
                else:
                    post = to_postfix(nums)
                if isinstance(post, str):
                    print(post)
                    continue
                total = get_total(post)
                if total is None:
                    print(to_postfix(nums))
                print(total)
        elif len(nums) != 0:
            if "=" in nums[0] or "=" in nums[1]:
                assign_variables(nums)
            else:
                post = to_postfix(nums)
                if isinstance(post, str):
                    print(post)
                    continue
                total = get_total(post)
                if total is None:
                    print(to_postfix(nums))
                print(total)


main()
