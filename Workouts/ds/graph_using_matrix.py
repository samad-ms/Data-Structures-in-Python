def add_node(v):
    if v in nodes:
        print("already exist")
    else:
        global node_count
        node_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1," not present,cant add")
    elif v2 not in nodes:
        print(v2, " not present,cant add")
    else:
        index1=nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

def delete_node(v):
    if v not in nodes:
        print("not present")
    else:
        global node_count
        index1=nodes.index(v)
        node_count-=1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present")
    elif v2 not in nodes:
        print(v2,"not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1] = 0

node_count=0
nodes=[]
graph=[]
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B")

print_graph()
delete_node("C")
print_graph()
print()
delete_edge("A","B")
print_graph()