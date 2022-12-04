def p1(): 
    a1 = 0

    for line in open("input.in"):
        line = line.strip()
        f, s = [list(map(int, x.split("-"))) for x in line.split(",")]
        a, b = f
        c, d = s
        a1 += (a <= c and d <= b) or (c <= a and b <= d)
        
    print(a1)



def p2():
    a2 = 0

    for line in open("input.in"):
        line = line.strip()
        f, s = [list(map(int, x.split("-"))) for x in line.split(",")]
        a, b = f
        c, d = s
        if c < a:
            # swap a,b with c,d
            a, b, c, d = c, d, a, b
        a2 += max(a, c) <= b 
    
    print(a2)
        

p1()
p2()