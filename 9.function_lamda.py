sum = lambda arg1, arg2 : arg1 + arg2
print("Value of total : ", sum(10,20))

nums = [1,2,3]

def is_greater_than_one(x):
    return x > 1
more_than_nums = filter(is_greater_than_one, nums)
print(list(more_than_nums))

more_than_nums = filter(lambda  x : x >1, nums) # 위 문장과 동일한 함수
print(list(more_than_nums))
