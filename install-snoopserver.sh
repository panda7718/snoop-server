mkdir -p ~/workspace/ && \
rm -rf ~/workspace/snoop-server && \
cd ~/workspace && \
git clone https://github.com/panda7718/snoop-server.git && \
cd snoop-server && \
python manage.py runserver 0:8000 >> snoopserver.out 2>>snoopserver.out