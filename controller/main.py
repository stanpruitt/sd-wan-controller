from multiprocessing import Process, Queue
from controller.south import South
from controller.core import Core
from controller.north import North

#referene multiprocess
#https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue

def south_flask(southQueue, coreQueue, northQueue):
    south = South(southQueue, coreQueue, northQueue)
    south.run()
    pass

def core_process(southQueue, coreQueue, northQueue):
    south = Core(southQueue, coreQueue, northQueue)
    south.run()
    pass

def north_flask(southQueue, coreQueue, northQueue):
    south = North(southQueue, coreQueue, northQueue)
    south.run()
    pass



if __name__ == "__main__":
    southQueue = Queue()
    coreQueue = Queue()
    northQueue = Queue()

    southFlask = Process(target=south_flask, args=(southQueue, coreQueue, northQueue))
    coreProcess = Process(target=core_process, args=(southQueue, coreQueue, northQueue))
    northFlask = Process(target=north_flask, args=(southQueue, coreQueue, northQueue))


    southFlask.start()
    northFlask.start()
    coreProcess.start()

    southFlask.join()
    northFlask.join()
    coreProcess.join()
    pass