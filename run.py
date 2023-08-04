import os
import sys

from main import main

__DIR__ = os.path.dirname(os.path.abspath(__file__))


def run():
    arg = sys.argv[1:]
    if len(arg) != 2:
        print("Missing arguments!")
        exit()

    file_name = os.path.join(__DIR__, "txns.csv")
    arg.append(file_name)

    main(*arg)


if __name__ == "__main__":
    run()
