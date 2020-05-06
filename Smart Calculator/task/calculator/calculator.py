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
        if(nums[0] == "/help"):
            print("The program calculates the sum of numbers")
            continue
        print(nums[0])
    elif len(nums) != 0:
        summation = 0
        for x in nums:
            summation += int(x)
        print(summation)
