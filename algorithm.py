

import math
import hashlib
import requests


# 二分查找,时间复杂度O(log n)
def binary_search(arr:list, item:int) -> int:

    counts = 0 # 次数
    low = 0
    high = len(arr) - 1
    while low <= high:
        counts += 1
        mid = (low + high) // 2
        guess = arr[mid]
        # print('low:', str(low).rjust(3), 'high:', high, 'mid:', mid)
        if guess == item:
            print('count:', counts)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

arr1 = list(range(100))
print('index:', binary_search(arr1, 25))
print(math.log2(64))

# 快速排序
def quick_sort(arr):
    low = []
    high = []
    mid = []
    if len(arr) <= 1:
        return arr
    base = arr[0]
    # print('base:', base)
    for i in arr:
        if i < base:
            low.append(i)
        elif i > base:
            high.append(i)
        else:
            mid.append(i)
    # print('low:', low)
    # print('mid:', mid)
    # print('high:', high)
    # print('---------------')
    low = quick_sort(low)
    high = quick_sort(high)
    return low + mid + high
arr = [6,1,2,7,9,3,4,5,10,8]
print(quick_sort(arr))


# 快速排序
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    base = arr[0]
    low = [i for i in arr[1:] if i <= base]
    high = [i for i in arr[1:] if i > base]
    print('low:', low)
    print('high:', high)
    # low = quick_sort2(low)
    high = quick_sort2(high)
    return low + high
arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(quick_sort2(arr))

# 自然数之和
def sum(a:int):
    s = 0
    for i in range(a + 1):
        s = s + i
    return s

sum(100)

# 选择排序:对数组排序,时间复杂度O(n2)
def find_smallest(arr:list):
    new_arr = []
    for i in range(len(arr)):
        a = arr[0]
        # 取最小元素
        for i in arr:
            if a > i:
                a = i
        new_arr.append(a)
        arr.remove(a)
    return new_arr
arr = [6,2,9,1,0,4,-1,34,788,-45]

def cpnd():
    print('cnpdhas;dkf')
    print('我思故我在')