from controllerv2.edge import Edge

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
         self._edges = dict()

   def getresponse(self, edgeSN):
      try:
         edge = self._edges[edgeSN]
      except KeyError:
         edge = Edge(edgeSN)
         self._edges[edgeSN] = edge

      return edge.getresponse()