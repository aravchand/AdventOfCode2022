from collections import deque


def p1(): 
    """
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 
    """
    stacks = {
        1: ['T', 'D', 'W', 'Z', 'V', 'P'],
        2: ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
        3: ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
        4: ['R', 'S', 'J'],
        5: ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
        6: ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
        7: ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
        8: ['P', 'T', 'B', 'Q'],
        9: ['H', 'G', 'Z', 'R', 'C']
    }
    for s, stack in stacks.items():
        stacks[s] = deque(stack)

    lines = open("edited_input.in").read().splitlines()
    # print(lines)
    # print("\n\n\n")
    for line in lines:
        line = line.strip().split()
        _, n, _, f, _, t = line
        n = int(n)
        t = int(t)
        f = int(f)
        for _ in range(n):
            # print(" ".join(line))
            stacks[t].append(stacks[f].pop())
    a1 = ""
    for s, stack in stacks.items():
        a1 += stack.pop()
        
    print(a1)

def p2():
    stacks = {
        1: ['T', 'D', 'W', 'Z', 'V', 'P'],
        2: ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
        3: ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
        4: ['R', 'S', 'J'],
        5: ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
        6: ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
        7: ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
        8: ['P', 'T', 'B', 'Q'],
        9: ['H', 'G', 'Z', 'R', 'C']
    }
    for s, stack in stacks.items():
        stacks[s] = deque(stack)

    lines = open("edited_input.in").read().splitlines()
    # print(lines)
    # print("\n\n\n")
    for line in lines:
        line = line.strip().split()
        _, n, _, f, _, t = line
        n = int(n)
        t = int(t)
        f = int(f)
        l = []
        for _ in range(n):
            l.append(stacks[f].pop())
        for _ in range(n):
            stacks[t].append(l.pop())
    a2 = ""
    for s, stack in stacks.items():
        a2 += stack.pop()
        
    print(a2)

        

# p1()
# p2()

# For my first solution, I just hardcoded the input... not scalable at all!
# Let's try to make it more general:
s = open("input.in", "r").read()
stks, cmds = s.split("\n\n")
stks = stks.splitlines()
