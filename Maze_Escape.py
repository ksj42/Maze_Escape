from collections import deque

#input은 문자열
#split은 스페이스바를 기준으로 문자열을 분리
#map은 덩어리로된 문자숫자열을 숫자열로 형변환
n, m=map(int,input().split())
graph=[]
for i in range(n):
    #list로 넣어야 graph리스트에 들어감
    graph.append(list(map(int,input())))
    #print(graph)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    #출력해보면 큐에는 deque([]) 이렇게 저장된다.
    queue=deque()
    #append로 큐에 원소를 추가한다.
    queue.append((x,y))
    while queue:
        print(queue)
        print(graph)
        #큐에 있는 원소들중 가장 앞에 있는 원소(행값,열값 2개)를 x,y에 저장하고 큐에서 삭제한다.
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
