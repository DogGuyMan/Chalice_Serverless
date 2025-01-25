## 🍷 4 Amazon API Gateway

---

#### AWS 네트워킹 및 콘텐츠 전송 서비스
* VPC, CloudFront 등등... 과 같은 서비스다.

<!-- ![](image/2025-01-23-00-42-09.png)
<img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d572a6-c679-43d9-affa-54cc711a4b75_2250x2504.png"> -->


> ### 📄 1. 설명

#### Amazon API Gateway로 RESTful API를 생성하고 관리할 수 있음

애플리케이션이 돌아가는 클라이언트와 백엔드 마이크로 서비스 사이에 위치한다.

```
1. API를 이루는 
   1. Resources
   2. Stages
   3. Authorizers
   4. Gateway Responses
   5. Models
   6. Resource Policy
2. API Endpoint 마다 Method `GET`에 대해 어떻게 실행할 것인지 이런것을 UI로 설정 가능하다.
```

#### 1). 제공 기능
1. "REST API" "WebSocket API"를 {생성하고, 배포하고, 보호}한다.
   * WebSocket(상태 저장)
   * HTTP REST API (상태 비저장)
2. 트래픽 관리, 인증 매커니즘, 모니터링, API 버젼 관리
   * IAM || Lambda 권한 부여자 함수
3. API Request, Response 에 대한 처리를 담당한다.
4. AWS 백엔드 서비스에 엑세스 할 수 있게 해주는 "정문(Gateway)"의 역할을 수행한다. 
   1. "컴퓨팅 백엔드 서비스" (Lambda, EC2)
   2. "스토리지 백엔드 서비스" : (S3)
   3. "데이터 처리 서비스" : (Kinessis)
   4. "DB 백엔드 서비스" : (DynamoDB, RDS)
5. 위 기능을 어떠한 스케일이든 지원한다.

#### 2). API Gateway를 사용하는 방법.
1. AWS Management Console : 웹 기반 서비스
2. AWS SDK : 프로그래밍 스크립팅 가능
3. AWS CLI : 쉘 사용

> ### 📄 2. Quick Start



#### 1). Working With API Gateway Method

1. Query String Parameters
2. Post Method
3. Configuration
4. Using POSTMAN Tool

#### 2). API Gatewate Security
1. API Key
2. Lambda Authorizer

```
client send request to API Gateway RESTAPI
invoke lambda function that query dynamoDB 
http response back to client
```

> ### 📄 3. Chalice와 연동
* 배포시 AWS Lambda 와 같이 아래와 같은 형태로 Gateway API가 형성된 것을 확인할 수 있다.
   |배포 전| 배포 후|
   |---|---|
   |![](image/2025-01-25-01-23-28.png)|![](image/2025-01-25-01-24-11.png)|

* 리소스의 라우트 경로마다 HTTP Method(GET, POST, PUT, DELETE)가 연결 된 것을 확인할 수 있다.
![](image/2025-01-25-01-24-25.png)

> ### 참조
* [ Amazon API Gateway Doc](https://docs.aws.amazon.com/ko_kr/apigateway/latest/developerguide/welcome.html)
* [API Gateway](https://blog.bytebytego.com/p/api-gateway)
* [What is API Gateway? youtube](https://www.youtube.com/watch?v=6ULyxuHKxg8&t=12s)
