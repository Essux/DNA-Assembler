from deBruijn import deBruijn_Graph
import random

final = input('/')
k = int(input('Type k (for the kmers):'))
graph = deBruijn_Graph(k)

i = 0
while (len(graph.string) < len(final)):
    i += 1
    rand1= random.randint(0, len(final)-k)
    try:
        rand2 = random.randint(rand1+k, rand1 + 30 if rand1 + 30 < len(final) else len(final))
        read = final[rand1:rand2]
        graph.add_string_to_graph(read)
        st = graph.getString()
        print('Size:', len(read))
        if i % 10 == 0:
            print('Read', i, read)
            print('Edges', graph.edges)
            print (st)
    except ValueError:
        print('Failed Read')
        i-=1


print("Required reads", i)
built = graph.getString()
print(final)
print(built)
print('Equal:', final == built)
graph.graphvizExport()