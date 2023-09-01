def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def binary_search(element, arr):
    first = 0
    last = len(arr) - 1
    resultOK = False
    result = None
    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == element:
            resultOK = True
            result = mid
            break
        elif arr[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    return resultOK, result

unsorted_lst = [5, 2, 8, 1, 9]
sorted_lst = bubble_sort(unsorted_lst)
print('Отсортированный список:', sorted_lst)
target = 8
resultOK, result = binary_search(target, sorted_lst)

if resultOK:
    print(f"Элемент найден на позиции {result}.")
else:
    print("Элемент не найден.")
