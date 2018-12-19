
import sys
from ShowObject import *


def main():
    if len(sys.argv) == 1:
        print("Usage: python EpGen.py NameOfShow")
        exit()
    Show(" ".join(sys.argv[1:])).printRandomEpisode()

if __name__ == "__main__":
    main()
