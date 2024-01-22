import sys
sys.setrecursionlimit(10**4)

graph = []

def postorder(first, end):
    if first > end:
        return
    
    right = end + 1

    for i in range(first + 1, end + 1):
        if graph[first] < graph[i]:
            right = i
            break
    
    postorder(first + 1, right - 1)
    postorder(right, end)

    print(graph[first])
    
if __name__ == "__main__":
    
    graph = []
    while True:
        try : 
            graph.append(int(input()))
        except:
            break

    postorder(0, len(graph) - 1)
