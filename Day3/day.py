def p1(): 
    a1 = 0

    for line in open("input.in"):
        line = line.strip()
        n = len(line)
        A, B = line[0:n//2], line[n//2:]
        A = set(A)    
        B = set(B)
        shared = A & B
        for s in shared:
            if 'a' <= s <= 'z':
                a1 += ord(s) - ord('a') + 1
            elif 'A' <= s <= 'Z':
                a1 += ord(s) - ord('A') + 27
    print(a1)



def p2():
    a2 = 0

    n = 0
    lines = []
    for line in open("input.in"):
        line = line.strip()
        lines.append(line)
        n += 1
        if n==3:
            n = 0
            A, B, C = lines
            lines = []
            A = set(A)    
            B = set(B)
            C = set(C)
            shared = A & B & C
            for s in shared:
                if 'a' <= s <= 'z':
                    a2 += ord(s) - ord('a') + 1
                elif 'A' <= s <= 'Z':
                    a2 += ord(s) - ord('A') + 27
            
    print(a2)
        

p1()
p2()