def selectionSort(list):
    n = len(list)
    for i in range(n):
        minimumIndex = i
        for j in range(i + 1, n):
            if list[j] < list[minimumIndex]:
                minimumIndex = j
        list[i], list[minimumIndex] = list[minimumIndex], list[i]
    return list


myList = [54, 26, 93, 17, 77, 31, 44, 55, 8978, 521, 254, 654, 32, 41, 5, 54, 56, 20]
print(selectionSort(myList))
