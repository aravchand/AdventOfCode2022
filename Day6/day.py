def p(sig_len): 
    a = 0

    inp = open("input.in")
    inp = inp.read()
    for i in range(sig_len, len(inp)):
        rng = inp[i-sig_len:i]
        if len(set(rng)) == sig_len:
            a = i
            break
        
        
    print(a)

p(4)
p(14)