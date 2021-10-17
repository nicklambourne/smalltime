import subprocess
import sys

import smalltime


class UsageError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def main() -> None:
    if not len(sys.argv) > 1:
        raise UsageError(
            "You must provide the name (and optionally arguments of a program to time.)"
        )
    timer = smalltime.Timer()
    timer.start()
    subprocess.call(sys.argv[1:])
    timer.stop()
