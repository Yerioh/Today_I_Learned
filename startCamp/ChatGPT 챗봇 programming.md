# ChatGPT 챗봇 programming

## 1. ChatGPT 가입 및 API  key 발급

- API(Application Programming Interface) : 두 소프트웨어가 서로 통신할 수 있게 하는 매커니즘
    - 예시 ) 소셜 로그인(이용 사이트↔각 포털(구글, 카카오, 네이버)) / 날씨 데이터(기상청↔스마트폰) 등 /
- ChatGPT API key 발급: 내 소프트웨어에서 GPT 모델과 통신하여 사용하기 위하여 발급받는 key

## 2. ChatGPT 사용하기

- 일반적인 사항을 질문하기
    - 한국 음식에 대해 소개해보세요.
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled.png)
    
- 맥락/요구 사항을 자세하게 질문하기
    - 결과 : 간편성과 좋은 성분을 모두 갖춘 신개념 칼슘 보조 식품 홍보 문구 작성
    - 제품 : 간편하게 마시기만 해도 키가 쑥쑥 크는 칼슘 가득 셰이크
    - 문맥 : 소셜 미디어 포스팅에 업로드할 홍보 문구
    - 대상 : 한국 남녀노소 키가 쑥쑥 크고 싶은 사람
    - 위의 사항을 반영해 인스타그램, 페이스북, 틱톡 등 소셜 미디어에 활용할 내용을 각 플랫폼 별로 따로 작성해 보세요.
    - 어조는 Fun 하고 캐주얼하게

![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%201.png)

![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%202.png)

- 이어서 세부 질문하기
    1. Netfilx 활용법을 소개하는 기사의 목차를 작성해 보세요.
    2. 목차에 맞게 150자 이내로 기사를 작성해 보세요.
    3. 기사에 맞는 제목을 세 가지 제안해 보세요.

![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%203.png)

- 세상에 없던  질문 던지기
    - 세종대왕의 아들인 정약용이 사용한 광선검에 대해 소개해 보세요.
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%204.png)
    
    - 선사시대 유물 빗살 무늬 자동차에 대해 소개해 보세요.
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%205.png)
    
    - 고려시대에 문익점이 들여온 콩순이 인형에 대해 소개해 주세요.
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%206.png)
    

## 3. 챗봇 program 만들기

- ChatGPT 연동
    - [ChatGPT 문서 참고 링크](https://platform.openai.com/docs/api-reference/chat) 활용 URL 입력
    - 발급 받은 API  key 확인
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%207.png)
    
- ChatGPT에게 메세지 받기
    - `res.data`객체 확인하기 → `res.data.choices[0].message.content` ⇒ GPT가 응답한 메세지의 내용
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%208.png)
    
    - 응답 메세지를 함수를 이용하여 html에 출력
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%209.png)
    
    - 다음 응답을 위하여 응답 메세지를 oldMsg 변수에 저장하여 사용
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2010.png)
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2011.png)
    

## 4. Python 활용 ChatGPT API 실습

- 필요 라이브러리 설치 및 API KEY 설정
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2012.png)
    
- 기본 사용 방법
    - API 파라미터
        
        
        | system | 기본 지침(톤, 스타일, 특정 규칙) |
        | --- | --- |
        | user | 사용자의 입력(질문 혹은 명령) |
        | assistant | 챗봇의 응답 |
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2013.png)
    
- 파라미터 변경
    - max_token, n 변경
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2014.png)
    
    - temperature, top_p 변경
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2015.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2016.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2017.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2018.png)
        
- 페르소나 생성
    - ChatGPT를 활용해 원하는 페르소나를 만든 후 페르소나 프롬프트에 넣어서 대화해보기
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2019.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2020.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2021.png)
        
- 프롬프트 엔지니어링 실습
    - 실습 1 : 명시적 지시
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2022.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2023.png)
        
    - 실습 2 : 퓨샷 프롬프트(Few-Shot Prompt)
        - 프롬프트에 몇 가지 예시를 제공하여 특정한 방식으로 답변을 생성하도록 유도하는 방법
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2024.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2025.png)
        
    - 실습 3 : 생각의 사슬(Chain-of-Thought)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2026.png)
        
        - case1
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2027.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2028.png)
        
        - case2
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2029.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2030.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2031.png)
        
    - 실습 4 : 자기 일관성(Self-Consistency)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2032.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2033.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2034.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2035.png)
        
    - 실습 5 : 인터넷 검색 기반 응답
        - 외부 지식을 토대로 신뢰성 있는 답변 받기(위키피디아 라이브러리 활용)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2036.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2037.png)
        
        ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2038.png)
        
- 참고 : 최대 입력 토큰을 넘어서는 입력을 했을 떄 API호출에 오류 발생 ⇒ 최대 입력 토큰을 넘어서지 않도록 최신 대화 내용 입력
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2039.png)
    
    ![Untitled](ChatGPT%20%E1%84%8E%E1%85%A2%E1%86%BA%E1%84%87%E1%85%A9%E1%86%BA%20programming%20ef04fd803e3e4e06842c3d7dfc593934/Untitled%2040.png)