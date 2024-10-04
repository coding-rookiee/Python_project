T=int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2=map(int, input().split())
    l=((x1-x2)**2)+((y1-y2)**2)
    if l==0 and r1==r2: print(-1)
    elif l<(r1+r2)**2 and ((r1-r2)**2)<l: print(2)
    elif l==(r1+r2)**2 or ((r1-r2)**2)==l: print(1)
    else: print(0)