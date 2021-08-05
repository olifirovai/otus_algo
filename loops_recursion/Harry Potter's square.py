import os
from math import sin

os.system('cls')


# picture1 = x<y
# picture2 = x==y
# picture3 = 24-x==y
# picture4 = x<30-y !!???
# picture5 =
# picture6 =
# picture7 =
# picture8 =
# picture9 = x<y-10 or x>y+10
# picture10 =
# picture11 =
# picture12 =
# picture13 =
# picture14 =(1/(2*x+1)*50)*2>y - не готова, близко
# picture15 =
# picture16 =
# picture17 = round(7.5*sin(y/3+6.2),0) <= x-17 - очень близко
# picture18 =
# picture19 = (x%24)*(y%24)==0
# picture20 =
# picture21 =
# picture22 =
# picture23 =
# picture24 = 24-x==y or x==y
# picture25 = (x%6)*(y%6)==0

def harry_magic():
    line = ''
    for x in range(25):
        for y in range(25):
            # x < y - 10 or x > y + 10
            if round(7.5 * sin(y / 3 + 6.2), 0) <= x - 17:
                line += '# '
            else:
                line += '. '
        print(line)
        line = ''


if __name__ == '__main__':
    harry_magic()
