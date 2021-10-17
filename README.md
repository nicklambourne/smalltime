# smalltime

<p align="center">
    <img src="https://github.com/nicklambourne/smalltime/raw/master/docs/img/smalltime.png" width="250px"/>
</p>

## What is it?

## Requirements
`smalltime` requires Python >= 3.6.2.

See [`pyproject.toml`](https://github.com/nicklambourne/smalltime/blob/master/pyproject.toml) for dependencies and dev dependencies.

## Installation

Via [`poetry`](https://python-poetry.org/):
```bash
poetry add smalltime
```

Via `pip`:
```bash
pip install smalltime
```

## Basic Usage
### In Python Code
#### In-Line
```python
import smalltime

timer = smalltime.Timer(name="hello world timer")
timer.start()
print("Hello, ", end="")
print("World!")
timer.stop()
```

#### Via Decorator
```python
import smalltime
import subprocess

@smalltime.timed(name="thing_timer")
def thing_you_want_to_time():
    subprocess.call(["python", "-c", "\"import this\""])


thing_you_want_to_time()
```

### From the Command Line
N.B.: Assumes installation via Poetry and an active [Poetry shell](https://python-poetry.org/docs/cli/#shell).
```bash
# Usage: st <program> [args]
st sleep 10
Starting counter (BNM8rBqP)
Counter stopped (BNM8rBqP): 10007777130ns elapsed
```