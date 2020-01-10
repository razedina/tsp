G1 = [[0,3,3,8,6],[3,0,7,2,8],[3,7,0,5,2],[8,2,5,0,1],[6,8,2,1,0]]
G2 = [[0,2,2,2,7,5,2],[2,0,4,7,9,1,3],[2,4,0,3,6,6,5],[2,7,3,0,4,9,6],[7,9,6,4,0,4,9],[5,1,6,9,4,0,2],[2,3,5,6,9,2,0]]
kombinacije=[]

def Cijene(a, G1):
    cijena = 0
    vel = len(a)

    for i in range(0,len(a)-1):
        cijena = cijena + G1[a[i]-1][a[i+1]-1]
    cijena = cijena + G1[a[vel-1]-1][a[0]-1]
    return cijena

def generisiOkolinu(x, T):

    okolina = []
    for i in range(0,len(x)):
        for j in range(i+1, len(x)):
            pom = []
            for k in x:
                pom.append(k)

            pom[i], pom[j]=pom[j], pom[i]

            if pom != x and pom not in T and pom not in okolina:
                okolina.append(pom)

    return okolina

def tabu_search(f, x0, max_iter, eps, delta_x,n,G1):
    x = x0
    i = 0
    tabu = [x]
    minimumi = [[x,f(x,G1)]]
    while i < max_iter:
        kombinacije=generisiOkolinu(x, tabu)
        #for t in tabu:
         #   if t in kombinacije:
          #      kombinacije.remove(t)

        min_okolina = []
        for a in kombinacije:
            i = i + 1
            min_okolina.append([a,f(a,G1)])
            
        min_okolina.sort(key=lambda tup: tup[1])  
        x = min_okolina[0][0]

        tabu.append(x)
        if(len(tabu) > n):
            tabu.remove(tabu[0])

        minimumi.append([x,f(x,G1)])
        minimumi.sort(key=lambda tup: tup[1])
        if abs(minimumi[0][1]-minimumi[1][1]) < eps:
            return minimumi[0]
        #print(tabu, 'tabu')
        #print(kombinacije,'kombi', len(kombinacije))
        #kombinacije.clear()
        kombinacije = []

     
    return minimumi[0]
         
#print(tabu_search(f, [6, 19], 300, 0.0001, 0.5,10)) 
#print(tabu_search(f1, [-5, 5], 300, 0.00001, 0.2,10))
#Gen_ndim_okol([1, 2, 3], 0.5)
#print(kombinacije)
# 
if __name__ == '__main__':
    a=tabu_search(Cijene, [1,2,3,4,5], 300, 0.0001, 0.5,10,G1)
    print("Rjesenje problema za G1: ",a[0], " cijena: ", a[1] )
