import json
import os

class Tunnel():
    def __init__(self, file = None, form = None, tunnelport=5555):
        self._error = "OK"
        if file != None:
            self.initfromfile(file)
        elif form != None:
            self.initfromForm(form, tunnelport)

    def result(self):
        return self._error

    def initfromForm(self, form, tunnelport):
        data = dict()
        for k, value in form.items():
            if len(value) == 0:
                self._error = "Error: empty parameters"
                return
            data[k] = value

        data["tunnelport"] = tunnelport
        self._data = data
        with open("tunnels/" + data["name"], 'w') as json_file:
            json.dump(data, json_file)
        pass

    def initfromfile(self, file):
        try:
            with open(file) as json_file:
                data = json.load(json_file)
            self._data = data
        except:
            self._data = dict()

    def name(self):
        return self._data["name"]

    def edge(self):
        return self._data["edge"]

    def wan(self):
        return self._data["wan"]

    def pedge(self):
        return self._data["pedge"]

    def pwan(self):
        return self._data["pwan"]

    def tunnelport(self):
        return self._data["tunnelport"]

    def data(self):
        return self._data

    def remove(self):
        os.remove("tunnels/" + self._data["name"])

