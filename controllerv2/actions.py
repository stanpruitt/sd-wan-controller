from datetime import datetime

class Action():
    def __init__(self, id, name, param1):
        self._name = name
        self._param1 = param1
        self._start = datetime.now().strftime("%H:%M:%S")
        self._status = ""
        self._desc = ""
        self._id = id
        pass

    def id(self):
        return self._id

    def param1(self):
        return self._param1

    def setdesc(self, desc):
        self._desc = desc

    def setstatus(self, status):
        self._status = status

    def data(self):
        d = dict()
        d["id"] = self._id
        d["name"] = self._name
        d["start"] = self._start
        d["status"] = self._status
        d["desc"] = self._desc
        return d


class Actions():
    def __init__(self, core):
        self._list = list()
        self._id = 0
        self._core = core
        pass

    def actionresult(self, actionID, result):
        for a in self._list:
            if actionID == str(a.id()):
                a.setstatus(result)
                break

    def addaction(self, name, param1):
        action = Action(self._id, name, param1)
        self._id += 1
        self._list.append(action)
        if name == "newtunnel":
            self.newtunnel(action)
        elif name == "deltunnel":
            self.deltunnel(action)

    def list(self): #for display
        rl = list()
        for item in self._list:
            rl.append(item.data())
        return rl

    def newtunnel(self, action):
        action.setdesc("New tunnel: " + action.param1().name())
        #check if edge pair is exist
        try:
            edge = self._core.edge(action.param1().edge())
            pedge = self._core.edge(action.param1().pedge())
            action.setstatus("Waiting for setup ...")
            # TODO, we should check if any action is pending for perform
            serverip = edge.getip(action.param1().wan())

            edge.newtunnel((action.id(), None, action.param1().wan()), action, action.param1().tunnelport())
            pedge.newtunnel((action.id(), serverip, action.param1().pwan()), action, action.param1().tunnelport())
        except Exception as e:
            action.setstatus("Error  " + str(e))


    def deltunnel(self, action):
        action.setdesc("Delete tunnel: " + action.param1().name())
        try:
            edge = self._core.edge(action.param1().edge())
            pedge = self._core.edge(action.param1().pedge())
            action.setstatus("Waiting for delete ...")
            # TODO, we should check if any action is pending for perform
            edge.deltunnel(action, action.param1().tunnelport())
            pedge.deltunnel(action, action.param1().tunnelport())
        except Exception as e:
            action.setstatus("Error  " + str(e))


if __name__ == "__main__":
    acts = Actions(None)
    acts.addaction("newtunnel", '{"name":"fff"}')
    acts.addaction("newtunnel", '{"name":"fff"}')
    for d in acts.list():
        print(d)