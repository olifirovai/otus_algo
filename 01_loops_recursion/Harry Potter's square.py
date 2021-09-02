import os
from math import sin  # noqa

os.system('cls')


# picture1 = x < y
# picture2 = x == y
# picture3 = 24 - x == y
# picture4 = x < 29 - y
# picture5 =
# picture6 = x < 10 or y < 10
# picture7 = x > 15 and y > 15
# picture8 = x < 1 or y < 1
# picture9 = x < y - 10 or x > y + 10
# picture10 =
# picture11 =
# picture12 =
# picture13 = x >= 20 - y and x < 29 - y
# picture14 = (1 / (2 * x + 1) * 50) * 2 > y-6 - где-то рядом
# picture15 =
# picture16 =
# picture17 = round(7.5 * sin(y / 3 + 6.2), 0) <= x - 17 - очень близко
# picture18 =
# picture19 = (x % 24) * (y % 24) == 0
# picture20 =
# picture21 =
# picture22 =
# picture23 =
# picture24 = 24 - x == y or x == y
# picture25 = (x % 6) * (y % 6) == 0

# Полученные рисунки можно посмотреть в папке my_results
def harry_magic():
    line = ''
    for x in range(25):
        for y in range(25):
            if (x % 24) * (y % 24) == 0:
                line += '# '
            else:
                line += '. '
        print(line)
        line = ''


if __name__ == '__main__':
    harry_magic()
