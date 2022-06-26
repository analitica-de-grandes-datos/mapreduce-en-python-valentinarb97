#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 

if __name__ == '__main__':
    
    curkey = None
    suma = 0
    counter = 0
    for line in sys.stdin:
        line = line.strip()
        val, key, date = line.split("\t")
        val = int(val)        
        if counter <= 5:
            sys.stdout.write("{}\t{}\t{}\n".format(key,date,val))
            counter += 1