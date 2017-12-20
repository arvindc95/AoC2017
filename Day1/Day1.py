def day1star1():
    f = open('inputDay1Star1.txt')
    numbers = f.readline()
    length = len(numbers)
    sum = 0
    for i in range(0, length):
        if numbers[i] == numbers[(i + 1) % length]:
            sum += int(numbers[i])
    print("Captcha:", sum)

def day1star2():
    f = open('inputDay1Star1.txt')
    numbers = f.readline()
    half_len = len(numbers) // 2
    sum = 0
    for i in range(0, half_len):
        if numbers[i] == numbers[i + half_len]:
            sum += int(numbers[i]) * 2
    print("Captcha:", sum)
day1star2()