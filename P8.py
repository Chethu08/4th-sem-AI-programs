def neg(x):
    return x[1:] if x[0]=="~" else "~"+x

kb=[{"P","Q","R"},{"~P","R"},{"~Q","R"},{"~R","~P","Q"}]
new=[]

for c1 in kb:
    for c2 in kb:
        for x in c1:
            if neg(x) in c2:
                new.append((c1|c2)-{x,neg(x)})

print("Unsatisfiable" if set() in new else "Satisfiable")