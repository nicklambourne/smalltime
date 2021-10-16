import re

import _pytest.capture

import smalltime


class TestSmallTime:
    def test_smoke(self) -> None:
        assert smalltime.timer

    def test_timer_basic(self, capsys: _pytest.capture.CaptureFixture) -> None:
        timer = smalltime.SmallTimer(name="basic")
        timer.start()
        print("Hello")
        timer.stop()
        captured = capsys.readouterr()
        assert captured.out.startswith("Starting counter (basic)")
        assert re.search(r'\d+$', captured.out)

    def test_timer_cli(self) -> None:
        pass