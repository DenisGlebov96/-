arr = [1,1,1,2] #как записать элементы в массив с клавиатуры
for i in range(1,len(arr)):
    if arr[0] == arr[i]:
        continue
    else:
        break
else:
    print('Все элементы массива одинаковые')