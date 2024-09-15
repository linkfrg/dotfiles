#!/usr/bin/env python3

import sys
from ignis.client import IgnisClient

CODE_TEMPLATE = """
from ignis.services.recorder import RecorderService

recorder = RecorderService.get_default()
recorder.{}_recording()
"""


def run_code(_type: str) -> None:
    client = IgnisClient()
    client.run_python(CODE_TEMPLATE.format(_type))


if len(sys.argv) < 2:
    sys.exit(1)

elif sys.argv[1] == "start":
    run_code("start")

elif sys.argv[1] == "stop":
    run_code("stop")

elif sys.argv[1] == "pause":
    run_code("pause")

elif sys.argv[1] == "continue":
    run_code("continue")
