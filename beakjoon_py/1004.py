T=int(input())
for i in range(T):
    x1, y1, x2, y2=map(int,input().split())
    n=int(input())
    count=0
    for i in range(n):
        cx, cy, r=map(int, input().split())
        if ((x1-cx)**2+(y1-cy)**2<r**2 and (x2-cx)**2+(y2-cy)**2>r**2) or ((x1-cx)**2+(y1-cy)**2>r**2 and (x2-cx)**2+(y2-cy)**2<r**2):
            count+=1
    print(count)