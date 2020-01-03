import os
import subprocess

def pollscripts(dirname):
    listoffiles = os.listdir(dirname)
    polls = list()
    for f in listoffiles:
        fullpath = os.path.join(dirname, f)
        if os.path.isdir(fullpath):
            continue
        if f[0] == 'S' and f[-1] == 'y':
            polls.append(fullpath)
    return polls


if __name__ == "__main__":
    while True:
        try:
            for s in pollscripts("./dynamic/poll"):
                subprocess.run(["python3", s])
        except Exception as e:
            print(e)

