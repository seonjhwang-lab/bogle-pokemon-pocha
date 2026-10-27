"""props — 32x32 상점 소품 (6프레임 루프 애니메이션)

  arcade_*  피카츄 노란 미니 오락기: 귀 달린 노란 캐비닛, 빨간 볼 포인트, 화면 속 전기 슈팅 게임
  tv_*      로토무 주황 브라운관 TV: 머리 위 플라즈마 뿔, 양옆 번개 날개, 화면 속 포켓몬 방송
"""
from pixel import Canvas

W = H = 32

# ---------------------------------------------------------------- 피카츄 노란 오락기
LIGHTS = ['red', 'white', 'cyan', 'pink_hot', 'green']


def arcade(k: int) -> Canvas:
    c = Canvas(W, H)
    x0, x1 = 6, 25                     # 캐비닛 좌우 (폭 20)
    # 상단 피카츄 귀 장식 (검은 끝 + 노란 귀)
    c.rect(x0 + 1, 0, 3, 2, 'black'); c.rect(x0 + 1, 2, 3, 2, 'yellow')
    c.rect(x1 - 3, 0, 3, 2, 'black'); c.rect(x1 - 3, 2, 3, 2, 'yellow')
    # 노란 몸통 (피카츄 컬러)
    c.rect(x0, 9, 20, 22, 'gold')
    c.rect(x0, 9, 2, 22, 'yellow')
    c.rect(x1 - 1, 9, 2, 22, 'orange_dk')
    # 피카츄 빨간 전기 볼 장식 (캐비닛 양옆)
    c.rect(x0 + 1, 15, 2, 3, 'red' if k % 2 == 0 else 'pink_hot')
    c.rect(x1 - 2, 15, 2, 3, 'red' if k % 2 == 0 else 'pink_hot')
    # 마퀴 (상단 간판) + 순차 점멸 불빛
    c.rect(x0 - 1, 3, 22, 6, 'red')
    c.hline(x0 - 1, x1 + 1, 3, 'pink')
    c.hline(x0 - 1, x1 + 1, 8, 'red_dk')
    for i in range(5):
        on = (i == k % 5) or (k == 5)
        c.rect(x0 + 1 + i * 4, 5, 2, 2, LIGHTS[i] if on else 'brown_dk')
    # 화면 (검정 바탕 12x10)
    sx, sy = x0 + 4, 11
    c.rect(sx - 1, sy - 1, 14, 12, 'brown_dk')
    c.rect(sx, sy, 12, 10, 'black')
    # 별 배경 (아래로 흐름)
    for (bx, by) in ((1, 1), (8, 3), (4, 6), (10, 8)):
        c.px(sx + bx, sy + (by + k) % 10, 'gray_dk')
    # 적 (위쪽, 좌우로 흔들림) — 4프레임째에 번개 맞고 폭발
    ex = sx + 2 + [0, 2, 4, 6, 4, 2][k]
    if k in (3, 4):
        boom = ['yellow', 'cyan'][k - 3]
        c.px(ex, sy + 2, boom); c.px(ex + 1, sy + 1, boom); c.px(ex + 2, sy + 2, boom); c.px(ex + 1, sy + 3, boom)
        if k == 4:
            c.px(ex - 1, sy + 1, 'white'); c.px(ex + 3, sy + 3, 'white')
    else:
        c.px(ex, sy + 1, 'magenta'); c.px(ex + 2, sy + 1, 'magenta')
        c.hline(ex, ex + 2, sy + 2, 'pink'); c.px(ex + 1, sy + 3, 'pink')
    # 플레이어 미니 피카츄 (아래쪽, 좌우 이동)
    px = sx + [3, 5, 7, 7, 5, 3][k]
    c.px(px, sy + 7, 'yellow'); c.px(px + 2, sy + 7, 'yellow')
    c.hline(px, px + 2, sy + 8, 'yellow')
    c.px(px, sy + 9, 'red'); c.px(px + 1, sy + 9, 'gold'); c.px(px + 2, sy + 9, 'red')
    # 전기 총알 (위로)
    for j in range(2):
        by = sy + 6 - ((k * 2 + j * 3) % 6)
        if by > sy:
            c.px(px + 1, by, 'cyan' if j % 2 else 'yellow')
    # 화면 반사광
    c.px(sx, sy, 'slate'); c.px(sx + 1, sy, 'slate')
    # 조작부 (기울어진 판 — 피카츄 등 줄무늬 갈색)
    c.rect(x0, 22, 20, 4, 'brown')
    c.hline(x0, x1, 22, 'tan')
    c.vline(x0 + 5, 20, 22, 'black')
    c.rect(x0 + 4, 19, 3, 2, 'red' if k % 2 == 0 else 'red_dk')        # 몬스터볼 조이스틱
    c.rect(x0 + 11, 23, 2, 2, 'yellow' if k % 3 else 'white')          # 버튼
    c.rect(x0 + 15, 23, 2, 2, 'cyan' if k % 2 else 'blue')
    # 동전 투입구
    c.rect(x0 + 8, 27, 4, 3, 'brown_dk')
    c.vline(x0 + 10, 27, 29, 'black')
    c.px(x0 + 9, 29, 'red' if k % 2 else 'yellow')
    # 다리
    c.rect(x0 + 1, 31, 2, 1, 'black'); c.rect(x1 - 2, 31, 2, 1, 'black')
    c.outline('black')
    return c


# ---------------------------------------------------------------- 로토무 주황 브라운관 TV
SCREEN_BG = ['blue_dk', 'cyan', 'teal_dk', 'blue_dk', 'purple_dk', 'blue']


def tv(k: int) -> Canvas:
    c = Canvas(W, H)
    x0, y0, w, h = 3, 8, 26, 22
    # 로토무 머리 위 플라즈마 뿔/안테나 (살짝 흔들림 + 전기 오라)
    sway = [0, 1, 0, -1, 0, 1][k]
    c.rect(x0 + 11 + sway, 1, 4, 3, 'cyan')
    c.rect(x0 + 12 + sway, 2, 2, 6, 'orange')
    c.px(x0 + 12 + sway, 1, 'white'); c.px(x0 + 10 + sway, 4, 'cyan'); c.px(x0 + 15 + sway, 4, 'cyan')
    # 양옆 로토무 번개 날개 팔 (위아래로 파스스)
    wy = y0 + 7 + (k % 2)
    c.rect(1, wy, 2, 5, 'cyan'); c.px(0, wy + 2, 'white')
    c.rect(29, wy, 2, 5, 'cyan'); c.px(31, wy + 2, 'white')
    # 주황색 로토무 TV 케이스
    c.rect(x0, y0, w, h, 'orange')
    c.rect(x0, y0, w, 1, 'gold')
    c.rect(x0, y0 + h - 2, w, 2, 'rust')
    c.rect(x0 + w - 7, y0 + 2, 5, h - 5, 'rust')
    # 다이얼 2개 + 스피커 줄
    for j in range(2):
        c.rect(x0 + w - 6, y0 + 3 + j * 5, 3, 3, 'yellow'); c.px(x0 + w - 5, y0 + 4 + j * 5, 'black')
    for j in range(3):
        c.hline(x0 + w - 6, x0 + w - 4, y0 + 14 + j * 2, 'black')
    # 볼록 화면 (모서리 둥글게)
    sx, sy, sw, sh = x0 + 2, y0 + 2, 16, 15
    bg = SCREEN_BG[k]
    c.rect(sx, sy, sw, sh, 'navy')
    c.rect(sx + 1, sy + 1, sw - 2, sh - 2, bg)
    for (px, py) in ((sx + 1, sy + 1), (sx + sw - 2, sy + 1), (sx + 1, sy + sh - 2), (sx + sw - 2, sy + sh - 2)):
        c.px(px, py, 'navy')
    # 로토무 눈 표시 + 통통 뛰는 피카츄/몬스터볼 방송
    jump = [0, 1, 3, 4, 3, 1][k]
    cx = sx + 5 + [0, 1, 2, 3, 2, 1][k]
    cy = sy + sh - 7 - jump
    c.ellipse(cx + 1.5, cy + 1.5, 2.5, 2.5, 'yellow')
    c.px(cx - 1, cy - 1, 'yellow'); c.px(cx + 4, cy - 1, 'yellow')      # 귀
    c.px(cx, cy + 1, 'black'); c.px(cx + 3, cy + 1, 'black')             # 눈
    c.px(cx + 1, cy + 2, 'red'); c.px(cx + 2, cy + 2, 'red')             # 입
    c.px(cx - 1, cy + 2, 'pink_hot'); c.px(cx + 4, cy + 2, 'pink_hot')   # 볼
    # 반짝이 전기 별 (배경)
    c.px(sx + 12 - k % 3, sy + 3 + k % 2, 'white')
    # 볼록 반사광
    c.hline(sx + 2, sx + 5, sy + 2, 'white')
    c.px(sx + 2, sy + 3, 'white')
    # 케이스 하단 로토무 특유의 지그재그 미소
    c.hline(x0 + 4, x0 + 15, y0 + h - 3, 'white')
    c.px(x0 + 6, y0 + h - 4, 'white'); c.px(x0 + 10, y0 + h - 4, 'white'); c.px(x0 + 13, y0 + h - 4, 'white')
    # 받침
    c.rect(x0 + 4, y0 + h, 18, 2, 'rust')
    c.outline('black')
    return c


def frames():
    return [
        ('arcade', [arcade(k) for k in range(6)], 140),
        ('tv', [tv(k) for k in range(6)], 180),
    ]
