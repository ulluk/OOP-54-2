# class Counter:
#     def __init__(self,limit):
#
#         self.current = 0
#         self.limit = limit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.limit:
#             num = self.current
#             self.current += 1
#             return num
#         else:
#             raise StopIteration
#
#
# for i in Counter(5):
#     print(i)



#
# def counter_up_tp(limit):
#     current = 0
#     while current < limit:
#         yield current
#         current += 1
#
# for num in counter_up_tp(5):
#     print(num)
#


# def binary_serch(lst, target):
#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         print(mid)
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "None"
#
# my_array = [1,4,6,7,8,10,14,20]

# print(binary_serch(my_array, 20))


tt = [1,4,24,72,11,33,53,1,4,64,2,6,8,0]


def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

buble_sort(tt)
print(tt)


    