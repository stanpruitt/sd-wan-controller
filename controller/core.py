from controller.baseproc import BaseProc

class Core(BaseProc):

    def run(self):
        v = self._coreQueue.get()
        self._northQueue.put(v)
        pass

