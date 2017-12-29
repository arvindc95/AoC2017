ELEMENT_COUNT = 256

def day10star1():
    f = open('inputDay10Star1.txt')
    lengths = list(map(int, f.readline()))
    nums = list(range(0, ELEMENT_COUNT))
    index = 0
    skip = 0
    for length in lengths:
        if length > (ELEMENT_COUNT - index):
            first_section = nums[index:]
            non_reversed = nums[length - len(first_section):index]
            last_section = nums[:length - len(first_section)]
            reversed_section = (first_section + last_section)[::-1]
            nums = reversed_section[len(first_section):] + non_reversed + reversed_section[:len(first_section)]
        else:
            nums = nums[:index] + nums[index: index + length][::-1] + nums[index + length:]
        index = (index + length + skip) % ELEMENT_COUNT
        skip += 1
    print("First and second:", nums[0], nums[1], nums[0] * nums[1])
        
def day10star2():
    f = open('inputDay10Star1.txt')
    lengths = list(map(ord, f.readline())) + [17, 31, 73, 47, 23]
    nums = list(range(0, ELEMENT_COUNT))
    index = 0
    skip = 0
    for round in range(0, 64):
        for length in lengths:
            if length > (ELEMENT_COUNT - index):
                first_section = nums[index:]
                non_reversed = nums[length - len(first_section):index]
                last_section = nums[:length - len(first_section)]
                reversed_section = (first_section + last_section)[::-1]
                nums = reversed_section[len(first_section):] + non_reversed + reversed_section[:len(first_section)]
            else:
                nums = nums[:index] + nums[index: index + length][::-1] + nums[index + length:]
            index = (index + length + skip) % ELEMENT_COUNT
            skip += 1
    dense_hash = []
    for i in range(0, 256, 16):
        xor_val = nums[i]
        for num in nums[i + 1:i + 16]:
            xor_val ^= num
        dense_hash += [xor_val]
    dense_hash = ['0' + hex(x)[2:] if len(hex(x)) == 3 else hex(x)[2:] for x in dense_hash]
    hash_str = ''
    for hex_val in dense_hash:
        hash_str += hex_val
    print("Dense hash:", hash_str)


day10star2()