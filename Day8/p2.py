forest = []
for line in open("input.in", "r"):
    forest.append(line.strip())
n = len(forest)
mx = -1
for i in range(n):
    for j in range(n):
        
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        prd = 1
        for d in range(4):
            ci, cj = i + dx[d], j + dy[d]
            see = 0
            while ci >= 0 and ci < n and cj < n and cj >=0:
                see+=1
                if forest[ci][cj]>=forest[i][j]:
                    break
                ci += dx[d]
                cj += dy[d]

            prd *= see
        #     print(prd, end=" ")
        # print()
        mx = max(mx, prd)
    
print(mx)