#Recursion
#tail recursion
'''def fun(n):
    if n==0:
        return
    print(n,end=" ")#5 4 3 2 1
    fun(n-1)
    
n=int(input())
fun(n)'''

#head recursion
'''def fun(n):
    if n == 0:
        return 200
#   r=fun(n-1)
    print(n, end=" ")#1 2 3 4 5
    r=fun(n-1)
    return r
n = int(input())
print(fun(n))'''

#5 4 3 2 1 1 2 3 4 5
'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ")
n = int(input())
(fun(n))'''

#5 4 3 2 1 2 3 4 5 
'''def fun(n):
    if n==0:
        return
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ")
n = int(input())
(fun(n))'''

#odd numbers
'''def fun(n):
    if n==0:
        return
    if n%2!=0:
        print(n,end=" ")
    fun(n-1)
    if n%2!=0:
        print(n,end=" ")
n = int(input())
(fun(n))'''

#1 2 3 4 5 5 4 3 2 1
'''def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    print(m+1,end=" ")
n = int(input())
fun(n)'''

#1 2 3 4 5 4 3 2 1
'''def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    if m+1!=n:   #if m!=n-1:
        print(m+1,end=" ")
n = int(input())
fun(n)'''

#factorial
'''def fun(n):
    if n<0:
        return None
    elif n==0:
        return 1
    else:
        return n*fun(n-1)
n=int(input())
print(fun(n))'''

##odd number
'''def fun(n):
    if n==0:
        return
    fun(n-1)
    if n%2!=0:
       print(n,end=" ")
n = int(input())
(fun(n))'''
#.even numbers
'''def fun(n):
    if n==0:
        return
    fun(n-1) 
    if n%2==0:
        print(n,end=" ")
n = int(input())
(fun(n))'''
#prime or not
'''n=int(input())
flag=0
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        flag+=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")'''

#prime or not using recursion
'''def is_prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
n=int(input())
if is_prime(n):
    print("prime number")
else:
    print("not prime number")'''

#reverse of a number using recursion
'''def reverse(n,rev=0):
    if n==0:
        return rev
    rev=rev*10+n%10
    return reverse(n//10,rev)
n = int(input())
print(reverse(n))'''

#min steps
'''def fun(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+fun(n//2)
    else:
        return 1+min(fun(n-1),fun(n+1))
n = int(input())
print(fun(n))'''

#sum of all the elements in the list using recursion
'''def fun(num):
    if not num:
        return 0
    return num[0] + fun(num[1:])
n = list(map(int,input().split()))
print(fun(n))'''

#count number of prime numbers in a list using recursion
def fun(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def count(num):
    if not num:
        return 0
    if fun(num[0]):
        return 1 + count(num[1:])
    else:
        return count(num[1:])
n=list(map(int, input().split()))
print(count(n))

















