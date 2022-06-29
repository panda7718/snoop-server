from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

tool_subprocesses = {}

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/exec/<name>', methods=['GET', 'POST', 'DELETE'])
def exec_tool(name):
    if (request.method == 'POST'):
        print(f'executing tool {name}')
        tool_subprocesses[name] = 'started'
        return 'Running'
    elif (request.method == 'GET'):
        if (tool_subprocesses[name] != None):
            return 'Running'
        return 'Not running'
    else:
        print(f'stopping tool {name}')
        tool_subprocesses.pop(name)
        return 'Not running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)