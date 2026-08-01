# 고칠 때

## 규칙을 고치는 순서

문서와 스킬은 같은 규칙의 두 형태다. **문서가 정본**이다.

1. `docs/` 아래 해당 문서를 고친다
2. 그 규칙을 담고 있는 스킬(`plugin/skills/*/SKILL.md`)을 같이 고친다
3. 두 곳의 표현이 어긋나지 않는지 확인한다

스킬만 고치고 문서를 두면 다음에 문서를 읽은 사람이 다른 규칙을 따르게 된다.

## 스킬은 자급자족해야 한다

각 `SKILL.md`는 그 스킬을 실행하는 데 필요한 규칙을 **전부 자체에 담는다.**
"저장소 문서를 읽으라"고 미루지 않는다. 에이전트가 그 문서를 읽는다는 보장이 없기 때문이다.

문서를 가리켜야 할 때는 규칙을 요약해 스킬 안에 넣고, 원문 위치를 함께 적는다.

## 규칙이 흔적을 만든다

권장 목록을 만들 때는 그것이 기계적으로 복제될 것을 전제한다.
`docs/title.md` 9절에 이 저장소가 한 번 겪은 사례가 적혀 있다.

권장 유형을 늘리기 전에 물어본다. **이 유형이 모든 글에 적용되어도 괜찮은가.**
안 괜찮다면 권장이 아니라 조건을 적어야 한다.

## 외부 자료를 가져올 때

자료마다 이용 조건이 다르다. `NOTICE.md`를 먼저 읽는다.

- **변경 금지 조건**의 자료는 원문 표나 문장을 옮기지 않는다. 규칙을 우리 말로 다시 진술한다
- **동일조건변경허락(SA)** 조건의 자료는 문장을 가져오면 저장소 전체가 그 조건에 묶인다.
  착안점만 얻고 새로 쓴다
- 새 자료를 참고했으면 `NOTICE.md`에 출처와 조건, 그리고 **어느 선까지 썼는지**를 적는다

## 스킬을 고친 뒤 확인

```bash
claude plugin validate ./plugin --strict
claude plugin validate . --strict
```

버전을 올릴 때는 `plugin/.claude-plugin/plugin.json`과 `.claude-plugin/marketplace.json`의
`version`을 함께 올린다. 둘이 어긋나면 검증에서 걸린다.

## 실제로 설치해 본다

선언만으로 끝내지 않는다. 다른 디렉터리에서 실제로 설치해 스킬이 잡히는지 확인한다.

```bash
claude plugin marketplace add pebblous/korean-tech-writing
claude plugin install korean-tech-writing@korean-tech-writing
claude plugin list
```
