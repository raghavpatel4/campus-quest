import time
import sys


def loading_text():
    for _ in range(4):
        time.sleep(1)  # 1-second delay for each ellipsis
        print("... ")

    sys.stdout.write("\n")  # Move to the next line after the loading is done
