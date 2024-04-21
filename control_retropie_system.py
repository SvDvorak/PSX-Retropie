#!/usr/bin/python3 -u

import errno
import os
import re
import shutil
import signal
import socket
import subprocess
import time
from pathlib import Path

class vars():
    pid_timeout = 10        # Timeout PID wait after 10sec
    sleep_time = 0.2        # Sleep for 1/5sec while polling

def touch_file(pathstr):
    Path(pathstr).touch()
    shutil.chown(pathstr, "pi", "pi")

def get_pid(ex):
    pid = 0
    try:
        pid_str = subprocess.check_output(['pgrep', '-f', '-o', ex]).strip().decode()
        pid = int(pid_str)
    finally:
        return pid

def get_run_pid():
    ex = '/opt/retropie/supplementary/runcommand/runcommand.sh'
    return get_pid(ex)

def get_es_pid():
    ex = '/opt/retropie/supplementary/.*/emulationstation([^.]|$)'
    return get_pid(ex)

def wait_pid(pid):
    if pid < 1:
        return False                # Invalid PID
    wait_counter = 0
    hold_time = vars.pid_timeout / vars.sleep_time
    while True:
        wait_counter += 1
        if wait_counter > hold_time:
            return False            # Timeout
        try:
            os.kill(pid, 0)
        except OSError as err:
            if err.errno == errno.ESRCH:
                return True         # No such PID
        time.sleep(vars.sleep_time)

def quit_emulator():
    run_pid = get_run_pid()
    if run_pid:
        net_command("QUIT")
        wait_pid(run_pid)

def kill_es():
    quit_emulator()
    es_pid = get_es_pid()
    if es_pid:
        os.kill(es_pid, signal.SIGTERM)
        wait_pid(es_pid)

def net_command(command):           # RetroArch network command
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("127.0.0.1", 55355))
    except socket.error as err:
        print("Socket error: ", err)
    else:
        s.send(command.encode())
    finally:
        if s: s.close

def restart_es():
    es_pid = get_es_pid()
    if es_pid:
        touch_file("/tmp/es-restart")
        os.kill(es_pid, signal.SIGTERM)

def do_reset():
    if get_run_pid():
        net_command("RESET")
    else:
        restart_es()

def do_quit():
    quit_emulator()

def do_reboot():
    kill_es()
    os.system("sudo reboot")

def do_shutdown():
    kill_es()
    os.system("sudo shutdown -h now")