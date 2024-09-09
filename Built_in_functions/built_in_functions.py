def hh_mm_ss(miliseconds):
    seconds = round(miliseconds / 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(hh_mm_ss(10000))
print(hh_mm_ss(68000))
print(hh_mm_ss(3680000))
