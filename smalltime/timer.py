import functools
import sys
import time

from typing import Optional, TextIO

import ansicolors
import shortuuid


class SmallTimer:
    def __init__(self, name: Optional[str] = None, target: TextIO = sys.stdout):
        self.name = name if name else shortuuid.uuid()[:8]
        self.stored_time = None
        self.target = target

    def start(self) -> "SmallTimer":
        print(ansicolors.color(f"Starting counter ({self.name})", fg="white", bg="red"))
        self.stored_time = time.perf_counter_ns()
        return self

    def stop(self) -> int:
        if not self.stored_time:
            raise RuntimeError("Timers must be started before they can be stopped.")
        time_delta_ns = self.stored_time - time.perf_counter_ns()
        print(ansicolors.color(f"Counter stopped ({self.name}): {time_delta_ns}ns elapsed", fg="white", bg="red"))
        self.stored_time = None
        return time_delta_ns


def timed(timer_id: str):
    def decorator_timed(func):
        @functools.wraps(func)
        def wrapper_timed(*args, **kwargs):
            timer = SmallTimer(name=timer_id)
            timer.start()
            func(*args, **kwargs)
            timer.stop()
        return wrapper_timed
    return decorator_timed


