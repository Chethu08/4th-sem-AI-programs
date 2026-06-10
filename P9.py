b={i:" " for i in
["top-L","top-M","top-R",
 "mid-L","mid-M","mid-R",
 "low-L","low-M","low-R"]}

def show():
    print(f"{b['top-L']}|{b['top-M']}|{b['top-R']}")
    print("-+-+-")
    print(f"{b['mid-L']}|{b['mid-M']}|{b['mid-R']}")
    print("-+-+-")
    print(f"{b['low-L']}|{b['low-M']}|{b['low-R']}")

t="X"
for _ in range(4):
    show()
    b[input(f"Turn for {t}: ")]=t
    t="O" if t=="X" else "X"
show()