# CLI

- Command Line Interface
- 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
- 컴퓨터의 성능을 최대한 발휘하기 위해서 주로 사용

↔ GUI (Graphic User Interface): 그래픽을 통해 사용자와 상호 작용하는 방식

## 1. 특징

- 효율성
    - CLI는 키보드만으로 모든 작업을 수행할 수 있으며 메모리와 CPU 사용량이 적어 저사양 시스템에서도 효율적으로 동작
- 정밀한 제어
    - 특정 프로그램이나 시스템의 세부 설정을 보다 정밀하게 제어할 수 있음
- 표준성
    - CLI 명령어는 대부분의 Unix 운영체제 기반 시스템에서 동일하게 작동하여 여러 환경에서 적용할 수 있음

## 2. 문법 및 활용

- ‘.’의 역할
    - .  :  현재 디렉토리
    - .. :  상위 디렉토리(부모)
- 기초 문법
    - touch : 파일 생성
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled.png)
    
    - mkdir : 새 디렉토리 생성
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled%201.png)
    
    - ls : 현재 작업 중인 디렉토리 내부의 폴더 혹은 파일 목록을 출력
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled%202.png)
    
    - cd :  현재 작업 중인 디렉토리를 변경(위치 이동)
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled%203.png)
    
    - start  : 폴더/파일을 열기 (Mac에서는 open)
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled%204.png)
    
    - rm : 파일 삭제(디렉토리 삭제시 -r까지 사용)
    
    ![Untitled](CLI%201bfd4f97be22456f895d936973807f70/Untitled%205.png)
    
    - claer : 터미널 내용 삭제
    - python : python 파일 실행
- 경로
    - 절대 경로 : Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
        
        ex) C:\Users\SSAFY\Desktop\12기_3반_김지원
        
    - 상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것