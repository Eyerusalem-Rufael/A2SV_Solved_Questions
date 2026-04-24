"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(id):
            importance = emplo_id[id].importance
            for i in emplo_id[id].subordinates:
                importance += dfs(i)
            return importance

        emplo_id = {id.id : id for id in employees}
        return dfs(id)