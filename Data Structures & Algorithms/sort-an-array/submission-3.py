import random
class Solution:
    def partition(self, nums, low, high):
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        pivot = nums[high]

        i = low-1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                self.swap(nums, i, j)
        
        self.swap(nums, i+1 , high)
        return i+1
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def quickSort(self, nums, low, high):
        if low < high:
            pid = self.partition(nums, low, high)
            self.quickSort(nums, low, pid-1)
            self.quickSort(nums, pid+1, high)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        # sorting algorithms
        # quick, bubble, insertion, selection, merge, heap
        
        # quick sort - chose a pivot, partition on pivot elem, return pivot indx andrecusrive call
        # on quick sort on lef thalf of pivot indx and right half. 
        # partition func will keep all elm less than pivot towards left, with an i pointer, and at the end 
        # swap pivot lemt with last i pointer (choose pivot as high idx to start)
        # Avg O(nlogn) , worst case O(n2)

        # insertino sort - pick each elem, put it in right pos at left, O(n2)

        # bubble sort - O(n2) - swap neighbour elm through the array, do it for n times.

        # selection sort - O(n2) - find the smallest elm, put it in fiorst place,
        # find second smallest from indx 1, put it in 1 ind, anD SO ON

        # merge sort - O(nlogn) - find mid, recursively call merge sort on lef thalf and right half
        # and then merge the two halfes returned.
        # merge func will create two temp array for left and right,
        # replace from left to end in sorted order in org arr.


        # quick sort
        return self.quickSort(nums,0,len(nums)-1) 

        