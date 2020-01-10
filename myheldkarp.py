import itertools
import sys
import random

dists = [
    [0,10,15,20],
    [5,0,9,10],
    [6,13,0,12],
    [8,8,9,0]
]
dists = [
    [0,20,42,25],
    [20,0,30,34],
    [42,30,0,10],
    [25,34,10,0]
]
dists = [
    [0,20,42,25,45,54],
    [20,0,30,34,32,43],
    [42,30,0,10,23,43],
    [25,34,10,0,23,45],
    [20,20,42,25,0,12],
    [60,20,42,25,43,0]
]
BiH=[
    [0,60,140,135,340,170,280,195],
    [63, 0, 185, 120, 260, 85, 195, 200],
    [145, 190, 0, 245, 430, 275, 250, 315],
    [140, 124, 240, 0, 330, 70, 180, 75],
    [355,265,420,333,0,260,168,390],
    [180,88,270,72,255,0,105,120],
    [295,200,245,185,170,107,0,230],
    [205,205,318,77,395,122,235,0]
]
l=0
def my_tsp(dists):
    global l
    n=len(dists[0])
    C={}
    for k in range(1,n):
        C[(k,0)] = (dists[k][0],0)#0 za koje je postignut min

    for vel_skupa in range(1,n-1):
        for grad in range(1,n):
            ostali_gr = range(1,grad)+range(grad+1,n)
            for skup in itertools.combinations(ostali_gr, vel_skupa):
                bits = 0#potrebno je odrediti koji su gradovi u skupu
                for bit in skup:
                    bits = bits | (1<<bit)
                res=[]
                for gr in skup:
                    prev = bits & ~(1 << gr)
                    res.append((( dists[grad][gr] + C[(gr,prev)][0]),gr))
                    l=l+1
                C[(grad,bits)] = min(res)

    res = []
    for grad in range(1,n):
        skup = range(1,grad) + range(grad + 1, n)
        bits = 0
        for bit in skup:
            bits = bits | (1 << bit)

        res.append(((dists[0][grad]+C[(grad,bits)][0]),grad))
        l=l+1

    bits = (1<<n)-1    
    C[(n,bits)]=min(res)
    putanja=[0]
    #pronalazak putanje
    opt_vrijed,roditelj = min(res)
    k = True
    bits = bits - 1
    while k:
        putanja.append(roditelj)
        bits = bits & ~(1 << roditelj)
        _,roditelj = C[(roditelj, bits)]
        if bits == 0: 
            k = False

    putanja.append(0)
    return ([opt_vrijed, putanja])

def generate_distances(n):
    dists = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = random.randint(1, 99)

    return dists
def read_distances(filename):
    dists = []
    with open(filename, 'rb') as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            dists.append(map(int, map(str.strip, line.split(','))))

    return dists


if __name__ == '__main__':
    arg = sys.argv[0]

    if arg.endswith('.csv'):
        dists = read_distances(arg)
    #else:
        #dists = generate_distances(int(arg))

    # Pretty-print the distance matrix
    print("Cijene putovanja")
    for row in BiH:

        print(''.join([str(n).rjust(5, ' ') for n in row]))
        

    print('')
    [opt,putanja] = my_tsp(dists)
    print("Optimalna vrijednost:",opt)
    print("Putanja:", putanja)
    print(l)
