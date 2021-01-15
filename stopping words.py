import math

def removeStopWordPercent(N,k):
    sumlower=0
    sumupper=0
    for n in range(1,k+1):
        sumlower+= 1/(n*math.log10(N)+n)
        sumupper+=1/(n*math.log10(N))
    return (sumlower,sumupper)

N = 10e4
k=10

sumlower,sumupper = removeStopWordPercent(N,k)
print(str((sumlower/N)*100)+"% ≤ freq ≤ "+str((sumupper/N)*100)+"%")