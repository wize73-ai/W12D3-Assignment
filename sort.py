###  Ive tried three approaches to the sorting problem number 912 sort an array.

# Findings:

# Bubble sort failed to complete, threw time limit exceeded 
# quick sort failed the same way.

# The merge sort was the only algorithm to pass the test cases. and had a big O of n log n, whereas the quick and bubble sorts both required loops in loops without built in methods improving efficiency.


# QuickSort:

# QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quick_sort(arr, low, high):
            if low < high:
                # Partition the array and get the pivot index
                pi = partition(arr, low, high)

                # Recursively sort elements before and after partition
                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)
        
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            j = low

            while j <= high - 1:
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        # Calculate the length of the array without using len()
        n = 0
        for _ in nums:
            n += 1

        quick_sort(nums, 0, n - 1)
        return nums



# Bubble Sort:

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 


def bubble_sort(nums):
    n = 0
    for _ in nums:
        n += 1

    # Bubble Sort algorithm
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j += 1
        i += 1

    return nums


# Merge Sort:


# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
# 
# 
# 

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0

        # Manually calculating the lengths of left and right arrays
        len_left = len_right = 0
        for _ in left:
            len_left += 1
        for _ in right:
            len_right += 1

        while i < len_left and j < len_right:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len_left:
            result.append(left[i])
            i += 1

        while j < len_right:
            result.append(right[j])
            j += 1

        return result

    # Manually calculating the length of the array
    n = 0
    for _ in arr:
        n += 1

    if n > 1:
        mid = n // 2

        # Dividing the array manually
        left = []
        right = []
        i = 0
        for item in arr:
            if i < mid:
                left.append(item)
            else:
                right.append(item)
            i += 1

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)
    else:
        return arr
