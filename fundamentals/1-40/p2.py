def past(h, m, s):

    #h = 3 600 000 ms
    #m = 60 000 ms
    #s = 1000 ms

    hours_ms = h * 3600000
    minutes_ms = m * 60000
    seconds_ms = s * 1000

    sum = hours_ms + minutes_ms + seconds_ms

    return sum