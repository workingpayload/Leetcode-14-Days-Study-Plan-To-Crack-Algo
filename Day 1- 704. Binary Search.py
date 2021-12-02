class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid_index = 0
        while(l<=r):
            mid_index = (l+r)//2
            mid_number= nums[mid_index]
            
            if mid_number==target:
                return mid_index
            if mid_number<target:
                l = mid_index+1
            else:
                r = mid_index-1
        return -1        
        
