# calculator.py
# written by Natasha Graham
# JetBrains and Hyperskills Python course


to_exit = False
while not to_exit:
    nums = input().split()
    if len(nums) == 1:
        if(nums[0] == "/exit"):
            to_exit = True
            print("Bye!")
            break
        print(nums[0])
    elif len(nums) == 2:
        print(int(nums[0]) + int(nums[1]))
