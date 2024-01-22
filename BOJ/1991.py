
def preorder(graph, s):
    print(chr(s + ord('A')), end='')
    if graph[s][0] != ' ':
        preorder(graph, graph[s][0])
    if graph[s][1] != ' ':
        preorder(graph, graph[s][1])

def inorder(graph, s):
    if graph[s][0] != ' ':
        inorder(graph, graph[s][0])
    print(chr(s + ord('A')), end='')
    if graph[s][1] != ' ':
        inorder(graph, graph[s][1])

def postorder(graph, s):
    if graph[s][0] != ' ':
        postorder(graph, graph[s][0])
    if graph[s][1] != ' ':
        postorder(graph, graph[s][1])
    print(chr(s + ord('A')), end='')




if __name__ == "__main__":
    n = int(input())

    graph = [[] for _ in range(n)]
    
    for i in range(n):
        ro, l ,r = map(str, input().split())
        if l != '.':
            graph[ord(ro) - ord('A')].append(ord(l) - ord('A'))
        else:
            graph[ord(ro) - ord('A')].append(' ')
        if r != '.':
            graph[ord(ro) - ord('A')].append(ord(r) - ord('A'))
        else:
            graph[ord(ro) - ord('A')].append(' ')
    preorder(graph, 0)
    print()
    inorder(graph, 0)
    print()
    postorder(graph, 0)