def de_bruijn_ize(st, k):
    edges = {}
    nodes = set()
    for i in range(len(st) - k +1):
        kmer1 = st[i:i+k-1]
        kmer2 = st[i+1:i+k]
        if kmer1 not in edges.keys():
            edges[kmer1] = []
        edges[kmer1].append(kmer2)

        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    edges['INITIAL'] = [st[:k-1]]
    for node in nodes:
        if node not in edges:
            edges[node] = []
    return nodes, edges

visited = set()
trail = []

def dfs(curNode, edges, initial):
    visited.add(curNode)
    while curNode in edges and edges[curNode]:
        nextNode = edges[curNode].pop()
        dfs(nextNode, edges, False)
    if (not initial):
        trail.append(curNode)

def topoSort(nodes, edges):
    for node in edges.keys():
        if edges[node]:
            dfs(node, edges, True)
    trail.reverse()

def listToString(fragments):
    st = fragments.pop(0)
    while fragments:
        st += fragments.pop(0)[-1]
    return st

#st = 'ACTAGAGTTTTTTTGAT'
st = input('/')
nodes, edges = de_bruijn_ize(st, 7)
print(nodes)
print(edges)
topoSort(nodes, edges)
print(trail)
print(st)
built = listToString(trail)
print(built)
print('Equal:', st == built)