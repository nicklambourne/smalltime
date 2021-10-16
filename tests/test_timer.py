import re

import _pytest.capture

import smalltime


class TestTimer:
    def test_smoke(self) -> None:
        assert smalltime.timer

    def test_timer_basic(self, capsys: _pytest.capture.CaptureFixture) -> None:
        timer = smalltime.SmallTimer(name="basic")
        timer.start()
        print("Hello")
        timer.stop()
        captured = capsys.readouterr()
        assert captured.out.startswith("\x1b[37;41mStarting counter (basic)")
        assert re.search(r"\d+ns elapsed\x1b\[0m\n$", captured.out)

    def test_timer_cli(self, capsys: _pytest.capture.CaptureFixture) -> None:
        @smalltime.timed()
        def example_timed_function() -> None:
            print("World")

        example_timed_function()
        captured = capsys.readouterr()
        assert captured.out.startswith("\x1b[37;41mStarting counter (example_timed_function)")
        assert re.search(r"\d+ns elapsed\x1b\[0m\n$", captured.out)
