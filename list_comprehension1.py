#multiple for to build comprehensive 
a = [(x,y) for x in range(5) for y in range(5) if (x+y) % 2 == 0]

print(a)

b = [(x,y) for x in range(5) for y in range(5) if(x+y) % 2 == 0  and x!=y]

print(b)