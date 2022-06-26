#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    	for line in sys.stdin:
            line=line.strip()
            splits=line.split("   ")
            if len(splits[2]) == 1:
                sys.stdout.write("00{}\t{}\t{}\n".format(splits[2],splits[0],splits[1]))
            elif len(splits[2]) == 2:
                sys.stdout.write("0{}\t{}\t{}\n".format(splits[2],splits[0],splits[1]))
            else:
                sys.stdout.write("{}\t{}\t{}\n".format(splits[2],splits[0],splits[1]))
