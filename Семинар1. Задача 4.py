a = int(input())
cnt = 0
while a % 10 == 0:
    cnt += 1
    a /= 10
print(cnt)