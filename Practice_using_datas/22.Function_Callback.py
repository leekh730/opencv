def callback1(a,b):
    print("callback1 = {}".format(a+b))

def callback2(a):
    print("callback2 = {}".format(a**2))

def callback3():
    print("callback1 = Hello, World!")

def callthecallback(callback = None, cargs = ()):
    print("Call the Callback")
    if callback != None:
        callback(*cargs)

callthecallback(callback1, cargs=(1,2))
callthecallback(callback2, cargs=(2,))
callthecallback(callback3)