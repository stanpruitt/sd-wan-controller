import json

class Edge():
    def __init__(self, file = None, SN = None):
        if file != None:
            self.initfromfile(file)
        elif SN != None:
            self.initfromSN(SN)


    def initfromSN(self, SN):
        self._SN = SN
        #read parameters from database
        try:
            with open("data/" + SN) as json_file:
                data = json.load(json_file)
            self._data = data
        except:
            self._data = dict()

    def initfromfile(self, file):
        try:
            with open(file) as json_file:
                data = json.load(json_file)
            self._data = data
        except:
            self._data = dict()
        try:
            self._SN = self._data["sn"]
        except:
            self._SN = 0

    def data(self):
        return self._data

    def name(self):
        return self._data["name"]

    def getip(self, wan):
        try:
            wans = self._data["wans"]
            for w in wans.split(";"):
                its = w.split(",")
                if its[0] == wan:
                    return its[1]
                else:
                    raise
        except:
            raise(Exception("Can not get ip for wan " + wan))

    def getSN(self):
        return self._SN

    def getresponse(self):
        return '<xml>' \
               '<version option="optional" version="*"/>' \
               '<command line="python3 scripts/query.py"/>' \
               '</xml>'

    def queryCMD(self, form):
        update = False
        for k, value in form.items():
            try:
                oldv = self._data[k]
                if oldv != value:
                    update = True
                    self._data[k] = value
            except Exception as e:
                update = True
                self._data[k] = value
        print(update, self._data)
        if update:
            with open("data/" + self._SN, 'w') as json_file:
                json.dump(self._data, json_file)
        return "OK"

    def newtunnel(self, param):
        print(param)
        pass