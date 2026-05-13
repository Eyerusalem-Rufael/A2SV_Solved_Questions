class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        heap = []
        result = []
        tasks = sorted(enumerate(tasks),key = lambda x : x[1])
        # print(tasks)
        idx = time = 0
        while idx < n or heap:
            while idx < n and tasks[idx][1][0] <= time:
                heapq.heappush(heap,(tasks[idx][1][1],tasks[idx][0])) # processing time,position
                idx += 1

            if not heap:
                time = tasks[idx][1][0]
                continue
            proccesing_time , ind = heapq.heappop(heap)
            time += proccesing_time
            result.append(ind)

        return result