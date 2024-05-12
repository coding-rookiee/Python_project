h,m=map(int,input().split())
n=int(input())
m+=n
if (m>59):
    h+=m//60
    m%=60
    if (h>23):
        h-=24
print(h,m)