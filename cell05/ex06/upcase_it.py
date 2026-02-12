import sys
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(str(arg).upper())
else:
    print("none")
