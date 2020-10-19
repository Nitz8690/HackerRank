'''Task

Given an array, , of

integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of
decimal place (i.e., , format).'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from  statistics import mean,median,mode
N = int(input())

arr = [int(i) for i in input().split(' ')]
#mean = sum(arr/N)
arr.sort()

print('{0:.1f}'.format(sum(arr)/N))

if N % 2 == 0:
    median = (arr[N//2] + arr[(N//2) - 1])/2
else:
    median = arr([N//2])

print('{0:.1f}'.format(median))

counts = []
for i in arr:
    counts.append(arr.count(i))

if max(counts)>1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))

