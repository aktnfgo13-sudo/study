N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
safe = []
pick_safe = []
poizen = []
rd = [-1, 1, 0, 0]
cd = [0, 0, -1, 1]
arr_check = []

result = 0


for i in range(N): # 0 인덱스 튜플로 리스트화
    for j in range(M):
        if arr[i][j] == 0:
            safe.append((i, j))
        elif arr[i][j] == 2:
            poizen.append((i, j))

def count_safe(x,y): # 바이러스 퍼지는 함수
    global arr_check
    if arr_check[x][y] == 2:
        for direc in range(4):
            xd = x + rd[direc]
            yd = y + cd[direc]
            if 0 > xd or N <= xd or 0 > yd or M <= yd:
                continue
            if arr_check[xd][yd] == 0:
                arr_check[xd][yd] = 2
                count_safe(xd,yd)

    
def comb(depth, idx): # 3가지 벽을 세우는 조합
    global arr_check
    global result
    if depth == 3:
        count = 0
        arr_check = [row[:] for row in arr] # arr 복사
        for row, col in pick_safe: # 벽 추가
            arr_check[row][col] = 1
        for poizen_row, poizen_col in poizen: # 독 퍼집
            count_safe(poizen_row, poizen_col)    
        for i in range(N):
            for j in range(M):
                if arr_check[i][j] == 0:
                    count += 1
        result = max(count, result)
        return 
    for i in range(idx, len(safe)):
        pick_safe.append(safe[i])
        comb(depth + 1, i + 1)
        pick_safe.pop()


comb(0,0)

print(result)


# # 연구소 
# 1 = 벽
# 2 = 바이서스

# 벽을 3개 세워 바이러스가 안전영역이 가장 커지는(최소로 퍼지는) 안전영역 최댓값

# 1. 0 인 위치의 인덱스를 저장(리스트 + 튜플)
# 2. 그중 3개를 선택하는 경우 즉 조합 
# 3. 영역 확인 


