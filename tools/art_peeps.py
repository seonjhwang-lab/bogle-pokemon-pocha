"""peeps — 16x24 포켓몬 손님 5종(꼬부기·이브이·고라파덕·님피아·잠만보) + 로켓단 나옹.

Each pokemon: walk(4) idle(2) eat(2) angry(2). Cat(Meowth): walk(4) idle(2) steal(2) flee(2).
"""
from pixel import Canvas

W, H = 16, 24

BASE = {
    '.': None, 'K': 'black', 's': 'skin', 'S': 'skin_dk', 'e': 'black', 'm': 'brown_dk',
    'h': 'plum_dk', 'W': 'white', 'g': 'gray_lt', 'R': 'red', 'r': 'red_dk',
}

# ---------------------------------------------------------------- kid = 꼬부기 (Squirtle)
KID_UP = [  # rows 7..20
    ".....KKKKKK.....",
    "....KCCCCCCK....",
    "...KCCCCCCCCK...",
    "...KCCBBBBCCK...",
    "...KCWCCCCWCK...",
    "...KCeCCCCeCK...",
    "...KCCpmmpCCK...",
    "....KBBBBBBK....",
    "..KBCYYYYYYCBK..",
    "..KBCYyYYyYCBK..",
    "..KBBYYYYYYBBK..",
    "...KTyYYYYyTK...",
    "...KTTTTTTTTK...",
    "...KTTKKKKTTK...",
]
KID = dict(up=KID_UP, top=7, leg_top=21, legs_x=(4, 10),
           leg_rows=['cyan', 'cyan', 'blue'], eye_row=12, eyes=(5, 10), mouth_row=13,
           legend={**BASE, 'C': 'cyan', 'B': 'blue', 'Y': 'yellow', 'y': 'tan', 'T': 'brown', 'p': 'pink'},
           bowl_row=18, face_col='cyan')

# ---------------------------------------------------------------- girl = 이브이 (Eevee)
GIRL_UP = [  # rows 5..18
    "..KKK......KKK..",
    ".KTKTT....TTKTK.",
    ".KTTbKKKKKKbTTK.",
    "..KTTTTTTTTTTK..",
    "...KTTTTTTTTK...",
    "...KTWTTTWTtK...",
    "...KTeTTTetTK...",
    "...KTTpmmpTTK...",
    "..KCCCCCCCCCCK..",
    ".KCCCCCCCCCCCCK.",
    "..KCCCCCCCCCCK..",
    "..KTTTTTTTTTTK..",
    "...KTtTTTTtTK...",
    "...KTTtTTtTTK...",
]
GIRL = dict(up=GIRL_UP, top=5, leg_top=19, legs_x=(5, 9),
            leg_rows=['tan', 'tan', 'brown', 'brown', 'brown_dk'], eye_row=11, eyes=(5, 9), mouth_row=12,
            legend={**BASE, 'T': 'tan', 't': 'brown', 'b': 'brown_dk', 'C': 'cream', 'p': 'pink'},
            bowl_row=16, face_col='tan')

# ---------------------------------------------------------------- teacher = 고라파덕 (Psyduck)
TEACH_UP = [  # rows 3..16
    "......KKKK......",
    "....KKYYYYKK....",
    "...KYYYYYYYYK...",
    "...KYYYYYYYYK...",
    "..KYYWWYYWWYYK..",
    "..KYYWeYYeWYYK..",
    "..KYYCCCCCCYYK..",
    "..KYYCmmmmCYYK..",
    "...KYYCCCCYYK...",
    "..KYYYYYYYYYYK..",
    ".KYYYYYYYYYYYYK.",
    ".KYYYYyYYyYYYYK.",
    "..KYYYYYYYYYYK..",
    "...KyyyyyyyyK...",
]
TEACH = dict(up=TEACH_UP, top=3, leg_top=17, legs_x=(4, 9), leg_w=3,
             leg_rows=['Y', 'Y', 'Y', 'Y', 'Y', 'cream', 'tan'], eye_row=8, eyes=(6, 9), mouth_row=10,
             legend={**BASE, 'Y': 'yellow', 'y': 'gold', 'C': 'cream'},
             bowl_row=15, face_col='yellow')

# ---------------------------------------------------------------- hsgirl = 님피아 (Sylveon)
HS_UP = [  # rows 4..17
    "..KKK......KKK..",
    ".KPKBP....PBKPK.",
    ".KPPPKKKKKKPPPK.",
    "..KWRRPPPPPPPK..",
    "...KPPPPPPPPK...",
    "...KCCCCCCCCK...",
    "...KCeCCCCeCK...",
    "...KCCpmmpCCK...",
    "..KWWWRRRRWWWK..",
    "..KCCBWWWWBCCK..",
    "..KCCCCCCCCCCK..",
    "..KCCCCCCCCCCK..",
    "...KCCCCCCCCK...",
    "...KPPCCCCPPK...",
]
HSGIRL = dict(up=HS_UP, top=4, leg_top=18, legs_x=(5, 9),
              leg_rows=['cream', 'cream', 'pink', 'pink', 'pink_hot'], eye_row=10, eyes=(5, 10), mouth_row=11,
              legend={**BASE, 'P': 'pink', 'B': 'blue', 'C': 'cream', 'p': 'pink_hot', 'R': 'pink_hot'},
              bowl_row=15, face_col='cream')

# ---------------------------------------------------------------- judo = 잠만보 (Snorlax)
JUDO_UP = [  # rows 3..16
    "..KKK......KKK..",
    ".KTTKKKKKKKKTTK.",
    ".KTTTCCCCCCCTTK.",
    "..KCCCCCCCCCCK..",
    "..KCeeCCCCeeCK..",
    "..KCCCCCCCCCCK..",
    "..KCCCmmmmCCCK..",
    ".KTTTTCCCCCTKTK.",
    ".KTTCCCCCCCCCTK.",
    ".KTCCCCCCCCCCCK.",
    ".KTCCCCCCCCCCCK.",
    "..KTCCCCCCCCCTK.",
    "..KTTCCCCCCCTTK.",
    "..KTTTTTTTTTTK..",
]
JUDO = dict(up=JUDO_UP, top=3, leg_top=17, legs_x=(4, 9), leg_w=3,
            leg_rows=['teal_dk', 'teal_dk', 'teal_dk', 'teal_dk', 'cream', 'cream', 'tan'], eye_row=7, eyes=(5, 10), mouth_row=9,
            legend={**BASE, 'T': 'teal_dk', 'C': 'cream'}, bowl_row=15, face_col='cream')

HEART = ["RR.RR", "RWRRR", ".RRR.", "..R.."]
ANGER = [".R.R.", "RR.RR", ".....", "RR.RR", ".R.R."]


def _check(rows):
    for r in rows:
        assert len(r) == 16, (len(r), r)


for spec in (KID, GIRL, TEACH, HSGIRL, JUDO):
    _check(spec['up'])


def legs(c: Canvas, spec, lift_l=0, lift_r=0):
    rows = spec['leg_rows']
    top = spec['leg_top']
    leg_color = {'T': 'teal_dk', 'Y': 'yellow'}
    for side, (x, lift) in enumerate(zip(spec['legs_x'], (lift_l, lift_r))):
        for j, col in enumerate(rows):
            y = top + j - lift
            col = leg_color.get(col, col)
            lw = spec.get('leg_w', 2)
            for dx in range(lw):
                c.px(x + dx, y, col)
            c.px(x - 1, y, 'black'); c.px(x + lw, y, 'black')
        # 발 앞코
        c.px(x - 1 if side == 0 else x + lw, top + len(rows) - 1 - lift, leg_color.get(rows[-1], rows[-1]))


def human(spec, pose: str, k: int) -> Canvas:
    c = Canvas(W, H)
    body = Canvas(W, H)
    body.grid(0, spec['top'], spec['up'], spec['legend'])
    lift_l = lift_r = 0
    bob = 0
    if pose == 'walk':
        lift_l, lift_r = [(1, 0), (0, 0), (0, 1), (0, 0)][k]
        bob = -1 if k in (0, 2) else 0
    elif pose == 'idle':
        bob = k
    elif pose == 'eat':
        bob = k
    elif pose == 'angry':
        lift_l, lift_r = [(1, 0), (0, 1)][k]

    ey, (ex1, ex2), my = spec['eye_row'], spec['eyes'], spec['mouth_row']
    fc = spec.get('face_col', 'skin')
    if pose == 'eat':
        # 행복한 눈(^^) + 볼터치 + 그릇
        for ex in (ex1, ex2):
            body.px(ex, ey, fc); body.px(ex, ey - 1 if spec is not TEACH else ey, 'black')
        body.px(ex1 - 1, ey + 1, 'pink'); body.px(ex2 + 1, ey + 1, 'pink')
        body.px(7, my, 'red_dk' if k == 0 else 'brown_dk'); body.px(8, my, 'red_dk' if k == 0 else fc)
        br = spec['bowl_row']
        body.hline(5, 10, br, 'red'); body.hline(6, 9, br + 1, 'red_dk')
        body.hline(6, 9, br - 1, 'cream')
        body.line(9, br - 4, 11, br - 1, 'tan')
        if k == 0:
            body.px(7, br - 3, 'white')
    if pose == 'angry':
        if spec is not TEACH:
            body.px(ex1 + 1, ey - 1, 'black'); body.px(ex2 - 1, ey - 1, 'black')
        body.px(ex1 - 1, ey + 1, 'pink'); body.px(ex2 + 1, ey + 1, 'pink')
        body.px(7, my, 'black'); body.px(8, my, 'black')
        if spec is TEACH:
            body.px(6, my, 'black'); body.px(9, my, 'black')
    legs(c, spec, lift_l, lift_r)
    c.paste(body.shifted(0, bob))

    if pose == 'eat':
        hy = 0 if k == 1 else 1
        c.grid(10, hy, HEART, {'R': 'pink_hot', 'W': 'white'})
    if pose == 'angry':
        c.grid(11, k, ANGER, {'R': 'red'})
        if k == 1:
            c.px(3, spec['top'] - 1, 'gray_lt'); c.px(2, spec['top'] - 2, 'white')
    return c


# ---------------------------------------------------------------- cat = 로켓단 나옹 (Meowth)
CAT_HEAD = [
    ".KK..KK.",
    ".KbYYbK.",
    "KccYYccK",
    "KcKccKcK",
    "KcccpcCK",
    ".KccccK.",
]
CAT_LEG = {'c': 'cream', 'C': 'tan', 'b': 'brown_dk', 'Y': 'gold', 'p': 'pink', 'K': 'black'}


def cat(pose: str, k: int) -> Canvas:
    c = Canvas(W, H)
    arched = pose == 'flee'
    by = 17 if not arched else 15   # 몸통 윗줄
    hx, hy = 0, 13
    # 나옹 몸통 (크림색 + 갈색 발/꼬리 끝)
    for y in range(by, by + 4):
        for x in range(3, 14):
            col = 'cream'
            if y == by + 3 and 4 <= x <= 11:
                col = 'tan'
            c.px(x, y, col)
    if arched:
        c.hline(5, 11, by - 1, 'cream'); c.hline(7, 9, by - 2, 'cream')
    # 다리 (갈색 발끝)
    leg_y0 = by + 4
    poses = {
        'walk': [((4, 0), (6, 1), (10, 1), (12, 0)), ((4, 1), (6, 0), (10, 0), (12, 1)),
                 ((4, 0), (6, 1), (10, 1), (12, 0)), ((4, 1), (6, 0), (10, 0), (12, 1))],
    }
    leg_set = poses['walk'][k] if pose == 'walk' else ((4, 0), (6, 0), (10, 0), (12, 0))
    for (lx, lift) in leg_set:
        for y in range(leg_y0, 23 - lift):
            c.px(lx, y, 'cream')
        c.px(lx, 23 - lift, 'brown_dk')
    # 말린 꼬리 (끝부분 갈색)
    sway = [0, 1][k % 2] if pose in ('idle', 'walk') else 0
    if arched:
        c.vline(14, by - 5, by + 1, 'cream'); c.px(14, by - 6, 'brown_dk'); c.px(15, by - 6, 'brown')
        c.px(13, by - 5, 'brown'); c.px(15, by - 4, 'brown')
    else:
        c.px(14, by + 1, 'cream'); c.px(14, by, 'cream')
        c.vline(15 - sway, by - 4, by - 1, 'cream')
        c.px(15 - sway, by - 5, 'brown_dk'); c.px(14 - sway, by - 5, 'brown')
    # 머리 (이마에 금화 부적)
    hy = by - 4 - (1 if arched else 0)
    c.grid(hx, hy, CAT_HEAD, CAT_LEG)
    c.px(3, hy + 1, 'yellow')  # 금화 하이라이트
    if pose == 'steal':
        # 입에 문 오랭열매/보따리 + 반짝이
        fy = hy + 5
        c.hline(0, 2, fy, 'blue'); c.px(1, fy - 1, 'cyan'); c.px(1, fy + 1, 'blue_dk')
        c.px(4 + k, hy - 2, 'yellow'); c.px(4 + k, hy - 4, 'yellow')
    if pose == 'flee':
        # 쉭! 화들짝 - 눈 땡그랗게, 입 벌림, 느낌표
        c.px(2, hy + 3, 'yellow'); c.px(5, hy + 3, 'yellow')
        c.px(3, hy + 4, 'red_dk'); c.px(4, hy + 4, 'red_dk')
        ex = 7 + k
        c.vline(ex, 0 + k, 3 + k, 'red'); c.px(ex, 5 + k, 'red')
    out = c.copy()
    sil = Canvas(W, H)
    sil.paste(c)
    sil.outline('black')
    final = Canvas(W, H)
    final.paste(sil)
    final.paste(out)
    return final


def frames():
    out = []
    for key, spec in (('kid', KID), ('girl', GIRL), ('teacher', TEACH), ('hsgirl', HSGIRL), ('judo', JUDO)):
        out.append((f'{key}_walk', [human(spec, 'walk', k) for k in range(4)], 140))
        out.append((f'{key}_idle', [human(spec, 'idle', k) for k in range(2)], 450))
        out.append((f'{key}_eat', [human(spec, 'eat', k) for k in range(2)], 220))
        out.append((f'{key}_angry', [human(spec, 'angry', k) for k in range(2)], 160))
    out.append(('cat_walk', [cat('walk', k) for k in range(4)], 110))
    out.append(('cat_idle', [cat('idle', k) for k in range(2)], 400))
    out.append(('cat_steal', [cat('steal', k) for k in range(2)], 180))
    out.append(('cat_flee', [cat('flee', k) for k in range(2)], 100))
    return out
