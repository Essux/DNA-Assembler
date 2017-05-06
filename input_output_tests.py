from deBruijn import deBruijn_Graph
import random

original = input('/')
length = len(original)
k = int(input('Type k (for the kmers):'))
graph = deBruijn_Graph(k)

i = 0
built = ""
while (len(graph.kmers) < len(original) - (k-1)):
    i += 1
    rand1= random.randint(0, length-k)
    try:
        rand2 = random.randint(rand1+k, rand1 + max(10, k) if rand1 + max(10, k+1) < length else length)
        read = original[rand1:rand2]
        graph.add_string_to_graph(read)
        graph.getString()
        built = graph.strings[0]
        if i % 15 == 0:
            print('Read', i, end='  ')
            print('Built:', len(built))
            graph.graphvizExport("Read"+str(i), True)
    except ValueError:
        i-=1
graph.getString()

print("Required reads", i)
print('Kmers', len(graph.kmers))
built = graph.strings[0]
print('Length', len(original))
print(original)
print(built)
print('Equal:', original == built)