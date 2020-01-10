dist = [
    [0,20,42,25],
    [20,0,30,34],
    [42,30,0,10],
    [25,34,10,0]
]
dist = [
    [0,20,42,25,45,54],
    [20,0,30,34,32,43],
    [42,30,0,10,23,43],
    [25,34,10,0,23,45],
    [20,20,42,25,0,12],
    [60,20,42,25,43,0]

]
C1={}
zadnji = ()
global l
l=0


def put(C1,n):
    bits = 1    
    global zadnji
    ruta = list()
    ruta.append(0)
    #pronalazak putanje
    opt_vrijed,roditelj = C1[(0,bits)]
    while 1:
        ruta.append(roditelj)
        if len(ruta) == n:
            break
        bits = bits | (1 << (roditelj))
        _,roditelj = C1[((roditelj), bits)]

    ruta.append(0)
    return ruta,opt_vrijed

def tsp(dist, dp, maska, pozicija):
    global l
    global C1
    global zadnji
    l=l+1
    n = len(dist)
    svi_gradovi = (1<<n) - 1
    if (maska == svi_gradovi):
        return dist[pozicija][0]
    if (dp[maska][pozicija] != -1):
        return dp[maska][pozicija]

    ans = 1000
    pom=()
    for grad in range(n):
        #print(maska & (1<<grad))
        if (maska & (1<<grad)) == 0:#ako nije posjecen grad
            vrijed = dist[pozicija][grad] + tsp(dist, dp, maska|(1<<grad),grad)
            if vrijed < ans:
                pom=(vrijed, grad)
            ans = min(ans, vrijed)
    dp[maska][pozicija] = ans
    #print(maska)
    #print(pom)
    C1[(pozicija,maska)] = pom
    if maska == 1:
        zadnji = pom
    return ans

if __name__ == '__main__':
    n = len(dist)
    dp = [[-1] * n for i in range(1<<n)]
    print("Travelling Saleman Distance is", tsp(dist,dp,1,0))
    #print(l)
    print(put(C1,n))
    #print(put(C1,n))
    #print(C1)
