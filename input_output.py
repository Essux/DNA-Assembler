from deBruijn import deBruijn_Graph
from time import clock
from sys import argv

filename = argv[1]

k = 200
graph = deBruijn_Graph(k)
i = 0

t0 = clock()

with open(filename + "ADN-segments.txt", mode='r') as file:
    length = int(file.readline())
    file.readline()

    while (len(graph.kmers) < length - k +1):
        i += 1
        nextst = file.readline()[:-1]
        file.readline()
        graph.add_string_to_graph(nextst) 
        graph.getGenes()

t1 = clock()-t0

print()
print('-'*45)
print('Required reads:', i)
built = graph.strings[0]
original = open(filename + "ADN.txt", mode='r').readline()
print('String correctness:', built == original)
print('Time used:', "{0:.3f}".format(t1), 'seg')
print('String length:', str(sum([len(stt) for stt in graph.strings])) + '/' + str(length))
print("Found", len(graph.genes), 'genes')
print('-'*45)