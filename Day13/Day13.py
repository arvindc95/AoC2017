
     
def day13star1():
    severity = 0
    f = open('inputDay13Star1.txt')
    for line in f.readlines():
        depth, range = [int(x) for x in line[:-1].split(': ')]
        if depth % ((range - 1) * 2) == 0:
            severity += (depth * range)
    print(severity)
    
    
        
# def day13star2():
    
    


day13star1()