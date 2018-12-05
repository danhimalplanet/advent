import operator
from dataclasses import dataclass
from datetime import datetime
from collections import Counter, defaultdict


@dataclass
class Event:
    dt: datetime
    detail: str
    guard_id: int = None


def main() -> None:

    result_a = None
    result_b = None

    with open("data.txt", "r") as f:
        input_data = [s.strip() for s in f.readlines()]

        guards = defaultdict(Counter)
        events = []
        current_guard_id = None

        for i in input_data:
            _dt, detail = i.split("] ")
            dt = datetime.strptime(_dt.replace("[", ""), "%Y-%m-%d %H:%M")
            guard_id = (
                int(detail.split()[1].replace("#", "")) if "Guard" in detail else None
            )
            event = Event(dt=dt, detail=detail, guard_id=guard_id)
            events.append(event)

        events.sort(key=operator.attrgetter("dt"), reverse=False)

        for event in events:
            if event.guard_id is not None:
                current_guard_id = event.guard_id
            elif "falls asleep" in event.detail:
                start_time = event.dt
            elif "wakes up" in event.detail:
                guards[current_guard_id].update(
                    range(start_time.minute, event.dt.minute)
                )

        guard_id, counter = max(guards.items(), key=lambda k: sum(k[1].values()))
        sleep_minute = counter.most_common()[0][0]
        result_a = guard_id * sleep_minute

    guard_sleep_minutes = []
    for guard_id, counter in guards.items():
        guard_sleep_minutes.append([guard_id, counter.most_common()[0]])

    guard_id, (minute, _) = max(guard_sleep_minutes, key=lambda k: k[1][1])

    result_b = guard_id * minute

    print(f"Part A: {result_a}")
    print(f"Part B: {result_b}")


if __name__ == "__main__":
    main()
