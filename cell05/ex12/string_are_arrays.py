import sys
import re
if len(sys.argv) == 2 and ("z" in str(sys.argv[1])):
    print(str.join("", (re.findall(rf"z", str(sys.argv[1])))))
else :
    print("none")
