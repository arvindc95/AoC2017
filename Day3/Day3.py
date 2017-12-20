import re

def day2star1():
    f = open('inputDay2Star1.txt')
    rows = f.readlines()
    checksum = 0
    for row in rows:
        regex = re.compile(r'\s+')
        cells = regex.sub(',', row).split(',')[:-1]
        max = int(cells[0])
        min = int(cells[0])
        for cell in cells:
            num = int(cell)
            if (num >= max):
                max = num
            if (num <= min):
                min = num
        checksum += (max - min)
    print("Checksum:", checksum)

def day2star2():
    f = open('inputDay2Star1.txt')
    rows = f.readlines()
    checksum = 0
    for row in rows:
        regex = re.compile(r'\s+')
        cells = regex.sub(',', row).split(',')[:-1]
        max = int(cells[0])
        min = int(cells[0])
        for cell in cells:
            num = int(cell)
            for test_cell in cells:
                test_num = int(test_cell)
                if (num % test_num == 0 and num != test_num):
                    checksum += int(num / test_num)
    print("Checksum:", checksum)
day2star2()