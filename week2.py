# Assignment 1:
# Implement following Pseudo Code in the programming language of your choice (keep it OOP).

# Input array A contains only integers from 1 to M
# algorithm CountSort(A[1,…,n])
# 	B[1…M] <- [0,…,0] // Declare array with the length M
# 	For j = 1 to n
# 		B[A[j]] <- B[A[j]] + 1
# 	For i = 2 to M
# 		B[i] <- B[i] + B[i-1]
# 	For j = n to 1
# 		A’[B[A[j]]] <- A[j]
# 		B[A[j]] <- B[A[j]] – 1

# Find out the complexity of this Algorithm.

class CountSort:
    def __init__(self, array, max_val):
        self.array = array
        self.max_val = max_val
        self.sorted_array = []

    def sort(self):
        # Initialize count array with zeros
        count = [0] * (self.max_val + 1)

        # Store the count of each element in count array
        for num in self.array:
            count[num] += 1

        # Store the cumulative count
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array,
        # and place the elements in output array
        self.sorted_array = [0] * len(self.array)
        i = len(self.array) - 1
        while i >= 0:
            self.sorted_array[count[self.array[i]] - 1] = self.array[i]
            count[self.array[i]] -= 1
            i -= 1

        return self.sorted_array
    
def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        # Decrement j until we find a value less than x
        while True:
            j -= 1
            if A[j] <= x:
                break
        
        # Increment i until we find a value greater than x
        while True:
            i += 1
            if A[i] >= x:
                break
        
        # If pointers have crossed, return the index j
        if i < j:
            A[i], A[j] = A[j], A[i]  # Swap the values
        else:
            return j

def quicksort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        i = 0
        for j in range(len(arr) - 1):
            if arr[j + 1] < pivot:
                arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
                i += 1
        arr[0], arr[i] = arr[i], arr[0]
        first_part = quicksort(arr[:i])
        second_part = quicksort(arr[i + 1:])
        first_part.append(arr[i])
        return first_part + second_part


# Example usage:
# count sort
input_array = [1, 4, 1, 2, 7, 5, 2, 9, 5, 3, 5, 4]
max_val = max(input_array)  # Find the maximum value in the array for the count array size
sorter = CountSort(input_array, max_val)
sorted_array = sorter.sort()

print("Sorted array:", sorted_array)

# Example usage:
# hoare partition
A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
index = hoare_partition(A, 0, len(A) - 1)
print("Partitioned index:", index)
print("Partitioned array:", A)
print("Quick sort result:", quicksort(A))
