class Graph:
    def __init__(self):
        self.graph={}
    def add_node(self,v):
        if v in self.graph:
            print(v,"already exist ")
        else:
            self.graph[v]=[]

    def add_edge(self,v1,v2):
        if  v1 not in self.graph:
            print(v1,"not present")
        elif v2 not in self.graph:
            print(v2,"not present")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def delete_node(self,v):
        if v not in self.graph:
            print("not present , cant delete")
        else:
            del self.graph[v]
            # self.graph.pop(v)
            for k in self.graph:
                list1=self.graph[k]
                if v in list1:
                    list1.remove(v)

    def delete_edge(self,v1,v2):
        if v1 not in self.graph:
            print("not present , cant delete")
        elif v2 not in self.graph:
            print("not present , cant delete")
        else:
            if v1 in self.graph[v2]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)


def dfs(node,graph):
    visited=set()
    if node not in graph:
        print("not present")
        return
    stack=[]
    stack.append(node)
    while stack:
        cur=stack.pop()
        if cur not in visited:
            print(cur)
            visited.add(node)
            for neigh in graph[cur]:
                stack.append(neigh)

# def dfs(node,visited,graph):
#     if node not in visited:
#         print(node,end=" ")
#         visited.add(node)
#         for neigh in graph[node]:
#             if neigh not in visited:
#                 dfs(neigh,visited,graph)

def bfs(node,graph):
    visited=set()
    queue=[]
    queue.append(node)
    while queue:
        cur=queue.pop(0)
        if cur not in visited:
            print(cur,end=" ")
            visited.add(cur)
            for neigh in graph[cur]:
                if neigh not in visited:
                    queue.append(neigh)


g1=Graph()
g1.add_node("A")
g1.add_node("B")
g1.add_node("C")
g1.add_edge("A","B")
g1.add_edge("A","C")
visited=set()
# dfs("A",g1.graph)
bfs("A",g1.graph)
