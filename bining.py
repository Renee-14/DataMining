import numpy as np


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def equal_freq(data, n):
    arr_len = len(data)
    depth = arr_len // n
    answer = []
    j = 0
    for i in range(depth):
        count = 0
        temp = []
        while count < depth and count + j < arr_len:
            temp.append(data[count + j])
            count += 1
        if len(temp) != 0:
            median = np.median(temp)
            temp_median = []
            for x in range(len(temp)):
                temp_median.append(median)
            answer.append(temp_median)
        j += depth
    return answer


def equal_width(data, m):
    w = (data[-1] - data[0]) // m
    range_arr = []
    j = 1
    prev = data[0]
    i = 0
    while i < data[-1]:
        i = data[0] + j * w
        if i > data[-1]:
            break
        range_arr.append([prev, i])
        prev = i
        j += 1
    print(range_arr)
    answer = []
    for interval in range_arr:
        temp = []
        for item in data:
            if item in range(interval[0], interval[-1] + 1):
                temp.append(item)
        if len(temp) != 0:
            median = np.median(temp)
            temp_median = []
            for x in range(len(temp)):
                temp_median.append(median)
            print(temp_median)
            answer.append(temp_median)
    return answer


print("Please press 1 to preform equal frequency binning \n")
print("Please press 2 to perform equal width binning \n")
user_input = int(input())

if user_input == 1:
    print("You have choosen equal frequency binning")
    data = input('Enter the data seperated by space')
    data = data.split()
    data = [int(x) for x in data]
    m = int(input("Please enter the no of bins you want to create"))
    data = bubbleSort(data)
    ans = equal_freq(data, m)
    print(ans)

elif user_input == 2:
    print("You have choosen equal width binning")
    data = input('Enter the data seperated by space')
    data = data.split()
    data = [int(x) for x in data]
    m = int(input("Please enter the no of bins you want to create"))
    data = bubbleSort(data)
    ans = equal_width(data, m)
    print(ans)
