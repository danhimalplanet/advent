import sys
import os
sys.path.append(os.path.abspath('.'))
import importlib
import json
from aoc import current_day


def advent_of_code(event, context):
    day = event['day'] if 'day' in event else current_day

    # import module for day
    day_mod = f"aoc.day{day}"
    module = importlib.import_module(day_mod)

    return {
        "result": run_day(day, module, event),
    }

def run_day(day, module, event):
    # invoke DayN.lambda_handler(event)
    # and return it
    day_class = getattr(module, f"Day{day}")
    today_lambda_func = getattr(day_class, "lambda_handler")
    return today_lambda_func(event)
