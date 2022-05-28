import sys
def main(argv):
    edges = {}
    vals = [] 
    file = open(argv, "r")
    content = file.readlines()
    for i in range(0, len(content)):
        line = content[i].split(',')

        first = int(line[0])
        second = int(line[1])
        if first not in vals: 
            vals.append(first)

        if second not in vals: 
            vals.append(second)
    
        if first in edges.keys():
            edges[first].append(second)
        edges[first] = [second]




    ## Use modify dfs to find the paths of all possible cycles in given graph represented by edge list stored in dictionary
    def DFS(graph, initial, fin):
        res = [(initial, [])]
        while len(res) != 0:
            vertex, path = res.pop()
            if path and vertex != fin:
                pass
            elif path and vertex == fin: 
                yield path

            if vertex not in graph.keys():
                pass
            else:
                for nxt_vertex in graph[vertex]:
                    if nxt_vertex in path:
                        continue
                    res.append((nxt_vertex, path+[nxt_vertex]))

    cycles = []

    for vertices in edges: 
        for path in DFS(edges, vertices, vertices): 
            cycles.append([vertices] + path)


    def printer(cycles):
        count = 0
        res = []
        temp = []
        for i in cycles:
            for j in i: 
                if j not in temp:
                    temp.append(j)

        

        old_list = []
        for i in cycles: 
            old_list.append(list(set(i)))

        unique_data = [list(j) for j in set(tuple(i) for i in old_list)]
        
        finn = []
        for i in unique_data:
            finn.append(i)
        

        # Single Strongly Connected Components that only Have indegree 1 and out degree 0
        
        for i in vals: 
            if i not in temp:
                res.append([i])

        
        flag = len(res)
        while flag > 0: 
            finn.append(res[flag - 1])
            flag -= 1 
            
            
        for i in sorted(finn):
            if len(i) == 1:
                for j in i: 
                    count += 1 
            elif len(i) > 1:
                count += 1
        print(str(count) + " Strongly Connected Component(s):")
        
        for k in sorted(finn):
            if len(k) != 0: 
                print(str(k)[1:-1])
        return
    return printer(cycles)

if __name__ == "__main__":
    main(sys.argv[1]) 



def solver(list): 
    sum = 1
    for i in list:
        sum *= list[i]
    return sum 
print(solver([1,2,3,4,5]))