import copy
class deBruijn_Graph:
    'Class used to build de Bruijn graph with the k-mers'
    def __init__(self, k):
        """@Parameter k: It's an interger value that represents the k-mers length
        Method used to initialize the class' attributes"""
        # Size of the k-mers
        self.k = k
        # Dictionary. Key: Parent node. Value: List of succesors 
        self.edges = {}
        # Set of graph nodes
        self.nodes = set()
        # Set of k-mers
        self.kmers = set()
        self.visited = set()
        self.trail = []
        self.string = ""

    def add_string_to_graph(self, st):
        """@Parameter st: It's a string that contains the segment of DNA
        This method builds and adds the string's k-mers to the graph""" 
        if len(st)<self.k:
            return
        # If the initial kmer hasn't been already seen and k-1mer isn't in the graph
        # the k-1mer is the beginning of a string
        if st[:self.k] not in self.kmers and st[:self.k-1] not in self.edges:
            if 'INITIAL' not in self.edges:
                self.edges['INITIAL'] = []
            self.edges['INITIAL'].append(st[:self.k-1])

        # For each kmer
        for i in range(len(st) - self.k +1):
            kmer = st[i:i+self.k]
            
            # If it hasn't been seen, add it's two k-1mers
            if kmer not in self.kmers:
                self.kmers.add(kmer)
                kmer1 = st[i:i+self.k-1]
                kmer2 = st[i+1:i+self.k]

                if kmer1 not in self.edges.keys():
                    self.edges[kmer1] = []
                self.edges[kmer1].append(kmer2)
                
                #If an edge goes towards a k-1mer, it's not really an initial, delete it
                if kmer2 in self.edges['INITIAL']:
                    self.edges['INITIAL'].remove(kmer2)

                self.nodes.add(st[i:i+self.k-1])
                self.nodes.add(st[i+1:i+self.k])

        for node in self.nodes:
            if node not in self.edges:
                self.edges[node] = []

    def _dfs(self, curNode):
        """@Parameter curNode: It is a node of graph where the dfs starts'
        'This method travels the graph in dfs from curNode to its successors to build'
        'the trail of the DNA"""
        stack = []
        stack.append(curNode)
        self.visited.add(curNode)
        while len(stack) > 0:
            curNode = stack.pop()
            for node in self.edges[curNode]:
                if node not in self.visited:
                    self.visited.add(node)
                    stack.append(node)
            self.trail.append(curNode)

    def getString(self):
        """This method calls dfs and _listToString to build the string with the k-mers"""
        edges2 = copy.deepcopy(self.edges)
        initialnode = self.edges['INITIAL'][0]
        if self.edges[initialnode]:
            self.visited = set()
            self._dfs(initialnode)
        self.edges = copy.deepcopy(edges2)
        return self._listToString()

    def _listToString(self):
        """This method concatenates the trail of the graph into a string representing the DNA
        sequence"""
        if (not self.trail):
            return ""
        st = self.trail.pop(0)
        while self.trail:
            st += self.trail.pop(0)[-1]
        self.string = st
        return st

    def graphvizExport(self):
        'This method shows the shape of deBruijn graph'
        text = ""
        text += "digraph deBruijn {\n"
        text += "node [shape = circle];\n"
        for f in self.edges.keys():
            for t in self.edges[f]:
                text += str(f) + " -> " + str(t) + '\n'
        text += "}"

        with open("deBruijn.dot", encoding='utf-8', mode='w') as file:
            file.write(text)