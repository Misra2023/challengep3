
def convert_to_24(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    return "{:02d}{:02d}".format(hour, minute)
