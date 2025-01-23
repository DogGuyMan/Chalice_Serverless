## Serverless RESTful API

---

#### 스펙

언어 : python 
프레임 워크 : `Chalice` 
인프라 : AWS Serverless Lambda & Amazon API Gateway

---

#### 학습 내용 

마이크로 서비스, REST API, 서버리스 아키텍쳐를 AWS 환경에서 개발 가능하다.
또한 AWS 람다에 대한 이해가 높아질 것이다.

#### 로드맵

1. **AWS Enviroment Setting**
    * AWS Enviroment
    * Enviroment Variable
    * Tag
2. **Lambda**
   * lambda function using console
3. **Chalice Application**
   * chalice Project
   * [deploy on AWS Cloud](https://www.udemy.com/course/aws-chalice-build-serverless-rest-apis-on-aws/?couponCode=KEEPLEARNING)
4. **Deploy Application AWS Cloud**
   * AWS Gateway Sevice
   * REST Query Parameters / URL Parameter
   * Working With API Gateway Method / Request types
      * Accessing Request Data/Request Content Type
      * Accessing POST Data/POST Object
5. **S3, SQS 리소스에 접근하기**
   * 클라우드 데이터 저장소가 대신 정적 파일(리소스, 이미지)을 제공하도록 위임
   * 이름은 "버킷"을 사용
   * 이걸 활용해서 Addressable와 같이 사용하여
     * AddressableAssetSettings와 Remode URL(S3, 구글 클라우드 플랫폼) 를 사용할 수 있다.
6. **CRUD Postgresql 또는 DynamoDB 연동**

---
