from controller.baseproc import BaseProc
from flask import Flask, request, Response, render_template

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
        self._coreQueue.put("hello world")
        self._app = Flask(__name__)
        self.add_all_endpoints()
        self._app.run(debug=True)
        pass

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET']):
        #self._app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler), methods = ['POST', 'GET'])
        self._app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler), methods)


    def add_all_endpoints(self):
        # Add root endpoint
        self.add_endpoint(endpoint="/", endpoint_name="/", handler=self.index)
        self.add_endpoint(endpoint="/index.html", endpoint_name="/index.html", handler=self.index)
        self.add_endpoint(endpoint="/index.htm", endpoint_name="/index.htm", handler=self.index)

        self.add_endpoint(endpoint="/todo/", endpoint_name="/todo/", handler=self.todo)

        self.add_endpoint(endpoint="/tunnel/create", endpoint_name="/tunnel/create", handler=self.action, methods=['POST'])

    def index(self):
        return self.overview()


    def todo(self):
        return render_template("todo.html")

    def overview(self):
        return render_template("overview.html")

    def action(self):
        if request.method == "POST":
            print(request.form)
            self._coreQueue.put(request.form)
            return "import subprocess\n" \
                   "subprocess.run(['python3', '-Vaa'])"
        else:
            return "NOT Supported"




