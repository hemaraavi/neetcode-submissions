class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_result = [0]*len(temperatures)
        stack = []
        for i in range(0,len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    prev_temp = stack.pop()
                    output_result[prev_temp] = i - prev_temp
                stack.append(i)
        return output_result