a,b,c=map(int,input().split())
if a==b==c:
    mon=10000+a*1000
elif a==b:
    mon=1000+a*100
elif b==c:
    mon=1000+b*100
elif c==a:
    mon=1000+c*100
else:
    M=a
    if b>M:
        M=b
    if c>M:
        M=c
    mon=M*100
print(mon)