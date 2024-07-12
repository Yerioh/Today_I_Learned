# Git

- 분산 버전 관리 시스템
- 코드의 ‘변경 이력’을 기록하고 ‘협업’을 원활하게 하는 도구

## 1. 용어 해석

### 1) 버전 관리

- 변화를 기록하고 추적하는 것
- 이전과 무엇과 달라졌는지만 기록해도 충분

 ***Google Docs를 활용한 버전 관리**

[https://www.google.com/intl/ko_KR/docs/about/](https://www.google.com/intl/ko_KR/docs/about/) 

- 파일 > 버전 기록 > 현재 버전 이름 지정 : 버전 저장
- 버전 기록 보기 : 저장된 버전들을 확인할 수 있음

![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled.png)

### 2) 분산

- 중앙 집중식 : 버전은 중앙 서버에 저장된고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리

**[장점]**

- 중앙 서버에 의존하지 않고도 동시에 다양한 작업 수행 가능
    - 개발자들 간의 작업 충돌을 줄여주고 개발 생산성 향상
- 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
- 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
    - 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버와 동기화

## 3. git의 역할

- 코드의 버전(히스토리)를 관리 ⇒ 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교
- git은 로컬 저장소 내 모든 파일의 ‘변경사항’을 감시하고 있다.

## 4. git의 영역

- Working Directory : 실제 작업 중인 파일들이 위치하는 영역
- Staging Area : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역(가상으로 존재!)
- Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역 모든 버전과 변경 이력이 기록됨
- commit : 변경된 파일들을 저장하는 행위이며,  마치 사진을 직뜻이 기록한다 하여 ‘snapshot’이라고도 함

## 5. git의 동작

- git init : 로컬 저장소 설정(초기화) ⇒ git의 버전 관리를 시작할 디렉토리에서 진행
- git add : 변경사항이 있는 파일을 Staging Area에 추가
- git commit :  Staging Area에 있는 파일들을 저장소에 기록 ⇒ 해당 시점의 버전을 생성하고 변경 이력을 남기는 것

## 6. git 진행하기

- git init : working directory 설정 (master)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%201.png)
    
- git add : staging area에 추가
    - git add . : 현재 폴더에 있는 파일을 전부 add
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%202.png)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%203.png)
    
- commit 생성하기
    - commit 작성자 정보 설정(메일주소, 유저네임)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%204.png)
    
    - commit : git commit -m “commit 명”
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%205.png)
    
    - log 확인하기 : git log
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%206.png)
    

## 7. git commit 실습

1. 바탕화면에 git_commit 폴더를 만들고 git 저장소 생성
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%207.png)
    
2. 해당 폴더 안에 a.txt 라는 텍스트 파일을 만들고, “add a.txt”라는 커밋 메세지로 커밋 생성
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%208.png)
    
3. 이번에는 b.txt 라는 텍스트 파일을 만들고, “add b.txt”라는 커밋 메세지로 커밋 생성
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%209.png)
    
4. a.txt 파일을 수정하고, “update a.txt” 라는 커밋 메세지로 커밋 생성
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2010.png)
    
5. 커밋 목록 확인하기
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2011.png)
    
    ![git log —oneline](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2012.png)
    
    git log —oneline
    
    ## 참고
    
    ### 1) 로컬 local
    
    - 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
    - 개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경
    
    ### 2) git 기타 명령어
    
    - git status : 현재 로컬 저장소의 파일 상태 보기
    - git log : git history 보기
    - git log —oneline : git 이력 한줄 보기
    - git config —global -l : git 환경설정 전체 보기
    
    ### 3) git init 주의 사항
    
    - git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것
        - 즉, 이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것
    - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문

## [부록]

### 1. Commit 수정하기

**바로 직전 생성한 commit 수정하기**

`git commit --amend`

- Commit 메시지 수정
    - `git commit --amend` 
    → Vim 에디터 열림( a : 입력 모드 / esc : 명령어 모드) 
    → `:wq` 로 저장하면 수정 완료
    - 수정 완료하면 해쉬 값도 변경됨(f30ca27 → 5d56236)co
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2013.png)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2014.png)
    
- Commit 전체 수정
    - 변경할 파일을 add 
    → `git commit --amend` 
    → Vim 에디터 진입 
    → `:wq` 로 저장
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2015.png)
    
- `git commit —amend` 정리
    - 버전관리 측면에서 봤을 때,
     “앗, 빠진 파일 넣었음”, “오타 살짝 고침” 과 같은 commit은 유효한 버전이라고 보기 어려움
    - 즉, 불필요한 commit을 생성하지 않고, 직전 commit을 수정할 수 있기 때문에 git에서 꼭 필요한 기능 중에 하나라고 볼 수 있음

### 2. 원격 저장소

- 코드와 버전관리 이력을 온라인 상의 특정 위치에 저장하여 개발자가 협업할 수 있도록 하는 서비스
ex) GitLab, GitHub 등

### 3. 로컬과 원격저장소(git & github) 연동

- `git clone <url>` : 원격저장소를 내 로컬에 다운로드
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2016.png)
    
- `git remote <origin> <url>` : 원격저장소를 <origin>이라는 이름으로 연동
**주의 : init한 폴더로 들어가야 명령어 실행됨
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2017.png)
    
- `git push <origin> <master>` : 원격저장소<origin>의 <master>브런치에 파일을 업로드
⇒ 로컬과 github 연동 완료
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2018.png)
    
- `git pull <origin> <master>` :  원격저장소<origin>의 내용을 다운로드
⇒ 충돌이 일어나지 않게 push와 pull은 규칙을 정해서 할 것
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2019.png)
    
- `clone` vs `pull`
    - `clone` : 프로젝트의 내용을 전부 내려받음
                  맨 처음 한번 사용(이미 init이 되어있음)
    - `pull` : 변경된 사항을 내려받음 
                  프로젝트 업데이트 시 사용
- `git remote -v`  : 원격저장소 연동 확인
- `git remote rm <origin>` : 원격저장소 연동 끊기

### 4. gitignore

- git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 파일
⇒ 프로젝트를 진행하며 공유하면 안되는 부분을 관리
    
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2020.png)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2021.png)
    
- 이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음
(`git rm —cached` 명령어를 통해 git 캐시에서 삭제 필요)
    
    ![Untitled](Git%20a20671e190ba4da3879638841ef993f6/Untitled%2022.png)
    
- gitignore 목록 생성 서비스
    - 운영체제, 프레임워크, 프로그래밍 언어 등 개발 환경에 따라 gitignore 목록을 만들어주는 사이트
    - [https://www.toptal.com/developers/gitignore](https://www.toptal.com/developers/gitignore)

### 5. GitHub 활용

- 프로젝트 협업
- 개인 포트폴리오
- TIL을 통해 내가 학습하는 것을 기록
    - Today I Learned
    - 매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것
    - ‘문서화’의 중요성 : 신입 개발자에게 요구되는 가장 중요한 덕목
    
    ⇒ 꾸준히 스스로 학습해 성장할 수 있고 문서화를 통해 내 생각을 정리하고 팀에게 공유할 수 있는 능력
    
- 개인, 팀 프로텍트 코드를 공유
    - 개발 면접 지원 시 본인의 GitHub 주소를 공유해 어떤 프로젝트를 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
- 오픈 소스 프로젝트에 기여