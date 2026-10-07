class Union:
    def __init__(self, n):
        self.parent=[i for i in range(n)] #each node is its own parent to begin
        self.size=[1] * n
        self.num_sets=n
    
    def find(self, x):
        if self.parent[x] != x: #ur someone elses bitch
            self.parent[x] = self.find(self.parent[x]) #recursive path halving/compression
        return self.parent[x]


    def union(self,x,y):
        xr, yr=self.find(x), self.find(y) #find the roots
        if xr==yr:
            return False #theyre already the same, not gonna merge them
        if self.size[xr] < self.size[yr]:
            xr, yr= yr, xr #xr is now always the bigger one :)
        self.parent[yr]=xr
        self.size[xr] += self.size[yr]
        self.num_sets -=1 #decrement the number of sets since we just merged two of them
        return True
        

    def num_components(self):
        return self.num_sets


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs can be used to count the number of connected components in the graph? yes but requires adj list. First lets try dsu again
        #basically we return the number of unique roots
        dsu=Union(n)
        #add edges to dsu
        for i in range(len(edges)):
            dsu.union(edges[i][0],edges[i][1])

        return dsu.num_components()