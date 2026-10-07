class Union:
    def __init__(self, n):
        self.parent=[i for i in range(n)]
        self.size=[1] * n #initialize every set to size 1
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x]=self.find(self.parent[x]) #path compression
        return self.parent[x]

    def union(self,x,y):
        x_root=self.find(x)
        y_root=self.find(y)
        if x_root == y_root:
            return False
        #must merge!
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root #ensure x is always bigger
        self.parent[y_root]=x_root
        self.size[x_root] += self.size[y_root]
        return True
    def connected(self, x, y):
        return self.find(x)==self.find(y)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1!=len(edges):
            return False
        #check for cycles and connctivity (equivalent) both are O(v+e) but cycle detection can exit earlier
        dsu=Union(n)
        for i in range(len(edges)):
            if not dsu.union(edges[i][0],edges[i][1]):
                return False
        return True
        

        #alternatively, dfs visiting a non-parent node means it has a cycle
        