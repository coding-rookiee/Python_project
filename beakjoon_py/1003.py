'''
li=[0, 1]
def fi(n):
    if len(li)>n:
        return li[n]
    else:
        li.append(fi(n-1)+fi(n-2))
        return fi(n-1)+fi(n-2)
T=int(input())
for i in range(T):
    n=int(input())
    fi(n)
    if n==0:
        print(1, 0)
    elif n==1:
        print(0, 1)
    else:
        print(li[n-1], li[n])
'''
import sys
T=int(sys.stdin.readline())
for i in range(T):
    n=int(sys.stdin.readline())
    a, b=1, 0
    for j in range(n):
        a, b=b, a+b
    print(a, b)