#미완

'''
import sys
n=int(sys.stdin.readline())
t=[0]*10
for i in range(1,n+1):
    ii=i
    while ii>0:
        nn=ii%10
        ii=ii//10
        for j in range(10):
            if j==nn:
                tt=t[j]+1
                del t[j]
                t.insert(j, tt)
for i in range(10):
    print(t[i], end=" ")
'''
n=int(input())
t=[0]*10
nn=1
while nn<=n:
    nn%10