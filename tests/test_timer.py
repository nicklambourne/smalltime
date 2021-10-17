import re

import _pytest.capture

import smalltime

WHITE_ON_RED = "\x1b[37;41m"
CLEAR_STYLES = r"\x1b\[0m\n"


class TestTimer:
    def test_smoke(self) -> None:
        assert smalltime.timer

    def test_timer_basic(self, capsys: _pytest.capture.CaptureFixture) -> None:
        timer = smalltime.SmallTimer(name="basic")
        timer.start()
        print("Hello")
        timer.stop()
        captured = capsys.readouterr()
        assert captured.out.startswith(f"{WHITE_ON_RED}Starting counter (basic)")
        assert re.search(fr"\d+ns elapsed{CLEAR_STYLES}$", captured.out)

    def test_nested(self, capsys: _pytest.capture.CaptureFixture) -> None:
        first_timer = smalltime.Timer()
        second_timer = smalltime.Timer()
        first_timer.start()
        second_timer.start()
        print("Hello, ", end="")
        second_timer.stop()
        print("World!")
        first_timer.stop()
        captured = capsys.readouterr()
        first_timer_matches = list(
            re.finditer(fr"\(({first_timer.name})\)", captured.out)
        )
        second_timer_matches = list(
            re.finditer(fr"\(({second_timer.name})\)", captured.out)
        )
        assert len(first_timer_matches) == 2 and len(second_timer_matches) == 2
        assert (
            first_timer_matches[0].start()
            < second_timer_matches[0].start()
            < second_timer_matches[1].start()
            < first_timer_matches[1].start()
        )

    def test_timed_decorator(self, capsys: _pytest.capture.CaptureFixture) -> None:
        @smalltime.timed()
        def example_timed_function() -> None:
            print("World")

        example_timed_function()
        captured = capsys.readouterr()
        assert captured.out.startswith(
            f"{WHITE_ON_RED}Starting counter (example_timed_function)"
        )
        assert re.search(fr"\d+ns elapsed{CLEAR_STYLES}$", captured.out)
