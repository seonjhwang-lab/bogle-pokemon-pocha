"""ui_mini — 8x8 주문 카드용 미니 아이콘 (포켓몬 열매 테마)."""
from pixel import Canvas

LEG = {'K': 'black', 'W': 'white', 'g': 'gray_lt', 'Y': 'yellow', 'y': 'gold', 'O': 'orange',
       'G': 'green', 'd': 'green_dk', 'R': 'red', 'r': 'red_dk', 'c': 'cream', 'B': 'blue',
       'b': 'blue_dk', 'C': 'cyan', 'P': 'pink_hot', 'p': 'pink'}

ICONS = {
    'mini_ramen': ["........", ".c.c.c..", "KKKKKKKK", "KRcRcRRK", ".KrrrrK.", "..KKKK..", "........", "........"],
    'mini_egg':   ["..GG....", ".KppKK..", "KWpppPK.", "KpppppPK", "KppppPPK", ".KPPPPK.", "..KKKK..", "........"],
    'mini_scallion': ["........", ".KK..KK.", "KBCK.KbK", ".KK.KK..", "...KBCK.", "KK..KK..", "bK......", "K......."],
    'mini_cheese': ["........", "..KKKKKK", ".KWYYYYK", ".KYYyYYK", "KYYYYYyK", "KyyyyyyK", "KKKKKKK.", "........"],
    'mini_slush': [".....G..", ".KKKKGK.", "KyyyyyyK", ".KyYyyK.", ".KyyyyK.", "..KyyK..", "..KKKK..", "........"],
    'mini_heart': ["........", ".PP.PP..", "PWPPPPP.", "PPPPPPP.", ".PPPPP..", "..PPP...", "...P....", "........"],
    'mini_perfect': ["...Y....", "...Y....", ".YYYYY..", "..YYY...", ".Y...Y..", "........", "........", "........"],
}


def frames():
    out = []
    for name, rows in ICONS.items():
        c = Canvas(8, 8)
        c.grid(0, 0, rows, LEG)
        out.append((name, [c], 1000))
    return out
