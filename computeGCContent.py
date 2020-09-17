def computeHighestGCContent(pathToFile):
    dnaIdDict = {}
    highestGCContent = 0
    id = ""
    with open(pathToFile) as fp:
        content = fp.read().split(">")[1:]
        for line in content:
            seqContent = line.splitlines()
            identifier = seqContent[0]
            dna = ""
            for index in range(1, len(seqContent)):
                dna += seqContent[index]
            dnaIdDict[identifier] = dna
            gc_content = computeGCcontent(dna)
            if gc_content >= highestGCContent:
                highestGCContent = gc_content
                id = identifier
    return id, highestGCContent


def computeGCcontent(dna):
    n = len(dna)
    countGC = 0
    for symbol in dna:
        if symbol == "G" or symbol == "C":
            countGC += 1
    gcPrecentage = (countGC / n) * 100;
    return gcPrecentage


print(computeHighestGCContent("rosalind_gc.txt"))
