import sys
import re
if len(sys.argv) == 3:
    print(len(re.findall(rf"{str(sys.argv[1])}", str(sys.argv[2]))))
else :
    print("none")
