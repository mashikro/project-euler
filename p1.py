# https://projecteuler.net/problem=1

# natural nums == whole nums starting from 0 or 1. no negative nums or no fractions.

def generate_multiples_of_x(x, n):
    start = x
    mult = 1
    nums = []
    next_ = start
    while next_ < n:
        nums.append(start * mult)
        mult += 1
        next_ = start*mult
    print("------------------------------- x=", x)
    print(nums)
    return nums

# print(generate_multiples_of_x(3, 10))

# print(generate_multiples_of_x(5, 10))

def multiples(m1, m2, n):

    nums_m1 = generate_multiples_of_x(m1, n)
    nums_m2 = generate_multiples_of_x(m2, n)
    for num in nums_m2:
        if num not in nums_m1:
            nums_m1.append(num)
    return sum(nums_m1)

print(multiples(3,5,10)) #23
print(multiples(3,5,1000)) #233168