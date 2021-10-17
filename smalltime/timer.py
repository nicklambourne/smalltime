import functools
import sys
import time

from typing import Callable, Optional, TextIO

import colors
import shortuuid


class SmallTimer:
    def __init__(self, name: Optional[str] = None, target: TextIO = sys.stdout):
        self.name = name if name else shortuuid.uuid()[:8]
        self.stored_time = None
        self.target = target

    def start(self) -> "SmallTimer":
        print(
            colors.color(f"Starting counter ({self.name})", fg="white", bg="red"),
            file=self.target,
        )
        self.stored_time = time.perf_counter_ns()
        return self

    def stop(self) -> int:
        if not self.stored_time:
            raise RuntimeError("Timers must be started before they can be stopped.")
        time_delta_ns = time.perf_counter_ns() - self.stored_time
        print(
            colors.color(
                f"Counter stopped ({self.name}): {time_delta_ns}ns elapsed",
                fg="white",
                bg="red",
            ),
            file=self.target,
        )
        self.stored_time = None
        return time_delta_ns


def timed(name: Optional[str] = None, target: Optional[str] = None):
    def decorator_timed(func: Callable):
        @functools.wraps(func)
        def wrapper_timed(*args, **kwargs):
            timer = SmallTimer(
                name=name or func.__name__, target=target if target else sys.stdout
            )
            timer.start()
            func(*args, **kwargs)
            timer.stop()

        return wrapper_timed

    return decorator_timed
