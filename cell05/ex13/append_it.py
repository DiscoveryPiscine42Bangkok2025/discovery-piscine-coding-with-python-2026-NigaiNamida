import sys
import re
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
            print(f"{str(arg)}ism")
else :
    print("none")
