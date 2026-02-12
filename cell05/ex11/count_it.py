import sys
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(f"{str(arg)}: {len(str(arg))}")
else:
    print("none")
