class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                #step 1: build hash map: character and how often it appears
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        #step 2: keep track of the top k frequent element in minheap
        maxHeap = []
        for key in dic:
                heapq.heappush(maxHeap, (-dic[key], key))

        #step 3: return the top k element from the minHeap
        return [heapq.heappop(maxHeap)[1] for _ in range(k)]