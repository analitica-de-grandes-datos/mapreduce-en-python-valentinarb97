#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        line=line.strip()
        splits=line.split("   ")
        sys.stdout.write("{}\t{}\n".format(splits[0],splits[2]))