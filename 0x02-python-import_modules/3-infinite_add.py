#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    if (argc == 1):
        print("0")
    else:
        sum = 0
        for i in range(1, argc):
            sum += int(argv[i])
        print("{}".format(sum))
