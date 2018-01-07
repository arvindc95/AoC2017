import math

# class Node:
#     def __init__(self, val, conn_nodes = []):
#         self.val = val
#         self.nodes = {}
#         for node in conn_nodes:
#             self.nodes[node] = Node(node)

            
def day12star1():
    programs = {}
    f = open('inputDay12Star1.txt')
    for line in f.readlines():
        ids = line.split(' <-> ')
        conn_ids = ids[1][:-1].split(', ')
        programs[ids[0]] = conn_ids
    count = 1
    visited = set(['0'])
    unvisited = set(programs['0'])
    while len(unvisited) > 0:
        program = unvisited.pop()
        visited.add(program)
        count += 1
        [unvisited.add(prog_id) for prog_id in set(programs[program]).difference(visited)]
    print(visited, unvisited)
    print(count)
    
    
        
# def day12star2():
    
    


day12star1()