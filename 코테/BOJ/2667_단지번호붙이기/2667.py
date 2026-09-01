N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
rd = [-1, 1, 0, 0]
cd = [0, 0, -1, 1]
home_local = []

def search(x, y):

    arr[x][y] = 2
    home_local[-1] += 1

    for direc in range(4):
        rn = x + rd[direc]
        cn = y + cd[direc]
        if rn < 0 or rn >= N or cn < 0 or cn >= N or arr[rn][cn] != 1:
            continue
        search(rn, cn)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_local.append(0)
            search(i, j)

home_local.sort()

print(len(home_local))
for x in home_local:
    print(x)


