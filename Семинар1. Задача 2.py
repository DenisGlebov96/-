arr = [2,8,4,5,9,6,3,4]
N = int(input())
if len(arr) >= N: 
    print(arr[N-1]**N)
else:
    print(-1)