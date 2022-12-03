def p1(): 
    m = {'A' : 0, 'B': 1, 'C': 2, 'X' : 0, 'Y': 1, 'Z': 2}
    a1 = 0
    for line in open("input.in"):
        line = line.strip()
        opp, me = line.split()
        sc = m[me] + 1
        if m[opp] == m[me]:
            sc += 3
        elif (m[me]-1+3)%3 == m[opp]:
            sc += 6
        a1 += sc
    print(a1)



def p2():
    a2 = 0
    m = m = {'A' : 0, 'B': 1, 'C': 2, 'X' : 0, 'Y': 3, 'Z': 6}
    for line in open("input.in"):
        line = line.strip()
        opp, me = line.split()
        sc = m[me]
        if me == 'X':
            sc += 1 + (m[opp]-1+3)%3
        elif me == 'Y':
            sc += 1 + (m[opp]-3+3)%3
        elif me == 'Z':
            sc += 1 + (m[opp]+1)%3

        a2 += sc
    print(a2)
        

p1()
p2()