from controller.baseproc import BaseProc
from flask import Flask, request, Response

class EndpointAction(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        # Perform the action
        answer = self.action()
        # Create the answer (bundle it in a correctly formatted HTTP answer)
        self.response = Response(answer, status=200, headers={})
        # Send it
        return self.response


class South(BaseProc):

    def run(self):
        self._app = Flask(__name__)
        self.add_all_endpoints()
        self._app.run(debug=True)
        pass

    def add_all_endpoints(self):
        # Add root endpoint
#        self.add_endpoint(endpoint="/", endpoint_name="/", handler=self.action)
        self.add_endpoint(endpoint="/tunnel/create", endpoint_name="/tunnel/create", handler=self.action)


    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self._app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler), methods = ['POST', 'GET'])
        # You can also add options here : "... , methods=['POST'], ... "

    def action(self):
        if request.method == "POST":
            print(request.form)
            self._coreQueue.put(request.form)
            return "import subprocess\n" \
                   "subprocess.run(['python3', '-Vaa'])"
        else:
            return "list"


'''

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
   if request.method == "POST":
      print(request.form)
      return "BAD"
   else:
      return "Hello Worlds"


if __name__ == '__main__':
   app.run(debug = True)


'''