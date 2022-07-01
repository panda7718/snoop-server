from flask import Flask
from flask import request
import os
import subprocess
from threading import Thread, Event

app = Flask(__name__)

tool_subprocesses = {}


class MyThread(Thread):
    def __init__(self, event, command):
        Thread.__init__(self)
        self.stopped = event
        self.started = False
        self.command = command
        self.process = None

    def run(self):
        while not self.stopped.wait(0.5):
            if (not self.started):
                self.process = subprocess.Popen([self.command], stdout=subprocess.PIPE, shell=True)
                self.process.wait()
                self.started = True


@app.route('/')
def hello():
    return 'Hello snoop!'

@app.route('/exec/<name>', methods=['GET', 'POST', 'DELETE'])
def exec_tool(name):
    if (request.method == 'POST'):
        app.logger.info(f'executing tool {name}')
        json = request.get_json()
        command = json["command"]
        app.logger.info(f'{command}')
        thread = MyThread(Event(), f'eval "{command}"')
        tool_subprocesses[name] = thread
        thread.start()
        return 'Running'
    elif (request.method == 'GET'):
        if (tool_subprocesses[name] != None):
            return 'Running'
        return 'Not running'
    else:
        app.logger.info(f'stopping tool {name}')
        if (tool_subprocesses.get(name) != None):
            tool_subprocesses[name].process.terminate()
            tool_subprocesses[name].stopped.set()
            tool_subprocesses.pop(name)
        return 'Not running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)