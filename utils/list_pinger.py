import os
import platform
import subprocess

def ping(target_server):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', target_server), shell=True)
    except Exception as e:
        return 'False'
    else:
        return 'True'