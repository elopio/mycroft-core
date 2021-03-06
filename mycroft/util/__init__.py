import os
import subprocess
from os.path import dirname

import psutil

__author__ = 'jdorleans'


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def play_wav(file_path):
    return subprocess.Popen(["aplay", file_path])


def play_mp3(file_path):
    return subprocess.Popen(["mpg123", file_path])


def record(file_path, duration, rate, channels):
    if duration > 0:
        return subprocess.Popen(["arecord", "-r", str(rate), "-c", str(channels), "-d", str(duration), file_path])
    else:
        return subprocess.Popen(["arecord", "-r", str(rate), "-c", str(channels), file_path])


def remove_last_slash(url):
    if url and url.endswith('/'):
        url = url[:-1]
    return url


def read_stripped_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def read_dict(filename, div='='):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            (key, val) = line.split(div)
            d[key.strip()] = val.strip()
    return d


def create_file(filename):
    try:
        os.makedirs(dirname(filename))
    except OSError:
        pass
    with open(filename, 'w') as f:
        f.write('')


def kill(names):
    print psutil.pids()
    for name in names:
        for p in psutil.process_iter():
            try:
                if p.name() == name:
                    p.kill()
                    break
            except:
                pass

class CerberusAccessDenied(Exception):
    pass