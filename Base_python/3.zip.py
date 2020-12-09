#enumerate : 열거하다라는 뜻, 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
#enumerate 함수는 보통 for문과 함께 자주 사용함, for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 사용
some_list = ['foo', 'bar', 'baz']
for index, value in enumerate(some_list):
    print('x : {}, y: {}'.format(index, value))

#zip, 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'seven']
seq3 = ['samsung', 'apple', 'lg']
seq4 = ['python', 'cpp']
for a, b, c in zip(seq1, seq2, seq3):
    print('x : {}, y : {}, z : {} '.format(a,b,c))
    print('1 : {1}, 2 : {2}, 3 : {0}'.format(a,b,c))

for a, b, c in zip(seq1, seq2, seq4): # seq4에 3번째 인자가 없기때문에 출력은 2개만 된다.
    print('x : {}, y : {}, z : {} '.format(a,b,c))
    print('1 : {1}, 2 : {2}, 3 : {0}'.format(a,b,c))
