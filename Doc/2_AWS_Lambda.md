## 🍷 2 Serverless 

---

#### AWS 컴퓨팅 서비스
* EC2, Lightsail, Elastic Beanstalk 등등..과 같은 서비스다.

![](image/2025-01-23-03-33-31.png)

---

> ### 📄 1. 서버리스 이해하기
* VM 인스턴스를 미리 구매하지 않아도 되며 서버필요 없이 단순히 코드만 배포.
* 함수 실행 시 100ms 단위 사용량에 따라 요금을 지불
상시 작동할 필요가 없는 서버인 경우, 서버리스 "컴퓨팅"을 사용하면 필요한 경우에만 실행되어 요금을 절약 가능
* 높은 확장성 및 빠른 서비스 연동

#### 1). 가상 컴퓨팅 기술 비교 

* AWS 컴퓨팅 비교 테이블
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
* REST API 호출 가능 (API Gateway 콜과 연동)

##### ③ 효과적인 권한 통제
* Virtual Private Cloud(사설 네트워크) 연동 및, IAM Role을 사용한 실행 권한 설정
* AWS 이벤트 소스에 대한 다양한 리소스 정책

---

> ### 2. 서버리스 서비스와 타 서비스 통합

![](image/2025-01-23-02-03-37.png)

##### ① 파일 처리
* S3 스토리지에 파일이 업로드됨에 트리거를 AWS Lambda로 등록할 수 있다
##### ② 웹 애플리케이션 
* 고가용성을 제공하고, 서버의 스케일 업/다운이 용이한 서비스 구축 가능
##### ③ 모바일 백엔드
##### ④ A/B 테스트
##### ⑤ 크롤러 또는 봇 신속 처리

---

> ### 📄 3. 개념 이해

##### ① Lambda 함수&런타임 
1. **Lambda 함수 :**
     * 서버리스 서비스를 생성하는데 사용하는 기본 구성 요소, 
     런타임은 함수가 실행되는 언어 환경
     * EX 
         ```
         사용자가 웹사이트 버튼을 클릭하거나, 
         S3 버킷에 파일을 업로드할때의 이벤트를 트리거할떄
         Amazon DynamoDB 테이블에 항목이 추가될 때
         SQS (Simple Queue Service) 메세지 쓰기 작업
          비동기 메세징 큐 서비스
         ```
     * 람다 배포 방법
         1. .zip 파일
         2. 컨테이너 이미지

2. **Lambda 런타임 :**
   * 함수가 처음 호출되면 Lambda는 함수가 실행될 새 실행환경을 생성함
   * 초기 호출에 조금 딜레이가 있을 수 있다.
   * 다시 호출되면 기존 실행환경을 재사용할 수 있음
   * Node.js나 Python같은 런타임 언어를 쓸 수도, 
   만약 Go, C++, Rust를 사용하려면 OS전용 런타임을 사용할 수도 있다.
   이런 OS 전용 런타임을 사용한다면 컴파일 된 바이너리만 있으면 됨

##### ② 트리거 및 이벤트 소스 매핑 : AWS 서비스에서 함수를 간접적으로 호출하는 방법.

##### ③ 이벤트 객체 : 함수가 처리할 이벤트 데이터가 포함된 Json 객체
Python 런타임에서는 딕셔너리 또는 리스트로 변환
1. 람다 이벤트 (Json 형식)
   ```json
   {
     "Location": "SEA",
     "WeatherData":{
       "TemperaturesF":{
         "MinTempF": 22,
         "MaxTempF": 78
       },
       "PressuresHPa":{
         "MinPressureHPa": 1015,
         "MaxPressureHPa": 1027
       }
     }
   }
   ```
2. Python으로 이벤트 객체 접근
   ```python
   MinTemp = event['WeatherData']['TemperaturesF']['MinTempF']
   ```

##### ④ 함수가 다른 AWS 리소스에 액세스할 수 있는 권한
* IAM을 통해 실행 역할, 정책을 설정할 수 있다.
* Lambda가 AWS 리소스에 엑세스하고, 해당 리소스에 대한 작업을 수행해야 할 때
함수에 권한 부여를 해 줘야 한다.
   * DynamoDB테이블에서 CRUD 작업을 수행하는 경우 AmazonDynamoDBFullAccess 정책을 역할에 추가해야한다.
* 베스트 프랙티스는 작업을 수행하는데 필요한 권한만 부여한다 (최소 권한 원칙)

---

> ### 📄 4. AWS Lambda 프로그래밍
* Lambda 함수의 클래스가 메모리에 유지되므로, 
초기화 코드에서 핸들러 메서드 외부에서 선언된 클라이언트 및 변수를 재사용할 수 있습니다.
* 함수는 여러 간접 호출에 사용할 수 있는 임시 캐시인 /tmp 디렉터리의 로컬 스토리지에 액세스할 수 있습니다. 
(정확한 것은 "실행환경" & "실행환경 생명 주기") 확인하기

---

> ### 📄 5. Lambda 실행 환경 & 수명 주기

<img src="https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/images/Overview-Successful-Invokes.png">

* 함수 실행 뿐만 아니라, 실행에 필요한 리소스도 관리한다.
* 각 실행 환경은 `/tmp` 디렉터리에 512MB에서 10,240MB 사이 1MB 단위로 디스크 공간을 제공합니다. 
디렉터리 콘텐츠는 실행 환경이 일시 중지되어도 그대로 유지되기 때문에 일시적인 캐시를 여러 호출에서 사용할 수 있습니다.
* 생명 주기
   ```txt
   1. 초기화 단계 
      함수 실행 전 지연 시간에 가장 많이 기여하는 요인은 초기화 코드입니다.
         Function Init : 함수의 정적 코드 실행
         Extension Init
         Runtime Init
      10초 이내 완료되지 않으면 함수 타임아웃으로 Init 단계를 재실행
   2. 호출 단계
   3. 종료 단계
   ```

#### 1). 정적 초기화 최적화

---

> ### 📄 6. Lambda 아키텍쳐링


#### 1). 모놀리스 보단, 마이크로 서비스!

##### ① 모놀리스 : 안티패턴
<div align=center>
   <img src="https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/images/event-driven-architectures-figure-13.png">
</div>

* 하나의 람다함수로 모든 API Gateway 라우트를 처리함
* 함수하나에 복수의 기능이 결합되어 있어 함수단위 단일 책임이 아니므로 확장과 유지보수가 더 어렵다.

##### ② 마이크로 서비스 : 권장 패턴
<div align=center>
   <img src="https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/images/event-driven-architectures-figure-14.png">
</div>

* 기능에 따라 분리된 복수의 함수를 마이크로 서비스로 분해하여 API Gateway 라우트에 기반한 처리를 하도록 해야한다.

#### 2). Lambda 함수 Synchronous 

##### ① 한 함수에서 동기식 대기

<div align=center>
   <img src="https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/images/event-driven-architectures-figure-17.png">
</div>

* 한 함수에서 Synchronous 처리를 하도록 하면 대기 시간이 길어지는 요인이 된다.

##### ② 별도의 Lambda 함수 트리거링

<div align=center>
   <img src="https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/images/event-driven-architectures-figure-19.png">
</div>

* AWS 통합 시스템에서 Lambda함수를 간접 호출하는 On-Demand 방식으로 데이터를 제공해야한다.
* 따라서 AWS에 통합된 타 서비스(S3, DynamoDB 등..) 
이벤트 트리거를 별도의 Lambda로 위임하도록 


---

> ### 📄 7. Lambda 기반 애플리케이션 설계 원칙

#### 1). 워크로드 목표

**소프트웨어 개발 및 분산 시스템에 적용되는 많은 모범 사례가 서버리스 애플리케이션 개발에도 적용됩니다.**

##### ① 비용 효율성
##### ② 성능
* 컴퓨팅 리소스를 효율적으로 사용
##### ③ 신뢰성 & 내구성 & 보안
* 고가용성을 제공할 수도 있다.
* 내구성 요구사항을 충족하는 스토리지 옵션을 제공(? S3 참고하기)
* IAM을 통해 엑세스 보호 제공

#### 2). Lambda 설계 원칙
1. 직접 개발하지 말고 통합 서비스를 이용해 보자.
   * Lambda와 주로 통합되는 서비스
      ```
      데이터 스토리지 : {S3, DynamoDB, RDS}
      REST API : API Gateway
      ```
   * 패턴 제공
      ```
      메세지 큐         : SQS
      이벤트 버스       : EventBridge
         * 함수를 시간 일정에 따라 실행하는 기능을 만들 수 있다.
         예약된 표현식 cron 구문을 사용하면 Lambda함수를 트리거 할 수 있다.
         https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html
      게시/구독(팬아웃)  : Amazon SNS
      이벤트 스트림      : Amazon Kinesis
      ```

2. Lambda의 추상화 수준 이해
   * API Gateway와 Lambda가 상호 작용할 때는 서비스에서 완전히 관리하므로 로드 밸런싱 개념이 없습니다

3. 상태 비저장 구현
   * 변수나 데이터 등 상태는 함수 내에서만 사용되는 지역변수로만 존재하도록 하는것이 유리하다.
   * 단, DB연결 라이브러리 로드 상태 같은 경우 재사용되므로 이러한 부분은 정적 초기화를 하여
   함수가 호출될 때 마다 초기화 하지 않도록 최적화 하자.


---

### 참고

* [서버리스 이해하기](https://thebook.io/080334/0548/)
* [AWS Lambda 설명서](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/welcome.html)