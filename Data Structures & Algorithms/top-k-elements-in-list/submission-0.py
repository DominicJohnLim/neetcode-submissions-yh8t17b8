class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        item_hash = {}
        
        for item in nums:
            item_hash[item] = 1 + item_hash.get(item, 0)
        
        sorted_hash = []
        for item in item_hash:
            sorted_hash.append([item, item_hash[item]])

        sorted_hash = sorted(sorted_hash, key=lambda x: x[1], reverse=True)

        stripped_items = []

        for item in sorted_hash:
            stripped_items.append(item[0])

        
        return stripped_items[0:k]