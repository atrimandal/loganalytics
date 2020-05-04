import sys

buffer = ''
for line in sys.stdin:
    cur = line.strip()
    #get the regular expression or demarcator for the timestamped line
    if not cur.startswith('['):
        buffer += cur
    else:
        if len(buffer) > 0:
            print buffer
        buffer = cur
