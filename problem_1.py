def sqrt(number):
    llimit = 0
    ulimit = number
    
    if number ==0:
        return number
    if number <0:
        return 'No Real square root exist'
    
    while llimit<ulimit:
        check = (llimit + ulimit)//2

        if check*check == number:
            return check

        if llimit == ulimit-1:
            ulimit = llimit

        if check*check > number:
            ulimit = check

        if check*check<number:
            llimit = check
    return check

# Test case 1 perfect root
print(sqrt(121))
# 11

# Test case 2 perfect root
print(sqrt(0))
# 0

# Test case 3 perfect root
print(sqrt(83))
# 9

# Test case 4 perfect root
print(sqrt(127.32323))
# 11.0

# Test case 5 perfect root
print(sqrt(-4))
# No Real square root exist