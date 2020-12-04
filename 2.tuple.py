#Tuples 안에 elements들 비교하기

def cmp(a,b):
    return (a > b) - (a < b)
# ((456,'abc', 0) > (456, 'abc', 789)) - ((456,'abc', 0) < (456, 'abc', 789))
# 0 - 1
# -1

tuple1, tuple2 = (123,'xyz'), (456,'abc') # tuple1이 a로 대입, tuple2가 b로 대입
#즉, ((123,'xyz') > (456,'abc') - (123,'xyz') < (456,'abc')) 이 형태
print(cmp(tuple1, tuple2)) # -1, 123 > 456 = false로 '0'을 출력, xyz < abc = true로 '1'을 출력. 즉, 0 - 1 = -1
print(cmp(tuple2, tuple1)) # 1, 456 > 123 = true로 '1', abc < xyz = false로 '0', 즉 1 - 0 = 1

tuple3 = tuple2 + (789,) # 789 추가
print(tuple3)

# ((456,'abc', 0) > (456, 'abc', 789)) - ((456,'abc', 0) < (456, 'abc', 789))
# 0 - 1
# -1
print(cmp(tuple2, tuple3)) # 위와 같이 계산이 되어 -1이 출력된다.

# 첫번째 인자들 부터 순차적으로 비교가 되며, 그 해당 결과 값이 출력이 된다.
# 그러나, 인자들이 동일한 값으로 되어 있다면 순차적으로 비교하여 비교가 되는 인자들의 결과값을 출력해준다.