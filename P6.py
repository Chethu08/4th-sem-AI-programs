d=[[0,4,8,9,12],[4,0,6,8,9],[8,6,0,10,11],[9,8,10,0,7],[12,9,11,7,0]]
tour=[0]
v={0}
dist=0
c=0

while len(v)<5:
    n=min((d[c][i],i) for i in range(5) if i not in v)
    dist+=n[0]
    c=n[1]
    v.add(c)
    tour.append(c)

tour.append(0)
dist+=d[c][0]
print("Nearest Neighbour TSP Tour:",tour)
print("Total Distance:",dist)