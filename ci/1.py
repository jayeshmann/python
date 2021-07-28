# convert time from 12 to 24
def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == '12':
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]


print(timeConversion('04:00:00PM'))
