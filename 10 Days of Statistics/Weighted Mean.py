### TASK

'''
Given an array, , of integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of decimal place (i.e., format). '''



# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

x_arr = [int(i) for i in input().strip().split(' ')]
w_arr = [int(i) for i in input().strip().split(' ')]

sum1 = 0 
for  i  in range (N):
    sum1 = sum1 + x_arr[i] * w_arr[i]

print('{0:.1f}'.format(sum1/sum(w_arr)))
