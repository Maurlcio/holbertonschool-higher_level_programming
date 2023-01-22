#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    def whomst():
        for i in dir(hidden_4):
            if i[:2] == "__":
                pass
            else:
                print(i)
    whomst()
