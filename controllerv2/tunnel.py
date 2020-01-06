import json
import os

class Tunnel():
    def __init__(self, file = None, form = None):
        self._error = "OK"
        if file != None:
            self.initfromfile(file)
        elif form != None:
            self.initfromForm(form)

    def result(self):
        return self._error

    def initfromForm(self, form):
        data = dict()
        for k, value in form.items():
            if len(value) == 0:
                self._error = "Error: empty parameters"
                return
            data[k] = value

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


    def data(self):
        return self._data

    def remove(self):
        os.remove("tunnels/" + self._data["name"])

