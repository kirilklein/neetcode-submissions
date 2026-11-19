class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we use a stack
        # we store farthest start indices
        # example
        # [(0,3), (2,6), (4,5)]
        # [1, 2, 4]
        start_ids = []
        stack = []
        max_area = 0
      
        for i, h in enumerate(heights):
   
            if i==0 or not stack:
                stack.append(h)
                start_ids.append(i)
                max_area = h
                continue
        

            if h>stack[-1]: # simply append doesn't need anythign else
                stack.append(h)
                start_ids.append(i)


            else: # h<stack[-1]
                while stack and h<stack[-1]: 
                    last_height = stack.pop()
                    start_id = start_ids.pop()
                    new_area = last_height * (i - start_id) # actually e.g. 2-0 for index 1
                    max_area = max(max_area, new_area)
                if stack and h==stack[-1]: # special case we don't want to overwrite the start idx
                    continue
                else: 
                    stack.append(h)
                    start_ids.append(start_id)
                    max_area = max(max_area, h)
        
        # now compute areas for remaining stack 
        while stack:
            h = stack.pop()
            start_id = start_ids.pop()
            max_area = max(max_area, h * (len(heights) - start_id)) 
        return max_area
## ! make sure to set start index to what we pop and not to current start index
        
