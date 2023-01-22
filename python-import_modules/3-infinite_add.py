#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def infsum(argv):
        arg = len(argv) - 1

        if arg == 0:
            print("0")
        if arg == 1:
            print("{}".format(int(argv[1])))
        if arg >= 2:
            add = 0
            for i in range(1, arg + 1):
                add += int(argv[i])
            print("{}".format(add))

    infsum(sys.argv)


