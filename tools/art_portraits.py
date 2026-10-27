"""portraits — 32x32 스토리 대화창 초상화 (말할 때 입 2프레임)

  por_me       조리모를 쓴 피카츄 (새 사장 요리사)
  por_grandma  오박사 (흰 연구 가운, 회색 머리)
  por_hsgirl   님피아 (분홍 귀, 리본 더듬이)
  por_judo     잠만보 (청록 몸통, 크림 얼굴, 실눈)
"""
from pixel import Canvas

W = H = 32


def _frame_bg(c: Canvas, col: str):
    c.rect(0, 0, W, H, col)
    for y in range(0, H, 4):
        for x in range((y // 4) % 2 * 2, W, 4):
            c.px(x, y, 'white' if col in ('yellow', 'cream') else 'slate')


def _mouth(c: Canvas, k: int, y=21, x=15, color='red_dk'):
    if k == 0:
        c.hline(x - 1, x + 2, y, color)
    else:
        c.rect(x - 1, y - 1, 4, 3, color); c.hline(x, x + 1, y + 1, 'pink')


def me(k: int) -> Canvas:
    """조리모를 쓴 피카츄 요리사"""
    c = Canvas(W, H)
    _frame_bg(c, 'gold')
    # 몸통: 노란 피카츄 + 빨간 스카프/앞치마
    c.rect(6, 25, 20, 7, 'yellow')
    c.rect(8, 25, 16, 4, 'red'); c.hline(9, 22, 25, 'pink')
    c.rect(12, 28, 8, 4, 'white')  # 앞치마
    # 피카츄 귀 (양옆 위로 뻗음 + 검은 끝)
    c.line(7, 13, 2, 3, 'yellow'); c.line(8, 13, 3, 3, 'yellow'); c.line(9, 13, 4, 4, 'gold')
    c.line(2, 3, 4, 6, 'black'); c.line(3, 3, 5, 6, 'black')
    c.line(24, 13, 29, 3, 'yellow'); c.line(23, 13, 28, 3, 'yellow'); c.line(22, 13, 27, 4, 'gold')
    c.line(29, 3, 27, 6, 'black'); c.line(28, 3, 26, 6, 'black')
    # 얼굴 (통통한 노란 볼)
    c.ellipse(15.5, 17, 9, 8, 'yellow')
    c.ellipse(15.5, 19, 9.5, 5.5, 'yellow')
    c.vline(24, 15, 22, 'gold')
    # 하얀 조리모 (머리 위)
    c.ellipse(15.5, 6, 7.5, 4.5, 'white')
    c.ellipse(11, 6, 3.5, 3, 'white'); c.ellipse(20, 6, 3.5, 3, 'white')
    c.rect(9, 8, 14, 3, 'gray_lt'); c.hline(9, 22, 8, 'white'); c.hline(9, 22, 10, 'red')
    c.vline(13, 4, 7, 'gray_lt'); c.vline(18, 4, 7, 'gray_lt')
    # 눈 + 코 + 빨간 전기 볼
    for x in (11, 19):
        c.rect(x, 15, 3, 3, 'black'); c.px(x, 15, 'white')
    c.px(15, 18, 'black'); c.px(16, 18, 'black')
    c.ellipse(8.5, 20, 2.2, 2, 'red'); c.px(8, 19, 'pink')
    c.ellipse(22.5, 20, 2.2, 2, 'red'); c.px(22, 19, 'pink')
    _mouth(c, k, y=21, x=15)
    c.outline('black')
    return c


def grandma(k: int) -> Canvas:
    """오박사 (흰 연구 가운 + 붉은 셔츠 + 회색 덥수룩 머리)"""
    c = Canvas(W, H)
    _frame_bg(c, 'cream')
    # 흰 연구 가운 + 안쪽 주황/빨강 셔츠
    c.rect(4, 24, 24, 8, 'white')
    c.rect(12, 24, 8, 8, 'orange_dk'); c.rect(13, 25, 6, 7, 'rust')
    c.line(10, 24, 12, 31, 'gray_lt'); c.line(21, 24, 19, 31, 'gray_lt')
    # 얼굴
    c.ellipse(15.5, 15, 8, 9, 'skin')
    c.vline(23, 13, 20, 'skin_dk')
    # 오박사 특유의 회색/갈색 뾰족 머리
    c.ellipse(15.5, 8, 9, 5, 'gray')
    for sx in (8, 12, 16, 20):
        c.line(sx, 5, sx + 1, 2, 'gray'); c.px(sx + 1, 3, 'gray_lt')
    c.vline(7, 9, 16, 'gray'); c.vline(24, 9, 16, 'gray')
    c.hline(10, 21, 10, 'gray_dk')
    # 짙은 눈썹 + 인자한 눈
    c.rect(10, 12, 4, 2, 'gray_dk'); c.rect(18, 12, 4, 2, 'gray_dk')
    for x in (11, 18):
        c.rect(x, 15, 2, 2, 'black'); c.px(x, 15, 'white')
    c.px(15, 17, 'skin_dk'); c.px(16, 18, 'skin_dk')
    _mouth(c, k, y=21, x=15)
    c.outline('black')
    return c


def hsgirl(k: int) -> Canvas:
    """님피아 (분홍/크림 얼굴, 큰 귀, 리본 보우와 더듬이)"""
    c = Canvas(W, H)
    _frame_bg(c, 'pink')
    # 목 주변 크림 털 + 목 리본 보우
    c.rect(6, 25, 20, 7, 'cream')
    c.rect(11, 25, 10, 5, 'white')
    c.rect(9, 26, 4, 3, 'pink'); c.rect(19, 26, 4, 3, 'pink')
    c.rect(14, 26, 4, 3, 'blue'); c.px(15, 27, 'cyan')
    # 양쪽 큰 귀 (분홍 + 파랑 안쪽)
    c.ellipse(6, 8, 3, 6, 'pink'); c.ellipse(6, 8, 1.5, 4, 'blue')
    c.ellipse(25, 8, 3, 6, 'pink'); c.ellipse(25, 8, 1.5, 4, 'blue')
    # 얼굴 (크림 아랫부분 + 분홍 윗머리)
    c.ellipse(15.5, 16, 8.5, 8, 'cream')
    c.ellipse(15.5, 11, 8.5, 4.5, 'pink')
    c.hline(9, 22, 13, 'pink')
    # 왼쪽 귀 밑 리본 보우 + 날리는 리본 더듬이
    c.rect(5, 11, 6, 3, 'white'); c.rect(7, 11, 2, 3, 'pink_hot')
    c.line(23, 12, 29, 9, 'white'); c.px(29, 9, 'blue'); c.px(28, 10, 'pink')
    # 푸른 눈 + 속눈썹
    for x in (11, 19):
        c.rect(x, 15, 3, 3, 'blue_dk'); c.px(x + 1, 16, 'cyan'); c.px(x, 15, 'white')
    c.px(10, 14, 'black'); c.px(22, 14, 'black')
    c.px(9, 19, 'pink'); c.px(22, 19, 'pink')
    _mouth(c, k, y=21, x=15, color='pink_hot')
    c.outline('black')
    return c


def judo(k: int) -> Canvas:
    """잠만보 (청록색 커다란 머리와 귀, 크림색 얼굴, 실눈과 송곳니)"""
    c = Canvas(W, H)
    _frame_bg(c, 'blue')
    # 큼직한 청록 어깨 + 크림 배
    c.rect(2, 23, 28, 9, 'teal_dk')
    c.ellipse(15.5, 29, 10, 5, 'cream')
    # 뾰족한 청록 귀
    c.ellipse(6, 7, 3.5, 4.5, 'teal_dk')
    c.ellipse(25, 7, 3.5, 4.5, 'teal_dk')
    # 둥글고 큰 청록 머리 + 크림 얼굴(이마 V자 경계)
    c.ellipse(15.5, 15, 11, 9.5, 'teal_dk')
    c.ellipse(15.5, 17, 9, 7.5, 'cream')
    c.ellipse(15.5, 10, 4, 2.5, 'teal_dk')  # 이마 중앙 V자 내려옴
    # 실눈 (ㅡ ㅡ)
    c.hline(9, 13, 15, 'black'); c.hline(18, 22, 15, 'black')
    c.px(9, 14, 'black'); c.px(22, 14, 'black')
    # 볼 홍조
    c.px(8, 18, 'tan'); c.px(23, 18, 'tan')
    # 입 + 작은 아랫송곳니
    _mouth(c, k, y=20, x=15, color='red_dk')
    c.px(12, 19, 'white'); c.px(19, 19, 'white')
    c.outline('black')
    return c


def frames():
    return [
        ('por_me', [me(0), me(1)], 160),
        ('por_grandma', [grandma(0), grandma(1)], 160),
        ('por_hsgirl', [hsgirl(0), hsgirl(1)], 160),
        ('por_judo', [judo(0), judo(1)], 160),
    ]
