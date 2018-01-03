import math

def day11star1():
    f = open('inputDay11Star1.txt')
    directions = f.readline().split(',')
    i = 0
    j = 0
    k = 0

    for x in range(0, len(directions)):
        if directions[x] == 'n':
            i += 1
        if directions[x] == 's':
            i -= 1
        if directions[x] == 'ne':
            j += 1
        if directions[x] == 'sw':
            j -= 1
        if directions[x] == 'nw':
            k += 1
        if directions[x] == 'se':
            k -= 1
    
    prev = None
    while (prev != [i, j, k]):
        prev = [i, j, k]
        if (j > 0 and k > 0):
            diff = min(j, k)
            i  += diff
            j -= diff
            k -= diff
        if (j < 0 and k < 0):
            diff = max(j, k)
            i += diff
            j -= diff
            k -= diff

        if (j > 0 and i < 0):
            diff = -1 * min(-1 * i, j)
            k += diff
            i -= diff
            j += diff
        if (j < 0 and i > 0):
            diff = min(-1 * j, i)
            k += diff
            i -= diff
            j += diff

        if (i > 0 and k < 0):
            diff = min(-1 * k, i)
            j += diff
            i -= diff
            k += diff
        if (i < 0 and k > 0):
            diff = -1 * min(-1 * i, k)
            j += diff
            i -= diff
            k += diff
    print(sum(list(map(math.fabs, [i, j, k]))))

    
    
        
def day11star2():
    f = open('inputDay11Star1.txt')
    directions = f.readline().split(',')
    i = 0
    j = 0
    k = 0
    max_dist = 0
    for x in range(0, len(directions)):
        if directions[x] == 'n':
            i += 1
        if directions[x] == 's':
            i -= 1
        if directions[x] == 'ne':
            j += 1
        if directions[x] == 'sw':
            j -= 1
        if directions[x] == 'nw':
            k += 1
        if directions[x] == 'se':
            k -= 1
        
        prev = None
        while (prev != [i, j, k]):
            prev = [i, j, k]
            if (j > 0 and k > 0):
                diff = min(j, k)
                i  += diff
                j -= diff
                k -= diff
            if (j < 0 and k < 0):
                diff = max(j, k)
                i += diff
                j -= diff
                k -= diff

            if (j > 0 and i < 0):
                diff = -1 * min(-1 * i, j)
                k += diff
                i -= diff
                j += diff
            if (j < 0 and i > 0):
                diff = min(-1 * j, i)
                k += diff
                i -= diff
                j += diff

            if (i > 0 and k < 0):
                diff = min(-1 * k, i)
                j += diff
                i -= diff
                k += diff
            if (i < 0 and k > 0):
                diff = -1 * min(-1 * i, k)
                j += diff
                i -= diff
                k += diff
        max_dist = max(max_dist, sum(list(map(math.fabs, [i, j, k]))))
    
    print(max_dist)
    
    


day11star2()