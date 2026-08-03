#!/usr/bin/env python3
"""문체 흔적의 1차 신호를 센다.

본문 산문만 센다. 제목, 표, 코드, 인용 블록은 빼고 잰다.
이것을 빼지 않으면 소제목의 줄표가 본문 재진술로 잡혀 거짓 경보가 난다.

    python3 measure.py <파일> [--short]

--short 를 주면 짧은 글(소개글, 소셜 미디어)의 좁은 임계값을 쓴다.
"""

import re
import sys


def strip_markdown(t):
    """마크다운에서 본문 산문만 남긴다."""
    t = re.sub(r'^---\n.*?\n---\n', '', t, count=1, flags=re.DOTALL)  # 머리말
    t = re.sub(r'```.*?```', '', t, flags=re.DOTALL)                   # 코드 블록
    t = re.sub(r'`[^`\n]+`', '', t)                                    # 인라인 코드
    lines = []
    for ln in t.split('\n'):
        s = ln.strip()
        if s.startswith('#'):      continue   # 제목
        if s.startswith('|'):      continue   # 표
        if s.startswith('>'):      continue   # 인용 블록 (대개 나쁜 예)
        if re.match(r'^[-*_]{3,}$', s): continue
        if re.fullmatch(r'\*\*[^*]+\*\*', s): continue   # 볼드만 있는 줄 = 실질 소제목
        lines.append(ln)
    return '\n'.join(lines)


def strip_html(t):
    """HTML에서 본문 산문만 남긴다."""
    for tag in ('script', 'style', 'table', 'pre', 'code', 'blockquote',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'figcaption', 'nav'):
        t = re.sub(rf'<{tag}\b.*?</{tag}>', ' ', t, flags=re.DOTALL | re.IGNORECASE)
    t = re.sub(r'<(meta|link|img)\b[^>]*>', ' ', t, flags=re.IGNORECASE)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.DOTALL)
    return re.sub(r'<[^>]+>', ' ', t)


META_AHEAD = ['옮긴다', '풀어 쓰자면', '짚어 본다', '묶어 본다', '한 발 더 들어가면',
              '다시 읽어 본다', '다음 표가', '한눈에 본다', '또렷해진다', '살펴본다']
TRANSLATIONESE = ['에 있어서', '을 부른다', '라는 진단이다', '을 가능하게 한다',
                  '되어진', '된 것이다']
REPEATED = ['한 줄', '한 문장', '한 자리', '한 좌표', '한 가지', '한 화면']
ACADEMIC = ['본 보고서', '규명한다', '분석하고자', '고찰한다']
PROMOTIONAL = ['혁신적', '획기적', '놀라운', '차세대', '게임 체인저']
CONNECTIVES = ['흥미롭게도', '주목할 만한', '결론적으로', '이러한 맥락에서']
NOMINAL_END = ['이다.', '점이다.', '사실이다.', '것이다.']
ENGLISH_CLICHE = ['delve', 'moreover', 'furthermore', 'crucial', 'paradigm shift',
                  'underscore', 'stands as a testament', 'in the realm of',
                  'it is worth noting', 'a tapestry of']


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    short = '--short' in sys.argv
    if not args:
        print(__doc__)
        return 1

    path = args[0]
    raw = open(path, encoding='utf-8').read()
    body = strip_html(raw) if path.lower().endswith(('.html', '.htm')) else strip_markdown(raw)
    text = re.sub(r'\s+', ' ', body).strip()
    chars = len(text)

    if chars < 200:
        print(f"본문이 {chars}자뿐이다. 측정이 의미 없다.")
        return 0

    print(f"파일: {path}")
    print(f"본문 {chars}자 (제목·표·코드·인용 제외)\n")

    # T1 줄표
    dashes = text.count('—')
    per = chars // dashes if dashes else 0
    limit = 600 if short else 500
    danger = 400 if short else 300
    if not dashes:
        verdict = '통과'
    elif per < danger:
        verdict = '교정 필요'
    elif per < limit:
        verdict = '경고'
    else:
        verdict = '통과'
    freq = f"{per}자당 1개" if dashes else "없음"
    print(f"T1  줄표          {dashes:4}개  {freq:>14}   {verdict}")

    def report(code, label, words, per_thousand_limit=None, threshold=0):
        hits = [(w, text.count(w)) for w in words]
        hits = [(w, c) for w, c in hits if c > threshold]
        total = sum(c for _, c in hits)
        mark = '통과' if total == 0 else '검토'
        detail = ', '.join(f"{w} {c}" for w, c in sorted(hits, key=lambda x: -x[1])[:4])
        print(f"{code:3} {label:14}{total:4}개  {'':>14}   {mark}"
              + (f"   {detail}" if detail else ""))

    report('T2', '명사형 종결', NOMINAL_END)
    report('T3', '반복 표현', REPEATED, threshold=3)
    report('T4', '메타 예고문', META_AHEAD)
    report('T7', '번역투', TRANSLATIONESE)
    report('T7', '논문체', ACADEMIC)
    report('--', '광고체', PROMOTIONAL)
    report('--', '접속부사', CONNECTIVES)

    low = text.lower()
    en = [(w, low.count(w)) for w in ENGLISH_CLICHE]
    en = [(w, c) for w, c in en if c]
    if en:
        print(f"EN  영어 상투구    {sum(c for _, c in en):4}개  {'':>14}   검토   "
              + ', '.join(f"{w} {c}" for w, c in en[:4]))

    print("\n숫자는 시작점일 뿐이다. 판정은 증거 문구를 직접 읽고 내린다.")
    print("T5·T6·T8·T9·T10·T11은 기계로 세지 않는다. 사람이 본다.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
