heads = 35
legs = 94

def solve(heads, legs):
    rabbits = (legs/2) - heads
    chickens = heads - rabbits
    print(rabbits, " ", chickens)


solve(heads, legs)