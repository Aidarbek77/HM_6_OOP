def binary_search(arr, x):

  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2

    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      return mid

  return -1

# Пример использования
my_list = [2, 3, 4, 10, 40]
x = 10

my_list.sort()

result = binary_search(my_list, x)

if result != -1:
  print("Элемент", str(x), "найден в индексе", str(result))
else:
  print("Элемент", str(x), "не найден в списке")