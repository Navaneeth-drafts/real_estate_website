
arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

print("First Element:", arr[0])
print("Last Element:", arr[-1])

arr.append(60)      
print("After append(60):", arr)

arr.insert(2, 25)
print("After insert(2, 25):", arr)

arr.remove(40)      
print("After remove(40):", arr)

popped = arr.pop()
print("After pop():", arr)
print("Popped element:", popped)

print("Index of 30:", arr.index(30))

arr.sort()
print("Sorted Array:", arr)

arr.reverse()
print("Reversed Array:", arr)


print("Array Length:", len(arr))


# reversing a list in python 
arr = [10, 20, 30, 40, 50]
print("Original Array:", arr)
for i in range(0,len(arr)):
    arr[i] = arr[len(arr) - i - 1]
print("Reversed Array:", arr)

# finding the minimum element in the array 
# Example array
arr1 = [12, 5, 7, 19, 22, 25, 3]

# Assume first element is the minimum
minimum = arr1[0]

# Loop through array
for num in arr1:
    if num < minimum:
        minimum = num

print("Minimum element in the array is:", minimum)


def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated Array:", rotate_array(arr, k))

# reversing in groups
# finding the second largest element in an array
def secondlargest(arr,n):
    largest = float('-inf')
    sec_lar = float('-inf')
    for i in arr:
        if i > largest:
            sec_lar = largest
            largest = i
        elif i > sec_lar and i != largest:
            sec_lar = i
    return sec_lar

def reverse_in_groups(arr, n, k):
    for i in range(0, n, k):
        start = i
        end = min(i + k - 1, n - 1)
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return arr

# reverse of a string

def reverse_string(s):
    return s[::-1]

# palindrome string 

def is_palindrome(s):
    return s == s[::-1]

