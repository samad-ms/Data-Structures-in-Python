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

    def check_edge(self,v1,v2):
        if  v1 not in self.graph:
            print(v1,"not present")
        elif v2 not in self.graph:
            print(v2,"not present")
        else:
            if v1 in self.graph[v2]:
                return True
            else:
                return False


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

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.graph.get(v, []):
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        return False


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
            visited.add(cur)
            for neigh in graph[cur]:
                stack.append(neigh)


# def dfs(node,visited,graph):
#     if node not in visited:
#         print(node,end=" ")
#         visited.add(node)
#         for neigh in graph[node]:
#             if neigh not in visited:
#                 dfs(neigh,visited,graph)

g1=Graph()
g1.add_node("A")
g1.add_node("B")
g1.add_node("C")
g1.add_edge("A","B")
g1.add_edge("B","C")
g1.add_edge("A","C")
visited=set()
dfs("A",g1.graph)
print(g1.check_edge("A","B"))

# print(g1.is_cyclic())