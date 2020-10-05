s = input()
cntlow = cntup = cntc = 0
for i in range(0,len(s)):
    if 'a' <= s[i] <= 'z':
        cntlow += 1
    if 'A' <= s[i] <= 'Z':
        cntup += 1
    if '0' <= s[i] <= '9':
        cntc += 1
print(cntlow), print(cntup), print(cntc)
if (cntlow > 0) & (cntup > 0) & (cntc > 0) & (len(s) >= 16):
    print('Пароль надежный')
else:
    print('Пароль ненадежный')