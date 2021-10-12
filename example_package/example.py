import time
from typing import Any


def example_runner(arg: str):
    print(f"example_runner called with {arg}")
    time.sleep(0.1)
    return "hello " + arg


def join_strings(*args: Any, **_kwargs: Any) -> str:
    return ", ".join(args)
