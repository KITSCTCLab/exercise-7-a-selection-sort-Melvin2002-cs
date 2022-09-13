from typing import List

def swap(arr,j,k):
  temp=arr[j]
  arr[j]=arr[k]
  arr[k]=temp

def selectionSort(array, size) -> List[int]:
  # Write your code here
  if size==1:
    return array
  for i in range(0,size-1):
    low=i
    execution=0
    for j in range(i+1,size):
      if array[low]>array[j]:
        low=j
        execution=1
    if execution!=0:
      swap(array,i,low)
  
  
  

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
