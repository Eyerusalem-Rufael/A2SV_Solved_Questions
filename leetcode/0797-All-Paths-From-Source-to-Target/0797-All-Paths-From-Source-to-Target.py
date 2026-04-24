class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        queue = [(0,[0])] #add curr_node and the path
        res = []
        while queue:
            curr_node , path = queue.pop(0)
            if curr_node == end:
                res.append(path)
                continue
            for neigh in graph[curr_node]:
                queue.append((neigh,path + [neigh]))
            
        return res