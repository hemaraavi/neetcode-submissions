class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_array =[[] for _ in range(len(nums) + 1)]
        return_arr = []
        for each_num in nums:
            count[each_num] = 1+count.get(each_num,0)
        for each_item,count_item in count.items():
            freq_array[count_item].append(each_item)
        for each_freq in range(len(freq_array)-1,0,-1):
            for i in freq_array[each_freq]:
                return_arr.append(i)
                if len(return_arr) == k:
                    return  return_arr
        return return_arr

        