#!/usr/bin/env python
#
#  Usage:
#    ./pyguard.py path  ext1,ext2,extn cmd
#
#  Example:
#     ./pyguard.py ./mydir .py "make pyc"
#
#  Dependencies:
#    Linux, python3, pyinotify

import subprocess
import sys
import pyinotify

class OnWriteHandler(pyinotify.ProcessEvent):
    def my_init(self, cwd, extensions, cmd):
        self.cwd = cwd
        self.extensions=extensions.split(',')
        self.cmd = cmd

    def _run_cmd(self):
        print('==> Modifications detected...')
        subprocess.call(self.cmd.split(' '), cwd=self.cwd)

    def process_IN_MODIFY(self, event):
        if all(not event.pathname.endswith(ext) for ext in self.extensions):
            return
        self._run_cmd()

def py_guard(path, extensions, cmd):
    wm = pyinotify.WatchManager()
    handler = OnWriteHandler(cwd=path, extensions=extensions, cmd=cmd)
    notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
    wm.add_watch(path,pyinotify.ALL_EVENTS, auto_add=True)
    print("==> Start monitoring {} (type c^c to exit)".format(path))
    notifier.loop()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Command line error: missing argument(s).", file=sys.stderr)
        sys.exit(1)

# Required arguments
    path = sys.argv[1]
    extensions = sys.argv[2]

# Optional argument
    cmd = "make"
    if len(sys.argv) == 4:
        cmd = sys.arg[3]

# Blocks monitoring
    py_guard(path, extensions, cmd)

