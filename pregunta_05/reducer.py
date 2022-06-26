#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    currkey = None
    total = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if currkey == key:
            total += val
        else:
            if currkey is not None:
                print("{}\t{}".format(currkey, total))
            currkey = key
            total = val
    print("{}\t{}".format(currkey, total))
