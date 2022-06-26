#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 

if __name__ == "__main__":
    for line in sys.stdin:
        line_split = line.split(",")
        print("{}\t{}".format(line_split[3],line_split[4]))
