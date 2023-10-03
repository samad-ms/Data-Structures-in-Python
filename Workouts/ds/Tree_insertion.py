def add_node(v):
    global node_count
    if v in nodes:
        print("elemment already exist")
    else:
        node_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    for n in graph:
        for v in n:
            print(v,end=" ")
        print()


node_count=0
nodes=[]
graph=[]

print("before adding a nodes")
print(graph)
print(nodes)
add_node(1)
add_node(2)
print("after adding a nodes")
print_graph()
