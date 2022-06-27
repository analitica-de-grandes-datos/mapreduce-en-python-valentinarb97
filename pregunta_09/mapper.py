#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for row in sys.stdin:
       
        divido = row.strip().split("   ")
        col00 = divido[0]
        col01 = divido[1]
        col02 = divido[2]
  
    
        sys.stdout.write(f"{col00}\t{col01}\t{col02}\n")
