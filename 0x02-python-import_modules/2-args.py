#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 1):
        print("0 arguments.")
    else:
        if (len(sys.argv) == 2):
            msg = "argument:"
        else:
            msg = "arguments:"
        print("{} {}".format(len(sys.argv) - 1, msg))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
