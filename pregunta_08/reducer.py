#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    curkey = None
    suma = 0
    counter = 1
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:

            suma += val
            counter += 1     
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(suma),suma/counter))
                counter = 1
            curkey = key
            suma = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(suma),suma/counter))
