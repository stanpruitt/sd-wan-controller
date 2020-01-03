class Edge():
    def __init__(self, SN):
        self._SN = SN

    def getresponse(self):
        return '<xml>' \
               '<version option="optional" version="*"/>' \
               '<command line="python3 scripts/query.py"/>' \
               '</xml>'