def add_time(start, duration, day=""):

    days_of_week = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    days_of_week_arr = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]

    dt = duration.partition(":")
    dh = int(dt[0])
    dm = int(dt[2])

    st = start.partition(":")
    smt = st[2].partition(" ")
    sh = int(st[0])
    sm = int(smt[0])
    amopm = smt[2]
    amapmf = {"AM": "PM", "PM": "AM"}

    amountd = int(dh / 24)

    em = sm + dm
    if (em >= 60):
        sh = sh + 1
        em = em % 60
    amountampmf = int((sh + dh) / 12)
    eh = (sh + dh) % 12

    em = em if em > 9 else "0" + str(em)
    eh = eh = 12 if eh == 0 else eh
    if (amopm == "PM" and sh + (dh % 12) >= 12):
        amountd += 1

    amopm = amapmf[amopm] if amountampmf % 2 == 1 else amopm

    rtime =  str(eh) + ":" + str(em) + " " + amopm 
    if (day):
        day = day.lower()
        index = int((days_of_week[day]) + amountd) % 7
        nday = days_of_week_arr[index]
        rtime = rtime + ", " + nday

    if (amountd == 1):
        return rtime  + " " + "(next day)"
    elif (amountd > 1):
        return rtime + " (" + str(amountd) + " days later)"

    return rtime
