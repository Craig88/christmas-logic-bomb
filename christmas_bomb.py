from datetime import date

today = date.today()
target = date(today.year, 12, 25)


def show_message():
    theTree = [0, 0, 1, 1, 3, 5, 7, 9, 13, 7,
              11, 15, 19, 11, 15, 19, 11, 15,
              19, 23, 27, 6, 6, 6, 0]

    for row in theTree:
        gap_size = int((14 - (0.5 * (row + 1))))
        print(" " * gap_size + "*" * row)
    print(">>>>> MERRY CHRISTMAS <<<<<")
    print(" ")
    exit()


def bomb():
    if (today == target):
        show_message()


print("Running program as normal...")
bomb()
print("Nothing to see here...")
