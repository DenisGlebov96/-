s = input()
c = input()
cnt = 0
for i in range(0,len(s)):
    if s[i] == c:
        #print(s[i])
        index = i
        cnt += 1
    if cnt == 2:
        print(index)
        break
else:
    print ('Данный символ не повторяется')