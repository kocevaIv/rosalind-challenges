def transcribeDna(Dna):
    Rna = ""
    for nucleotide in Dna:
        if nucleotide == "T":
            print(nucleotide)
            Rna = Rna + "U"
        else:
            Rna = Rna + nucleotide
    return Rna
