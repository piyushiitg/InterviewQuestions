import time

def tailf(filename):
    f = open(filename, 'r')
    avg_size = 10
    to_read = 5 
    f.seek(-(avg_size*to_read),2)
    print f.tell()
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    for i in tailf(filename):
        print i,
