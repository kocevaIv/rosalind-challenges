class Graph():

    def __init__(self, graphDict=None):
        if graphDict is None:
            self.graphDict = {}
        else:
            self.graphDict = graphDict

    # get all the vertices from the graph
    def getVertices(self):
        return list(self.graphDict.keys())

    # get all the edges (v,w) in the graph
    def getEdges(self):
        edges = []
        for key in self.graphDict.keys():
            for value in self.graphDict[key]:
                if [key, value] not in edges:
                    edges.append([key, value])
        return edges

    # add a vertex v to the graph
    def addVertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

    # add a new edge
    def addEdge(self, edge):
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 not in self.graphDict:
            self.graphDict[vrtx1] = [vrtx2]
        else:
            self.graphDict[vrtx1].append(vrtx2)

    def __str__(self):
        str = ""
        for edge in self.getEdges():
            str += "{} {}\n".format(edge[0], edge[1])
        return str


# read the DNA sequences in FASTA format and return a dictionary in format {name sequence:dna sequence}
def readDNA(pathToFile):
    dnaDict = {}
    with open(pathToFile) as fp:
        content = fp.read().split(">")[1:]
        for line in content:
            entry = line.splitlines()
            seqName = entry[0]
            dna = "".join(entry[1:])
            dnaDict[seqName] = dna
    return dnaDict


# helper function
def isOverlap(dna_seq1, dna_seq2, k):
    return dna_seq2.startswith(dna_seq1[-k:])


def overlapGraphs(fileLocation, k):
    dnaDict = readDNA(fileLocation)
    graph_dictionary = {key: [] for key in dnaDict.keys()}
    graph = Graph(graph_dictionary)
    vertices = graph.getVertices()
    for i in range(len(vertices) - 1):
        v1 = vertices[i]
        for j in range(i + 1, len(vertices)):
            v2 = vertices[j]
            if isOverlap(dnaDict[v1], dnaDict[v2], k):
                graph.addEdge([v1, v2])
            if isOverlap(dnaDict[v2], dnaDict[v1], k):
                graph.addEdge([v2, v1])
    return graph
