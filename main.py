import time
import totalno_pretrazivanje as total
import tsp
import myheldkarp
import csv
import tabu_search
import matplotlib.pyplot as plt

dist = [
    [0,20,42,25,45,54],
    [20,0,30,34,32,43],
    [42,30,0,10,23,43],
    [25,34,10,0,23,45],
    [20,20,42,25,0,12],
    [60,20,42,25,43,0]

]


a=tabu_search.tabu_search(tabu_search.Cijene, range(1,len(dist)+1), 300, 0.0001, 0.5,10,dist)
print("Rjesenje problema za G1: ",a[0], " cijena: ", a[1] )

#a = datetime.datetime.now()
#total.pretrazivanje(dist)
#b = datetime.datetime.now()
#print (b-a)
#
#a = time.clock()
#total.pretrazivanje(dist)
#b = time.clock()
#print (b-a)
#with open('vrijeme.csv', mode='w')
# as vrijeme:
#    vrijeme = csv.writer(vrijeme, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    vrijeme.writerow(['Alg', 'Vrijeme', 'Broj gradova'])
rekurz = []
tot_pret = []
heldkarp = []
tabu = []
ap=[]
uspjesno = 0
for i in range(2,12):
    ap.append(i)
    dist = myheldkarp.generate_distances(i)
    n = len(dist)

    
    dp = [[-1] * n for i in range(1<<n)]
    #ans = tsp.tsp(dist,dp,1,0)

    start = time.time()
    print("Rekurz: ",tsp.tsp(dist,dp,1,0))
    print(tsp.put(tsp.C1,n))
    end = time.time()
    rekurz.append((end-start)*1000)

    start = time.time()
    print(total.pretrazivanje(dist))
    end = time.time()
    tot_pret.append((end-start)*1000)

    
    start1 = time.time()
    print("HK: ",myheldkarp.my_tsp(dist))
    end1 = time.time()
    heldkarp.append((end1-start1)*1000)

    #a=tabu_search.tabu_search(tabu_search.Cijene, range(1,len(dist)+1), 1000, 0.0001, 0.5,10,dist)
    start = time.time()
    print("Tabu: ", tabu_search.tabu_search(tabu_search.Cijene, range(1,len(dist)+1), 1000, 0.0001, 0.5,10,dist))
    end = time.time()
    tabu.append((end-start)*1000)

    # if a[1] == ans:
    #     uspjesno +=1
    #     print('ima')



    #with open('vrijeme.csv', mode='w') as vrijeme:
    #    vrijeme.writerow(['Rekurz', end-start, n])

    
print (rekurz)
print (tot_pret)
print (heldkarp)
print (tabu)

print(uspjesno/(4.)*100)

fig, ax = plt.subplots()
ax.plot(ap, rekurz ,'r',label="Rekurzija")
ax.plot(ap, tot_pret,'b', label="Totalno pretrazivanje")
ax.plot(ap, heldkarp, 'g',label="Held Karp")
ax.plot(ap, tabu, 'm',label="Tabu pretrazivanje")

ax.plot(ap,rekurz,'r*')
ax.plot(ap, tot_pret,'b*')
ax.plot(ap, heldkarp, 'g*')
ax.plot(ap, tabu, 'm*')
plt.xlabel('Broj gradova n')
plt.ylabel('Vrijeme izvrsavanja  u ms')
ax.legend()
plt.title('Algoritmi TSP-a')

plt.grid(True)
plt.show()
