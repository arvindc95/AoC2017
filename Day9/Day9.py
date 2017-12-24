def day9star1():
    f = open('inputDay9Star1.txt')
    chars = f.readline()
    score = 0
    groups = []
    i = 0
    while i < len(chars):
        if chars[i] == '!':
            i += 2 # could throw index error
        elif chars[i] == '<':
            while chars[i] != '>':
                if chars[i] == '!':
                    i += 2 # could throw index error
                else:
                    i += 1
        elif chars[i] == '{':
            groups.append(chars[i])
            i += 1
        elif chars[i] == '}':
            score += len(groups)
            groups.pop() # does popping empty list throw error?
            i += 1
        else:
            i += 1
    print("Score:", score)
        
def day9star2():
    f = open('inputDay9Star1.txt')
    chars = f.readline()
    garbage = 0
    score = 0
    groups = []
    i = 0
    while i < len(chars):
        if chars[i] == '!':
            i += 2 # could throw index error
        elif chars[i] == '<':
            i += 1
            while chars[i] != '>':
                if chars[i] == '!':
                    i += 2 # could throw index error
                else:
                    i += 1
                    garbage += 1
        elif chars[i] == '{':
            groups.append(chars[i])
            i += 1
        elif chars[i] == '}':
            score += len(groups)
            groups.pop() # does popping empty list throw error?
            i += 1
        else:
            i += 1
    print("Score:", score)
    print("Garbage:", garbage)

day9star2()