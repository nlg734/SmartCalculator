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


def get_total(equation):
    try:
        result = int(equation[0])
    except (TypeError, ValueError):
        try:
            result = int(variables[equation[0]])
        except Exception:
            print("Unknown variable")
            return None
    for i in range(1, len(equation), 2):
        operation = find_operation(equation[i])
        if operation == "+":
            try:
                result += int(equation[i + 1])
            except (TypeError, ValueError):
                try:
                    result += int(variables[equation[i + 1]])
                except IndexError:
                    print("Invalid expression")
                except Exception:
                    print("Unknown variable")
                    return None
        else:
            try:
                result -= int(equation[i + 1])
            except (TypeError, ValueError):
                try:
                    result -= int(variables[equation[i + 1]])
                except IndexError:
                    print("Invalid expression")
                except Exception:
                    print("Unknown variable")
                    return None
    return result


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
        if "=" in nums[0]:
            assign_variables(nums)
            continue
        try:
            print(int(nums[0]))
        except ValueError:
            try:
                print(variables[nums[0]])
            except Exception:
                print("Unknown variable")
    elif len(nums) != 0:
        if "=" in nums[0] or "=" in nums[1]:
            assign_variables(nums)
        else:
            total = get_total(nums)
            if total is not None:
                print(total)
