type Time = i64;
type BusId = i64;
type Answer = Time;
type Schedule = Vec<BusId>;

pub const ANY: BusId = -1;

pub fn part1(mut input: Schedule) -> Answer {
    let minutes = input.remove(0);
    let mut time = minutes;

    loop {
        for &bus_id in input.iter() {
            if bus_id == ANY {
                continue;
            }

            if get_bus_depart_time_from(time, bus_id) == time {
                return (time - minutes) * bus_id;
            }
        }
        time += 1;
    }
}

pub fn part2(mut input: Schedule, is_test: bool) -> Answer {
    let mut time: Time = if is_test { 1 } else { 100000000000000 };
    input.remove(0); // don't need part1 minutes

    loop {
        // first bus comes next when?
        let bus0 = input[0];
        time = get_bus_depart_time_next(time, bus0);

        if buses_depart_sequentially(time, &input, time + bus0 + 1) {
            return time;
        }
    }
}

fn get_bus_depart_time_next(t: Time, bus_id: BusId) -> Time {
    // int division rounds down
    return t / bus_id * bus_id + bus_id;
}

fn get_bus_depart_time_from(t: Time, bus_id: BusId) -> Time {
    return if t % bus_id == 0 {
        // current time is a departure
        t
    } else {
        t / bus_id * bus_id + bus_id
    };
}

fn buses_depart_sequentially(bt: Time, sched: &Schedule, mut time_max: Time) -> bool {
    let mut time_min = bt;

    for (i, &bus_id) in sched.iter().enumerate() {
        if i == 0 || bus_id == ANY {
            continue;
        }

        // departure time
        let dep = get_bus_depart_time_from(time_min, bus_id);

        // minute we want the departure time to be at
        let target_minute = bt + i as Time; // unsafe.. w/e

        // bus comes at the right time?
        if dep != target_minute || dep <= time_min || dep >= time_max {
            return false;
        }

        // adjust constraints
        time_min = dep;
        let next = get_bus_depart_time_next(time_min, bus_id);
        if next < time_max {
            time_max = next
        }

        // println!(
        // "i: {}, bid: {}, dep: {}, min: {}, max: {}",
        // i, bus_id, dep, time_min, time_max
        // );
    }

    return true;
}

#[cfg(test)]
mod tests {
    use crate::part1;
    use crate::part2;
    use crate::Answer;
    use crate::ANY;

    #[test]
    fn test_part1() {
        const PART1_TEST_ANSWER: Answer = 295;
        assert_eq!(part1(vec![939, 7, 13, 59, 31, 19]), PART1_TEST_ANSWER);
    }

    #[test]
    fn test_part2() {
        assert_eq!(
            part2(vec![939, 7, 13, ANY, ANY, 59, ANY, 31, 19], true),
            1068781
        );
        assert_eq!(part2(vec![939, 67, 7, 59, 61], true), 754018);
        assert_eq!(part2(vec![939, 67, ANY, 7, 59, 61], true), 779210);
        assert_eq!(part2(vec![939, 67, 7, ANY, 59, 61], true), 1261476);
        assert_eq!(part2(vec![939, 1789, 37, 47, 1889], true), 1202161486);
    }
}
