class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # "potential" = height + (len(heights) - index)
        
        pointer1 = 0
        pointer2 = len(heights) - 1
        max_area = 0
        first = True

        while pointer1 < pointer2:
            area = min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1)

            cachedp1, cachedp2 = pointer1, pointer2

            p1_area = area
            while p1_area <= max_area and pointer1 < pointer2:
                pointer1 += 1
                p1_area = min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1)

            possiblep1 = pointer1
            pointer1 = cachedp1
            p2_area = area

            while p2_area <= max_area and pointer1 < pointer2:
                pointer2 -= 1
                p2_area = min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1)

            possiblep2 = pointer2
            pointer2 = cachedp2

            # print(p1_area,p2_area,area)

            if p1_area > p2_area and p1_area > area:
                pointer1 = possiblep1
                area = p1_area
            elif p2_area > area:
                pointer2 = possiblep2
                area = p2_area

            if pointer1 == cachedp1 and pointer2 == cachedp2 and not first:
                pointer2 -= 1

            max_area = max(max_area, area)
            first = False

            # print(pointer1, pointer2, max_area)
        
        return max_area

