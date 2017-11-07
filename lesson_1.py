import sys

LENGTH = 109

if __name__ == '__main__':
    v = int(sys.stdin.readline())
    t = int(sys.stdin.readline())
    #print('v = {0}, t = {1}'.format(v, t))
    if t < 0 or t > 1000:
        sys.exit(1)
    if v < -1000 or v > 1000:
        sys.exit(1)
    s = v * t
    s1 = None
    if v > 0:
        s1 = s -  (s // LENGTH) * LENGTH
    else:
        s1 = abs((s // LENGTH) * LENGTH) + s
    print(s1)
#sys.stdin.readline()
#sys.exit(0)
