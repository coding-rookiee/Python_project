
N,M=map(int,input().split())
n=list(range(N+1))
for k in range(M):
    i,j=map(int,input().split())
    n[i:j+1]=n[j:i-1:-1]
for k in range(1, N+1):
    print(n[k], end=" ")
