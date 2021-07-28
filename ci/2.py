# given a time T in 24-hour format (hh:mm) and a positive integer K, you have to tell the time after K minutes in 24-hour time
def time_after(time, k):
    hh, mm = time.split(':')
    hh = int(hh)
    mm = int(mm)
    hh += k // 60
    mm += k % 60
    if mm >= 60:
        hh += mm // 60
        mm = mm % 60
    if hh >= 24:
        hh -= 24
    return '{:02d}:{:02d}'.format(hh, mm)


print(time_after('00:00', 600))
