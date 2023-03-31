import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
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
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans
            
        
        
        
            
        