def radix_sort(data):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(data)
    exp = 1

    while maxVal // exp > 0:

        while len(data) > 0:
            val = data.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
             val = bucket.pop()
             data.append(val)

        exp *= 10
    return data

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

elements = int(input("How many elements: "))
array = []
for x in range(elements):
    try:
       element = int(input(f"Element[{x+1}]: "))
       if element < 0:
        print("Bilangan tidak boleh negatif")
       else:
        array.append(element)
    except:
       print("Harus bilangan bulat")

print(f'Sebelum sorting: {array}')

radixResult = radix_sort(array)
mergeResult = mergeSort(array)
print('\nSetelah Sorting')
print(f"Hasil Sorting Radix: {radixResult}")
print(f"Hasil Sorting Merge: {mergeResult}")