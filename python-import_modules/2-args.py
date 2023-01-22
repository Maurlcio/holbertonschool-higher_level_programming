#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def argvcount(argv):
        arg = len(argv) - 1
        if arg == 0:
            print("0 arguments.")
        elif arg == 1:
            print("1 argument:")
            print("1: {}".format(argv[1]))
        elif arg > 1:
            print("{} arguments:".format(arg))
            for i in range(1, arg + 1):
                print("{}: {}".format(i, argv[i]))
    argvcount(sys.argv)
