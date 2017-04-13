from deBruijn import deBruijn_Graph
from time import clock

with open("AY325307ADN.txt", mode='r') as file:
    final = file.readline()

k = int(input('Type k (for the kmers):'))
graph = deBruijn_Graph(k)
i = 0

t0 = clock()
with open("AY325307ADN-segments.txt", mode='r') as file:
    length = int(file.readline())
    file.readline()

    while (len(graph.string) < length):
        i += 1
        nextst = file.readline()[:-1]
        file.readline()
        graph.add_string_to_graph(nextst)        
        if i % 15 == 0:
            print('Read', i)
            print('Read length:', len(nextst))
            graph.getString()
            print('Assembled length', len(graph.string))
            #print(graph.string in final)
t1 = clock()-t0

print('Required reads:', i)
built = graph.getString()
print('Equal:', final == built)
print('Time used:', t1, 'seg')