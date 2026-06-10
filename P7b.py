rules=[({"has-fur(tiger)"},"mammal(tiger)"),
       ({"has-feathers(penguin)","lays-eggs(penguin)"},"bird(penguin)"),
       ({"has-fur(cat)"},"mammal(cat)")]

facts={"has-fur(tiger)","has-feathers(penguin)",
       "lays-eggs(penguin)","lays-eggs(sparrow)",
       "has-fur(cat)"}

def check(goal):
    if goal in facts: return True
    for a,c in rules:
        if c==goal and all(check(x) for x in a):
            return True
    return False

for g in ["mammal(tiger)","bird(penguin)","bird(sparrow)","mammal(cat)"]:
    print(f"Goal {g} {'can' if check(g) else 'cannot'} be derived from facts.")