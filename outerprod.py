nums = [2, 3, 3, 8]

for i in range(len(nums)):
    print("\n", "\t" * i, end="")
    for j in range(i, len(nums)):
        print(nums[i]*nums[j], end="")
        print("  ",end="")
