### TASK 3

'''
Given an array, , of integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and are integers. '''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean, median, mode

N = int(input().strip())

def find_median(x):

    if  len(x) % 2 == 0:
        median = (x[len(x)//2] + x[len(x)//2 - 1])/2
    else:
        median = x[len(x)//2]
    return median


arr = [int(i) for i in input().split(' ')]
arr.sort()
q2 = find_median(arr)

q1_arr = [i for i in arr if i < q2]
q3_arr = [i for i in  arr if i > q2]

q1 = find_median(q1_arr)
q3 = find_median(q3_arr)

print(int(q1))
print(int(q2))
print(int(q3))

