###  Task5


'''
Given an array, , of integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of decimal place (i.e., format). An error margin of will be tolerated for the standard deviation. '''


import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().split()))

    mean = sum(X) / N
    std = (sum((x - mean)**2 for x in X) / N)**0.5

    print('%0.1f' % std)
