def countDnaNucleotides(Dna):
    countDict={'A':0,'C':0,'G':0,'T':0}
    for nucleotide in Dna:
        countDict[nucleotide]+=1
    return countDict