class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Stores indices
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # Pop elements from the stack until top element of stack is no longer less than current element
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = i - j   

            stack.append(i)

        return output