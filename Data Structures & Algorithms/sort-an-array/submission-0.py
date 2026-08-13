class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==0 or n ==1:
            return nums
        m = n//2
        L = self.sortArray(nums[0:m])
        R = self.sortArray(nums[m:])

        l_len = len(L)
        r_len = len(R)
        l =0 
        r= 0
        new_arr = [0] * n
        i = 0
        while l < l_len and r < r_len:
            if L[l] < R[r]:
                new_arr[i] = L[l]
                l=l+1
            else:
                new_arr[i] = R[r]
                r = r+1
            i= i+1

        while l < l_len:
            new_arr[i] = L[l]
            l=l+1
            i= i+1
        
        while r < r_len:
            new_arr[i] = R[r]
            r=r+1
            i= i+1
        return new_arr