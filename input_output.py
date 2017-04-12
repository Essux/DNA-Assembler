from deBruijn import deBruijn_Graph
import sys
sys.setrecursionlimit(10000)

with open("AB042837ADN.txt", mode='r') as file:
    final = file.readline()

k = int(input('Type k (for the kmers):'))
graph = deBruijn_Graph(k)
i = 0

with open("AB042837ADN-segments.txt", mode='r') as file:
    length = int(file.readline())
    file.readline()

    while (len(graph.string) < length):
        i += 1
        nextst = file.readline()[:-1]
        file.readline()
        if i % 250 == 0:
            print('Read', i)
            print('Read length:', len(nextst))
            print('Assembled length', len(graph.string))
        graph.add_string_to_graph(nextst)
        graph.getString()

#print('Nodes:', nodes)
#print('Edges:', graph.edges)
#print('Kmers', kmers)
built = graph.getString()
#print('Trail:', graph.trail)
#print(final)
#print(built)
print('Equal:', final == built)
#graph.graphvizExport()