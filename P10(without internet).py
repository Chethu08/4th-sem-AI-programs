info={
"ai":"AI is simulation of human intelligence by machine",
"stack":"Stack follows LIFO operation",
"sort":"Sorting arranges data"
}

q=input("Search: ").lower()
print(info[q] if q in info else "Not Found")