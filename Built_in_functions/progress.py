def progress(percent=0, width=30):
    end = "" if percent < 100 else "\n"
    left = width * percent // 100
    right = width - left
    print(
        "\r[",
        "#"*left,
        " "*right,
        "]",
        f'{percent:.0f}%',
        sep="",
        end=end,
        flush=True
    )

from time import sleep
from progress import progress
for percent in range(101):
    sleep(0.2)
    progress(percent)