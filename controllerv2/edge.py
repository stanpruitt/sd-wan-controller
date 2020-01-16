import json

class Edge():
    def __init__(self, file = None, SN = None):
        if file != None:
            self.initfromfile(file)
        elif SN != None:
            self.initfromSN(SN)

        self._action = 0     #no action
        self._command = ""
        self._actionID = 0
        self._actionobj = None


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
            ip = self._data["map"][wan]
            return ip
        except:
            pass

        try:
            ip = self._data["wans"][wan]
            return ip
        except:
            raise(Exception("Can not get ip for wan " + wan))

    def getSN(self):
        return self._SN

    def oneactionxml(self, sn, actionid, actiontype, args):
        xml = '<xml>'
        xml += '<head version="1.0" sn="' + sn + '" actionid="' + actionid + '" actiontype="' + actiontype + '"/>'
        xml += '<subprocess>'
        xml += '<args>' + args + '</args>'
        xml += '</subprocess>'
        xml += '</xml>'
        return xml

    def getresponse(self):
        if self._action == 1:
            self._action = 2
            self._actionobj.setstatus("Device got the command, waiting...")
            return self._command
        else:
            xml = self.oneactionxml(self.getSN(), "0", "query", '["python3", "scripts/query.py"]')
            return xml

            '''
            return '<xml>' \
               '<version option="optional" version="*"/>' \
               '<command line="python3 scripts/query.py 0"/>' \
               '</xml>'
            '''

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

    def queryCMD2(self, astdout):
        update = False
        for k, value in astdout.items():
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

    def newtunnel(self, param, actionobj, tunnelport):
        if param[1] == None: # tunnel server
            #action = '<command line="python3 scripts/tunnel.py ' + str(param[0]) + ' server ' + param[2] + ' "/>'

            args = '["python3", "scripts/tunnel.py", "-s", "-p", "' + str(tunnelport) + '"]'
            ll = self.oneactionxml(self.getSN(), str(param[0]), "tunnel", args)
        else:
            #action = '<command line="python3 scripts/tunnel.py ' + str(param[0]) + ' client ' +
            # param[2] + ' ' + param[1] + ' "/>'

            args = '["python3", "scripts/tunnel.py", "-c", "' + param[1] + '", "-p", "'\
                   + str(tunnelport) + '", "-l", "10.139.37.' + str(tunnelport%100 + 1) + '"]'
            ll = self.oneactionxml(self.getSN(), str(param[0]), "tunnel", args)
#        ll = '<xml> <version option="optional" version="*"/> ' + action + '</xml>'
        print(ll, " for ", self.name())
        self._action = 1    #start
        self._command = ll
        self._actionID = param[0]
        self._actionobj = actionobj
        pass

    def deltunnel(self, actionobj, tunnelport):

        args = '["python3", "scripts/tunnel.py", "-d", "-p", "' + str(tunnelport) + '"]'
        ll = self.oneactionxml(self.getSN(), str(actionobj.id()), "tunnel", args)

        print(ll, " for ", self.name())
        self._action = 1    #start
        self._command = ll
        self._actionID = actionobj.id()
        self._actionobj = actionobj
        pass


