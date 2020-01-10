import itertools as it
dist = [
    [0,20,42,25,45,54],
    [20,0,30,34,32,43],
    [42,30,0,10,23,43],
    [25,34,10,0,23,45],
    [20,20,42,25,0,12],
    [60,20,42,25,43,0]

]

def pretrazivanje(mat):
    putanja = []
    ans = 10000
    n = len(mat)
    lista = it.permutations(range(1,n))
    for per in lista:
        suma = mat[0][per[0]]
        for i in range(0,len(per)-1):
            suma = suma + mat[per[i]][per[i+1]]
        suma = suma + mat[per[len(per)-1]][0]
        if suma < ans:
            ans = suma
            putanja = per
    
    putanja = [0] + list(putanja) + [0]

    return ans, putanja

if __name__ == '__main__':
    print( pretrazivanje(dist))