# bubble sort

a = int(input("Enter the size of the array : "))
arr = []

for i in range (a):
    n = int(input(f"Enter the number {i} : "))
    arr.append(n)

print(f"The entered array of size {a} is : {arr}")

for i in range (0, a - 1):
    for j in range(0, a - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"The sorted array is : {arr}")
