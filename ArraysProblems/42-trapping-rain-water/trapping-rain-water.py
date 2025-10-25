class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, len(height)-1 
        leftMax, rightMax = height[left_pointer],height[right_pointer]
        res = 0 

        while left_pointer < right_pointer: 
            if leftMax < rightMax: 
                left_pointer += 1
                leftMax = max(leftMax, height[left_pointer])
                res += leftMax - height[left_pointer]
            else: 
                right_pointer -= 1
                rightMax = max(rightMax, height[right_pointer])
                res += rightMax - height[right_pointer]
        return res
