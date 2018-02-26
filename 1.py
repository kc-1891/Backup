def minutes_to_hours(mins, secs=0):
    hours = mins / 60 + secs / 3600
    return hours

print(minutes_to_hours(70))