
from subprocess import Popen, PIPE
from time import sleep
import threading
import re

class PipeReader(threading.Thread):
  def __init__(self, pipe):
    threading.Thread.__init__(self)
    self.read_buffer = ""
    self.pipe = pipe
    self.continue_reading = True

  def run(self):
    for line in self.pipe:
      if not self.continue_reading: break
      self.read_buffer += line


server_proc = None

def start_server():
  global server_proc
  server_proc = Popen(["java", "-jar", "server/ROOT.war"], stdout=PIPE)
  reader = PipeReader(server_proc.stdout)
  reader.start()
  server_ready = False
  for i in range(1, 30):
    sleep(0.5)
    if re.search("^.*Winstone Servlet Engine.* running.*$",reader.read_buffer):
      server_ready = True
      break
  reader.continue_reading = False

def stop_server():
  global server_pid
  try:
    server_proc._process.destroy()
  except IOError:
    pass

