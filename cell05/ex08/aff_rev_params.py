import sys
if len(sys.argv) > 1:
    for arg in reversed(sys.argv[1:]):
        print(str(arg))
else:
    print("none")