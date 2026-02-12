import sys
import re
if len(sys.argv) > 1:
    ism_check = True
    for arg in sys.argv[1:]:
        if "ism" in arg :
            ism_check = False
    if not ism_check :
        for arg in sys.argv[1:]:
            if "ism" not in arg :
                print(f"{str(arg)}ism")
    else :
        print("none")
else :
    print("none")
