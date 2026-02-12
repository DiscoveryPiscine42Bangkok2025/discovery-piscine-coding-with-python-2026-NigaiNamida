import sys
if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        if num1 < num2:
            arr = []
            while num1 <= num2:
                arr.append(num1)
                num1 += 1
            print(arr)
        else:
            print("none")    
    except ValueError:
        print("none")
else:
    print("none")