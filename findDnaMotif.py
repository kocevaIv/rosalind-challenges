def findMotif(s,t):
    motifLen = len(t)
    pos=[]
    for index in range(0,len(s)-motifLen):
        motif=s[index:index+motifLen]
        if motif == t:
            pos.append(index+1)
    return pos
