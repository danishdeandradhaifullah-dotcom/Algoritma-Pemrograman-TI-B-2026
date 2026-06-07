def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print(f"Data: {data} ")

find = int(input("Masukkan nilai yang dicari: "))
linear = linearSearch(data, find)
binary = binarySearch(data, find)

if linear != -1:
  print("\nLinear search ketemu dengan index: ", linear)
else:
  print("\nNot found")   

print("\nSebelum disort:") 
if binary != -1:
  print("Binary search ketemu dengan index: ", binary)
else:
  print("Not found")   

data.sort()
binary = binarySearch(data,find)
print("\nSetelah disort:")
if binary != -1:
  print("Binary search ketemu dengan index: ", binary)
else:
  print("Not found") 