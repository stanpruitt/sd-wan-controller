from controller.baseproc import BaseProc

class North(BaseProc):

    def run(self):
        print(self._northQueue.get())
        pass

