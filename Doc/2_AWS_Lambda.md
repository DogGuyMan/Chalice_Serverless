## 🍷 2 Serverless 

---

![](image/2025-01-23-03-33-31.png)

---

### 1. 서버리스 이해하기
* VM 인스턴스를 미리 구매하지 않아도 되며 서버필요 없이 단순히 코드만 배포.
* 함수 실행 시 100ms 단위 사용량에 따라 요금을 지불
상시 작동할 필요가 없는 서버인 경우, 서버리스 "컴퓨팅"을 사용하면 필요한 경우에만 실행되어 요금을 절약 가능
* 높은 확장성 및 빠른 서비스 연동

#### 1). 가상 컴퓨팅 기술 비교 

|/|Packaging|Updates|Execution|Runtime|Unit of Cost|
|---|---|---|---|---|---|
|VMs|AMI|Patching|Multi-threaded & Multi-task|하루에서 몇달동안 작동|VM개수당 & 시간당|
|Containers|Container File|Versioning|Multi-threaded & single-task|분에서 하루 동안 작동|VM개수당 & 시간당|
|Serverless|Code|Versioning|Single-threaded & single-task|아주작은 클럭 타임|사용 메모리당 리퀘스트 당|

#### 2). AWS Lambda 동작 원리

##### ① 단순한 자원 모델
* 메모리 사이즈 설정 가능 128MB ~ 1.5GB 까지!
##### ② 유연한 호출 경로
* Event 기반 호출 옵션 (S3 같은 서비스들..)
* REST API 호출 가능 (API Gatewat 콜과 연동)

##### ③ 효과적인 권한 통제
* Virtual Private Cloud(사설 네트워크) 연동 및, IAM Role을 사용한 실행 권한 설정
* AWS 이벤트 소스에 대한 다양한 리소스 정책

---

### 2. 서버리스 서비스

![](image/2025-01-23-02-03-37.png)

1. AWS Lambda : 서버리스 컴퓨팅
2. API GateWay
3. S3 : 스토리지 (클라우드 데이터 저장소)
4. HTTP 헤더 검사, 접근 제어
5. 모바일 디바이스 탐지
6. A/B 테스트
7. 크롤러 또는 봇 신속 처리

---

### 3. AWS Lambda 세팅

1. "Create Function"으로 "Function"을 만들 수 있음
2. 런타임 환경을 정해줘야 하고
3. 코드의 사이즈 
4. AWS Lambda - Environment Variables
5. AWS Lambda - Modules


#### 1). Lambda Management Console
1. AWS Enviroment 만 설정 한다면 Function 코드를 직접 웹에서 수정할 수 있다.


---

### 참고

[서버리스 이해하기](https://thebook.io/080334/0548/)