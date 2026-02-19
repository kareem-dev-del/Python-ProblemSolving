#1-(Factorial) using while
def factorial(num):
    i=1
    count=1
    while i <= num:
        count*=i
        i+=1
    return count    
print(factorial(5))

#2-(Factorial) using recursion

def factorial(num):
    if num == 0 or num == 1:return num
    return num * factorial(num - 1)
print(factorial(5))

#3-(Factorial) using for

def factorial_(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

