from controllerv2.edge import Edge
from os import listdir

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




