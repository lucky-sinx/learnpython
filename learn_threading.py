import threading
import time
from queue import Queue


def print_start_end(func):
    def wrapper():
        print("{} start".format(func.__name__))
        func()
        print("{} end".format(func.__name__))

    return wrapper


@print_start_end
def t1_job():
    # print('this is new thread,num is {}'.format(threading.current_thread()))
    for i in range(10):
        time.sleep(0.1)


@print_start_end
def t2_job():
    time.sleep(5)


@print_start_end
def main1():
    add_thread = threading.Thread(target=t1_job, name="t1")
    thread2 = threading.Thread(target=t2_job, name="t1")
    add_thread.start()
    thread2.start()
    add_thread.join()
    # thread2.join()

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


def job3(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


@print_start_end
def t3_job(data=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job3, args=(data[i], q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    res = []
    for i in range(4):
        res.append(q.get())
    print(res)


def main2():
    t3_job()


def job4():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job4:{}'.format(A))
        time.sleep(0.1)
    lock.release()


def job5():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job5:{}'.format(A))
        time.sleep(0.1)
    lock.release()


def main3():
    t4 = threading.Thread(target=job4)
    t5 = threading.Thread(target=job5)
    t4.start()
    t5.start()
    t4.join()
    t5.join()


if __name__ == "__main__":
    A = 0
    lock = threading.Lock()
    # main1()
    # main2()
    main3()
