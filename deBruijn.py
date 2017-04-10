edges = {}
nodes = set()
kmers = set()

def de_bruijn_ize(st, k):
    if st[:k] not in kmers and st[:k-1] not in edges:
        if 'INITIAL' not in edges:
            edges['INITIAL'] = []
        edges['INITIAL'].append(st[:k-1])

    for i in range(len(st) - k +1):
        kmer = st[i:i+k]
        if kmer not in kmers:
            kmers.add(kmer)
            kmer1 = st[i:i+k-1]
            kmer2 = st[i+1:i+k]
            if kmer1 not in edges.keys():
                edges[kmer1] = []
            edges[kmer1].append(kmer2)
            
            #If an edge goes towards it, it's not really an initial
            if kmer2 in edges['INITIAL']:
                index = edges['INITIAL'].index(kmer2)
                del edges['INITIAL'][index]

            nodes.add(st[i:i+k-1])
            nodes.add(st[i+1:i+k])
    for node in nodes:
        if node not in edges:
            edges[node] = []
    return nodes, edges

visited = set()
trail = []

def dfs(curNode, initial):
    visited.add(curNode)
    while curNode in edges and edges[curNode]:
        nextNode = edges[curNode].pop()
        dfs(nextNode, False)
    if not initial:
        trail.append(curNode)

def topoSort(nodes):
    for initialnode in edges['INITIAL']:
        if edges[initialnode] and initialnode not in visited:
            dfs(initialnode, False)
    trail.reverse()

def listToString(fragments):
    st = fragments.pop(0)
    while fragments:
        st += fragments.pop(0)[-1]
    return st

def graphvizExport():
        text = ""
        text += "digraph deBruijn {\n"
        text += "node [shape = circle];\n"
        for f in edges2.keys():
            for t in edges2[f]:
                text += str(f) + " -> " + str(t) + '\n'
        text += "}"

        with open("deBruijn.dot", encoding='utf-8', mode='w') as file:
            file.write(text)

final = input('/')
k = int(input('Type k (for the kmers):'))
reads = int(input('Type the number of reads to be simulated:'))
import random
for i in range(0, reads):
    try:
        rand1= random.randint(0, len(final) - k)
        rand2 = random.randint(rand1+k, len(final))
        de_bruijn_ize(final[rand1:rand2], k)
        print('Read', i+1, final[rand1:rand2])
    except:
        print('Failed Read')
import copy
edges2 = copy.deepcopy(edges)
#print('Nodes:', nodes)
print('Edges:', edges)
#print('Kmers', kmers)
topoSort(nodes)
print('Trail:', trail)
print(final)
built = listToString(trail)
print(built)
print('Equal:', final == built)
graphvizExport()