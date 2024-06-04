def squar_num(x):
    return x ** 2

def is_odd(x):
    return x % 2


in_data = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(squar_num, filter(is_odd, in_data))
print(list(result))
