# read the DNA sequences in FASTA format
def readDNA(pathToFile):
    dnaList = []
    with open(pathToFile) as fp:
        content = fp.read().split(">")[1:]
        for line in content:
            entry = line.splitlines()[1:]
            dna = "".join(entry)
            dnaList.append(dna)
    return dnaList


# helper method to initialise a matrix with all zeros
def constructEmptyProfileMatrix(columnSize):
    profileMatrix = {}
    nucleotides = ["A", "C", "G", "T"]
    for nucleotide in nucleotides:
        profileMatrix[nucleotide] = columnSize * [0]
    return profileMatrix


# build profile matrix
def buildProfileMatrix(dnaList):
    m = len(dnaList)
    columnSize = len(dnaList[0])
    nucleotides = ["A", "C", "G", "T"]
    profileMatrix = constructEmptyProfileMatrix(columnSize)
    for i in range(0, m):
        for column in range(0, columnSize):
            profileMatrix[dnaList[i][column]][column] += 1
    return profileMatrix


# find the consensus string from the profile matrix
def findConsensus(profileMatrix):
    nucleotides = ["A", "C", "G", "T"]
    consensusString = ""
    columnSize = len(profileMatrix[nucleotides[0]])
    for column in range(0, columnSize):
        maxCount = 0
        symbol = ""
        for nucleotide in nucleotides:
            if profileMatrix[nucleotide][column] > maxCount:
                maxCount = profileMatrix[nucleotide][column]
                symbol = nucleotide
        consensusString += symbol
    return consensusString