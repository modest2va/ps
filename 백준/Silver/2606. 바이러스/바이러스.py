def dfs(v):
    #print(v, end=" ")
    visited[v]=True
    empty.append(v)
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)





def bfs(v):
    q=[v]
    visited=[False]*(A+1)

    while q:
        v=q.pop(0)
        if not (visited[v]):
            visited[v]=True
            print (v, end=" ")
            for e in adj[v]:
                if not (visited[e]):
                    q.append(e)

A=int (input()) #number of node
B=int(input()) #nubmer of edge
C=1 #start node!

adj=[[] for _ in range(A+1)]
empty=[]
visited= [False]*(A+1)

for _ in range(B):
    a= input().split()
    adj[int(a[0])].append(int(a[1]))
    adj[int(a[1])].append(int(a[0]))

for e in adj:
    e.sort()

dfs(C)
print(int (len(empty))-1)
