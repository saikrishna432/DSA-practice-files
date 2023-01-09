

## print duplicates in the string      
dct={}

s = "geeksforgeeks"
l= dct.keys()
for i in s:
    if i in l:
        dct[i]=dct[i]+1
    else:
        dct[i]=1

for i in dct:
    if dct[i]>1:
        # print(i,", count=",dct[i])
        continue
        



##reverse a string


s = "test string"

l=s[::-1]
# print(l)
    

## Check weather string is a pallanedrim or not

# l=s[::-1]
# if l==s:
#     # print(s,"is a palindrome")
# else:
#     # print(s,"is not a palindrome")



# Python3 program to print sums of
# all possible subsets.
 
# Prints sums of all subsets of arr[l..r]
 
 
# def subsetSums(arr, l, r, sum=0):
 
#     # Print current subset
#     print(l,r)
#     if l > r:
#         print(sum, end="\n")
#         return
#     # print(sum, end="\n")
 
#     # Subset including arr[l]
#     subsetSums(arr, l + 1, r, sum + arr[l])
#     # print(sum, end="\n")
 
#     # Subset excluding arr[l]
#     subsetSums(arr, l + 1, r, sum)
#     # print(sum, end="\n")
 
 
# # Driver code
# arr = [5, 4]
# n = len(arr)
# subsetSums(arr, 0, n - 1)



# def subsetSums(arr, l, r, sum=0):
 
#     # Print current subset
#     print(l,r)
#     if l > r:
#         print(sum, end="\n")
#         return
 
#     # Subset including arr[l]
#     subsetSums(arr, l + 1, r, sum + arr[l])

#     # Subset excluding arr[l]
#     subsetSums(arr, l + 1, r, sum)
 
# # Driver code
# arr = [5, 4]
# n = len(arr)
# subsetSums(arr, 0, n - 1)



# Iterative Python3 program to print sums of all possible subsets
 
# Prints sums of all subsets of array
def subsetSums(arr, n):
    # There are total 2^n subsets
    total = 1 << n
 
    # Consider all numbers from 0 to 2^n - 1
    for i in range(total):
       Sum = 0
 
       # Consider binary representation of
       # current i to decide which elements
       # to pick.
       for j in range(n):       
          if ((i & (1 << j)) != 0):            
              Sum += arr[j]
 
       # Print sum of picked elements.
       # print(Sum, "", end = "")
 
arr = [ 5, 4 ]
n = len(arr)
 
subsetSums(arr, n);


#Chocklete Distribution problem

def findmindiff(arr,n,m):
    if m==0 & n==0:
        return 0
    if m>n:
        return -1
    
    a=sorted(arr)
    print(a)
    i=0
    min_diff=a[i+m-1]-a[i]
    
    for i in range(n-m+1):
        if min_diff>=(a[i+m-1]-a[i]):
            min_diff=(a[i+m-1]-a[i])
    return min_diff
    
    
    
    
if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
    m = 7  # Number of students
    n = len(arr)
    print("Minimum difference is", findmindiff(arr, n, m))

# Python Program to search an element in a sorted and pivoted array
 
# Searches an element key in a pivoted
# sorted array arrp[] of size n
def pivotedBinarySearch(arr, n, key):
 
    pivot = findPivot(arr, 0, n-1)
 
    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)
 
    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    return binarySearch(arr, pivot + 1, n-1, key)
 
 
# Function to get pivot. For array
# 3, 4, 5, 6, 1, 2 it returns 3
# (index of 6)
def findPivot(arr, low, high):
 
    # base cases
    if high < low:
        return -1
    if high == low:
        return low
 
    # low + (high - low)/2;
    mid = int((low + high)/2)
 
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)
 
# Standard Binary Search function
def binarySearch(arr, low, high, key):
 
    if high < low:
        return -1
 
    # low + (high - low)/2;
    mid = int((low + high)/2)
 
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key)
    return binarySearch(arr, low, (mid - 1), key)
 
 
# Driver program to check above functions
# Let us search 3 in below array
if __name__ == '__main__':
    arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    n = len(arr1)
    key = 3
    print("Index of the element is : ", \
          pivotedBinarySearch(arr1, n, key))
 

