from threading import Thread
import time



def test1():
    time.sleep(5)
    print ("hello")

def test2():
    print ("goodbye")


tr1 = Thread(target=test1)
tr2 = Thread(target=test2)

tr1.start()
tr2.start()