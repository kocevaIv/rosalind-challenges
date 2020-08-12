"""A population conssisting of: k-individuals that are homozygous dominant,
                                n-individuals are homozyguos recessive,
                                m-individuals are heterozygous
"""
#Possible events that if two randomly selected mating organisms will produce an individual possessing a recessive allele :
#1.homozygous recessive+heterozyguos - prob = 0.5
#2.homozygous recessive+homozyguos recessive - prob = 1
#3.heterozyguos + heterozyguos - prob = 0.25
#4.heterozyguos + homozygous recessive - prob = 0.5
def calculateProb(k,m,n):
    population=k+m+n
    e1=((n*m)/(population*(population-1)))*0.5
    e2=(n*(n-1))/(population*(population-1))
    e3=((m*(m-1))/(population*(population-1)))*0.25
    e4=((m*n)/(population*(population-1)))*0.5
    prob = e1 + e2 + e3 + e4
    return prob

def mendelsFirstLaw(k,m,n):
    probRecessvie = calculateProb(k,m,n)
    probDominant = 1 - probRecessvie
    return probDominant
