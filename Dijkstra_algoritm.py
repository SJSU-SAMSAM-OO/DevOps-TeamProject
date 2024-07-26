import sys
input = sys.stdin.readline
INF = 1e9
'''다익스트라 알고리즘(최단경로 탐색 알고리즘)
하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려줌(음의 간선 포함x)
1.출발노드를 정한다.
2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다.
3. 방문하지 않은 노드 중 가장 비용이 작은 노드를 선택한다.
4. 해당 노드를 거쳐 특정한 노드로 가는 경우를 고려해 최소 비용을 갱신한다.
5. 3~4번 반복
'''

def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0     # 시작 노드는 0으로 초기화
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]   # 시작 노드와 연결된 노드들의 거리 입력

    for _ in range(n-1):
        now = get_smallest_node()   # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
        visited[now] = True

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:   # 기존에 입력된 값보다 더 작은 거리이면
                distance[j[0]] = distance[now] + j[1]   # 값 갱신


n, m = map(int, input().split())    # 정점과 간선 개수
k = int(input())    # 시작할 노드

visited = [False] * (n+1)   # 방문처리용
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)
print(distance)

