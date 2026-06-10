rules=[({"has-fur(tiger)"},"mammal(tiger)"),
       ({"has-feathers(penguin)","lays-eggs(penguin)"},"bird(penguin)"),
       ({"has-fur(cat)"},"mammal(cat)")]

facts={"has-fur(tiger)","has-feathers(penguin)",
       "lays-eggs(penguin)","lays-eggs(sparrow)",
       "has-fur(cat)"}

while True:
    new={c for a,c in rules if a<=facts}
    if new<=facts: break
    facts|=new

print("Derived Facts:",facts)