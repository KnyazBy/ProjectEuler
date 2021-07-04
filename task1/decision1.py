print(sum([x for x in range(1, 1000) if (x%3)*(x%5) == 0])) 

#sum(i for i in range(1000) if not (i % 3 and i % 5))