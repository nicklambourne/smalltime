import subprocess
import sys

import smalltime


def main() -> None:
    timer = smalltime.SmallTimer()
    timer.start()
    subprocess.call(sys.argv)
    timer.stop()
