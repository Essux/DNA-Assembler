from deBruijn import deBruijn_Graph
final = input('/')
k = int(input('Type k (for the kmers):'))
#reads = int(input('Type the number of reads to be simulated:'))
graph = deBruijn_Graph(k)
import random
i = 0
while (len(graph.string) < len(final)):
    i += 1
    rand1= random.randint(0, len(final) - k)
    rand2 = random.randint(rand1+k, len(final))
    print('Read', i+1, final[rand1:rand2])
    graph.add_string_to_graph(final[rand1:rand2])
    print (graph.getString())

#print('Nodes:', nodes)
print('Edges:', graph.edges)
#print('Kmers', kmers)
built = graph.getString()
print('Trail:', graph.trail)
print(final)
print(built)
print('Equal:', final == built)
graph.graphvizExport()