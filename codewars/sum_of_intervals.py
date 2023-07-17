def sum_of_intervals(intervals):
    intervals.sort()

    start = intervals[0][0]
    end = intervals[0][1]
    interval_sum = 0

    for interval in intervals[1:]:
        if interval[0] <= end:
            if interval[1] > end:
                end = interval[1]
        else:
            interval_sum += end - start
            start = interval[0]
            end = interval[1]

    interval_sum += end - start

    return interval_sum


if __name__ == '__main__':
    print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))
