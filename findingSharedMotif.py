def readDNA(pathToFile):
    dnaList = []
    with open(pathToFile) as fp:
        content = fp.read().split(">")[1:]
        for line in content:
            entry = line.splitlines()[1:]
            dna = "".join(entry)
            dnaList.append(dna)
    return dnaList


def findAllSubStrings(dna):
    dnaSeqLen = len(dna)
    substrings = set()
    for nucleotide in range(0, dnaSeqLen):
        substring = dna[nucleotide]
        substrings.add(substring)
        for index in range(nucleotide + 1, dnaSeqLen):
            substring += dna[index]
            substrings.add(substring)
    return substrings


def checkPattern(dnaList, pattern):
    for dna in dnaList:
        if not dna.__contains__(pattern):
            return False
    return True


def findSharedMotif(dnaSeqList):
    sharedMotif = ""
    motifs = findAllSubStrings(dnaSeqList[0])
    for motif in motifs:
        if checkPattern(dnaSeqList, motif):
            if len(sharedMotif) < len(motif):
                sharedMotif = motif
    return sharedMotif
