
from subprocess import Popen
from time import sleep

server_process = None

def start_server():
  global server_process
  server_process = Popen(["java", "-jar", "server/ROOT.war"])
  sleep(5.0)

def stop_server():
  global server_process
  server_process.terminate()

