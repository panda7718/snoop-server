export PY_BIN=/home/cabox/.pyenv/shims/python3 && \
mkdir -p ~/workspace/ && \
rm -rf ~/workspace/snoop-server && \
cd ~/workspace && \
git clone https://github.com/panda7718/snoop-server.git && \
cd snoop-server && \
$PY_BIN -m pip install -r requirements.txt && \
$PY_BIN snoop-server.py >> snoopserver.out 2>>snoopserver.out