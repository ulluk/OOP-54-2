nums = (2, 7, 11, 15)
num = 9



def sumer(arr, target):
    target_index = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if nums[i] + nums[j] == target:
                target_index = [i, j]
                break
        if target_index:
            break
    return target_index

print(sumer(nums,num))