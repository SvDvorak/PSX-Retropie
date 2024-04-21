#! /usr/bin/env python3

import os

def reset():
  pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

  for pid in pids:
    try:
      commandpath = ""
      with open(os.path.join('/proc', pid, 'cmdline'), 'r') as f:
        commandpath = f.read()
      if commandpath[0:24] == '/opt/retropie/emulators/':
        os.system('kill -QUIT %s' % pid)
        print('kill -QUIT %s' % pid)
    except IOError:
      continue