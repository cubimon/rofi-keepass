import sys

from general import get_kp

def description(entry):
    if entry.title:
        return entry.title
    elif entry.url:
        return entry.url
    else:
        return str(entry)

kp = get_kp()
entries = list(map(description, kp.entries))
open('entries', 'w').write('\n'.join(entries))

