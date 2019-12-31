class BaseProc():
    def __init__(self, southQueue, coreQueue, northQueue):
        self._southQueue = southQueue
        self._coreQueue = coreQueue
        self._northQueue = northQueue

    def run(self):
        pass