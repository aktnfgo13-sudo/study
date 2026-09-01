N, M = map(int,input().split()) # N = 행렬 사이즈, M = 폐업시키지 않을 치킨집 최대 

# 1 <= 집의 개수는 <= 2N, M <= 치킨집의 개수 <= 13 
arr = [list(map(int,input().split())) for _ in range(N)]

home_rc = []
restorant_rc = []
pick_number = []
result = float('inf')

for i in range(N): # 치킨집 & 집 인덱스 리스트 생성
    for j in range(N):
        if 1 == arr[i][j]:
            home_rc.append((i, j))
        if 2 == arr[i][j]:
            restorant_rc.append((i, j))

distances = [[0]*len(restorant_rc) for _ in range(len(home_rc))]
for i in range(len(home_rc)):
    for j in range(len(restorant_rc)):
        distances[i][j] = abs(home_rc[i][0] - restorant_rc[j][0]) + abs(home_rc[i][1] - restorant_rc[j][1])

def combo(depth, idx): # 조합
    global result
    if depth == M:
        total = 0

        # 모든 집에 대해
        for home_idx in range(len(home_rc)):

            # 최소 거리 치킨집 선정
            min_distance = float('inf')
            for chicken_idx in pick_number:
                distance = distances[home_idx][chicken_idx]
                min_distance = min(distance, min_distance)

            total += min_distance

            if total >= result:
                return

        result = total
        return
    
    for i in range(idx, len(restorant_rc)):
        pick_number.append(i)
        combo(depth + 1, i + 1)
        pick_number.pop()

combo(0,0)
print(result)