import sys
import subprocess

import pyperclip
import rofi

from general import get_kp

entries = open('entries').read().split('\n')
r = rofi.Rofi()
index, _ = r.select('Select entry', entries)
if index < 0:
    sys.exit(0)
kp = get_kp()
password = kp.entries[index].password
pyperclip.copy(password)
subprocess.call(['xdotool', 'type', password])

