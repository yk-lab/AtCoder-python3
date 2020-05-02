import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
STX = [list(map(int, input().split())) for n in range(N)]
D = [int(input()) for q in range(Q)]

max_X = max(map(lambda x: x[2], STX))
max_T = max(map(lambda x: x[1], STX))

prog = []
finish = [-1] * Q
next_D = 0
for i in range(max_T + 1):
    now = [l[2] for l in filter(lambda r: r[0] <= i < r[1], STX)]
    remove = []
    for p in prog:
        p[1]+=1
        if p[1] in now:
            finish[p[0]] = p[1]
            remove.append(p)
        elif p[1] == max_X:
            finish[p[0]] = -1
            remove.append(p)            
    for p in remove:
        prog.remove(p)
    if next_D != -1 and i == D[next_D]:
        prog.append([next_D, 0])
        next_D = next_D + 1 if next_D < Q-1 else -1
for f in finish:
    print(f)