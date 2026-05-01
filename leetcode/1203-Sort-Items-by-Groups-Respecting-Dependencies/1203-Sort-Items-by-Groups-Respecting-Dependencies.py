class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def top_sort(graph,indegree,nodes):
            order = []
            queue = deque([i for i in nodes if indegree[i] == 0])
            while queue:
                node = queue.popleft()
                order.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)
            return order if len(order) == len(nodes) else [] 
       #giving id to non-groups
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        # print(group)
        item_graph = defaultdict(list)
        indegree_item = [0] * n
        group_graph = defaultdict(list)
        indegree_group = [0] * group_id

        for dep in range(n):
            for preq in beforeItems[dep]:
                item_graph[preq].append(dep)
                indegree_item[dep] += 1
        # print(indegree_item)
                if group[preq] != group[dep]: #in different group
                    group_graph[group[preq]].append(group[dep])
                    indegree_group[group[dep]] += 1
        #sort the groups
        graph_order = top_sort(group_graph,indegree_group[:],list(range(group_id)))
        if not graph_order:
            return []
        # print(graph_order)
        #sort the items
        item_order = top_sort(item_graph,indegree_item[:],list(range(n)))
        if not item_order:
            return []
        # print(item_order) 
        grouping = defaultdict(list)
        for i in item_order:
            grouping[group[i]].append(i)
        # print(grouping)

        ans = []
        for idx in graph_order:
            ans.extend(grouping[idx])
        return ans