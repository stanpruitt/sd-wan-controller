from controllerv2.edge import Edge
from controllerv2.tunnel import Tunnel
from os import listdir
from controllerv2.actions import Actions

class Singleton:
   __instance = None

   @staticmethod
   def getInstance():
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
         self._edges = self.loaddata()
         self._tunnels = self.loadtunnels()
         self._actions = Actions(self)
#         print(self._edges)

   def getresponse(self, edgeSN):
      try:
         edge = self._edges[edgeSN]
      except KeyError:
         edge = Edge(file = None, SN = edgeSN)
         self._edges[edgeSN] = edge

      return edge.getresponse()

   def queryCMD(self, edgeSN, form):
      try:
         edge = self._edges[edgeSN]
      except KeyError:
         edge = Edge(file = None, SN = edgeSN)
         self._edges[edgeSN] = edge

      return edge.queryCMD(form)

   def loaddata(self):
      edges = dict()
      for f in listdir("./data/"):
         if len(f) != 8:
            continue
         edge = Edge("./data/" + f, SN = None)
         edges[edge.getSN()] = edge
      return edges

   def fatedges(self):
      fats = list()
      for SN, edge in self._edges.items():
         data = edge.data()
         try:
            if data["type"] == "fatedge":
               fats.append(data)
         except Exception:
            pass


      return fats

   def thinedges(self):
      thins = list()
      for SN, edge in self._edges.items():
         data = edge.data()
         try:
            if data["type"] == "thinedge":
               thins.append(data)
         except Exception:
            pass


      return thins

   def loadtunnels(self):
      tunnels = dict()
      for f in listdir("./tunnels/"):
         tunnel = Tunnel("./tunnels/" + f, form = None)
         tunnels[tunnel.name()] = tunnel
      return tunnels


   def newtunnel(self, form):
      try:
         if form["name"] in self._tunnels.keys():
            return "tunnel <" + form["name"] + "> is exist, please delete it at first"
      except Exception as e:
         return str(e)

      tunnel = Tunnel(file = None, form = form)
      if tunnel.result() != "OK":
         return tunnel.result()
      self._tunnels[tunnel.name()] = tunnel
      self._actions.addaction("newtunnel", tunnel)
      return tunnel.result()

   def tunnels(self):
      tlist = list()
      for k, v in self._tunnels.items():
         tlist.append(v.data())
      return tlist

   def deletetnl(self, form):
      tunnel = self._tunnels[form["tunnelname"]]
      tunnel.remove()
      del self._tunnels[form["tunnelname"]]
      self._actions.addaction("deltunnel", tunnel)
      return self._tunnels

   def actions(self):
      return self._actions.list()

   def edge(self, name):
      for k, v in self._edges.items():
         if name == v.name():
            return v

      raise Exception("edge " +  name + " is not exist")

   def actionresult(self, actionID, result):
      self._actions.actionresult(actionID, result)