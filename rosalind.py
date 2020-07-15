def countDnaNucleotides(Dna):
    countDict={'A':0,'C':0,'G':0,'T':0}
    for nucleotide in Dna:
        countDict[nucleotide]+=1
    return countDict

def transcribeDna(Dna):
    Rna=""
    for nucleotide in Dna:
        if nucleotide == "T":
            print(nucleotide)
            Rna=Rna+"U"
        else:
            Rna=Rna+nucleotide
    return Rna

def wascallyWabbits(n,k):
    rabits_population=[1,1]
    for index in range(2,n):
        next_gen=rabits_population[index-1]+rabits_population[index-2]*k
        rabits_population.append(next_gen)
    return rabits_population
