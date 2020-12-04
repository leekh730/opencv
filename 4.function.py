def printinfo(fname, fage = 35):
    return fname, fage

name, age = printinfo(fage = 50, fname = "miki") #값을 지정했기 때문에 fname에는 "miki"가, fage에는 50이 대입됨
#fname은 0번째 인자, fage는 1번째 인자로 각각 name, age에 대입됨
print(name + "," + str(age)) # string과 string 끼리만 concatenate(연결)가 되기때문에 str(age)
print(name, age)

def changeme(fmylist):
    fmylist = [1,2,3,4]
    print("Values inside the function : ", fmylist)
    return

mylist = [10,20,30]
changeme(mylist)
print("Values outside the function : ", mylist)
