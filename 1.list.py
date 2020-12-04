#복합 자료형 List 구현과 이해
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies)

movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,2018)
print(movies)

movies[5]=1983
print(movies)

movies.remove(1983)
print(movies)

movies.remove("The Holy Grail")
print(movies)

movies = [1975,"The Life of Brian", 2020, "The Greatest Show man", ['Forest Gump', ["Avengers", "Titanic", "Spider-man", "E.T"]]]
print(movies[4][1][2]) 
#리스트에 리스트에 리스트 구조, 첫번째 리스트에 4번째 인자에 두번째 리스트가 존재하고 2번째 리스트의 1번째 인자에 세번째 리스트가 존재하고 3번째 리스트에서 2번째 인자를 출력하라


result = isinstance(movies, list) #isinstance(object, class), 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 true or false를 출력해줌
                                  #movies가 list인가? true
print(type(isinstance), result)
