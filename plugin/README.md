# korean-tech-writing 플러그인

한국어 기술 산문의 어조·제목·문체를 다루는 세 스킬이다.
설치하면 Claude Code가 이 세 스킬을 자동으로 인식하고, 해당하는 요청이 들어올 때 스스로 부른다.

## 설치

```bash
claude plugin marketplace add pebblous/korean-tech-writing
```

```bash
claude plugin install korean-tech-writing@korean-tech-writing
```

Claude Code 안에서는 `/plugin marketplace add pebblous/korean-tech-writing` 으로도 된다.
설치 뒤 새 세션부터 잡힌다. 지금 바로 쓰려면 `/reload-plugins`를 실행한다.

확인:

```bash
claude plugin list
```

## 세 스킬

| 스킬 | 하는 일 | 부르는 시점 |
|---|---|---|
| `ko-voice` | 어조 세 결(기본·사유·커버) 중 하나를 골라 본문을 다시 쓴다 | 작성 단계, 또는 어조를 바꿀 때 |
| `ko-prose-humanizer` | 문체 흔적 11종을 채점하고 산문 질감만 교정한다 | 게시 전 마지막 검수 |
| `ko-title` | 제목 세 자리를 점검하고 고쳐 쓴다 | 본문이 끝난 뒤 |

권장 순서는 작성, `ko-voice`(필요할 때), `ko-prose-humanizer`, `ko-title`이다.

## 부르는 법

이름을 대고 부를 수도 있고, 그냥 말해도 된다.

```
/ko-prose-humanizer report/index.html
/ko-voice draft.md --voice=reflective
/ko-title report/index.html
```

아래처럼 말해도 해당 스킬이 잡힌다.

- "이 글 AI 티 나는데 좀 다듬어 줘"
- "논문체 좀 빼 줘"
- "제목이 어색한데 후보 몇 개 뽑아 줘"

## 세 스킬이 지키는 공통 원칙

**내용이 아니라 질감을 고친다.** 세 스킬 모두 아래를 절대 바꾸지 않는다.

- 숫자, 통계, 날짜, 고유명사, 인용 원문
- 인용 출처, 링크, 참고문헌, 각주
- 글의 논리 구조, 소제목 체계, 단락 순서
- 문서의 마크업 구조와 속성

## 조직에 맞게 조정하기

두 자리를 각 조직이 채워야 제 성능이 난다.

1. **기준 글.** 사람이 쓴, 그 조직이 지향하는 글 한 편을 어조별로 등록한다.
   임계값만 보는 것보다 훨씬 정확하다.
2. **비유 체계.** 짧은 글에서 쓸 비유를 하나 정하고 개념마다 고정한다.

두 자리를 채우는 방법은 저장소 문서에 있다.

## 규칙의 근거

각 스킬은 자체적으로 실행 가능하도록 필요한 규칙을 모두 담고 있다.
규칙이 어디서 나왔고 임계값이 무엇에 근거하는지는 저장소 문서를 본다.

<https://github.com/pebblous/korean-tech-writing>

## 라이선스

MIT. 저장소 루트의 `LICENSE` 참조.
저장소의 `docs/` 아래 문서는 CC BY 4.0으로 별도 적용된다.
