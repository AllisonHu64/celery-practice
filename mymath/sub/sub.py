import sys

def main():
    if len(sys.argv) <= 2:
        sys.exit("sub requires at least 2 argument.")
    
    try:
        num1 = int(sys.argv[1])
    except:
        sys.exit("arg1 %s is not an interger." % (sys.argv[1]))
    
    try:
        num2 = int(sys.argv[2])
    except:
        sys.exit("arg2 %s is not an interger." % (sys.argv[2]))
    print("result: %d" % (num1 - num2))

if __name__ == '__main__':
    main()