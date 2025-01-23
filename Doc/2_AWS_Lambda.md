## 🍷 2 Serverless 

---

![](image/2025-01-23-03-33-31.png)

---

### 1. 서버리스 이해하기
VM 인스턴스를 미리 구매하지 않아도 됩니다.
단순히 코드를 업로드한 뒤, 사용량에 따라 요금을 지불하면 됩니다. 
24시간 작동할 필요가 없는 서버인 경우, 서버리스 "컴퓨팅"을 사용하면 필요한 경우에만 실행되어 요금을 절약할 수도 있습니다.

---

### 2. 서버리스 서비스

![](image/2025-01-23-02-03-37.png)

1. AWS Lambda : 서버리스 컴퓨팅
2. API GateWay
3. S3 : 스토리지 (클라우드 데이터 저장소)
   * 클라우드 데이터 저장소가 대신 정적 파일(리소스, 이미지)을 제공하도록 위임
   * 이름은 "버킷"을 사용
   * 이걸 활용해서 Addressable와 같이 사용하여
     * AddressableAssetSettings와 Remode URL(S3, 구글 클라우 플랫폼) 를 사용할 수 있다.


* 예시
    1. S3 트리거 이벤트를 람다로 정의
        ```
        Events with the Simple Storage Service

        S3에서 람다에 트리거 실행
        람다는 이미지 처리
        처리된 이미지를 다시 S3에 저장
        ```
    2. AWS Lambda & DynamoDB 연동

---

### 3. AWS Lambda

1. "Create Function"으로 "Function"을 만들 수 있음
2. 런타임 환경을 정해줘야 하고
3. 코드의 사이즈 
4. AWS Lambda - Environment Variables
5. AWS Lambda - Modules


#### 1). Lambda Management Console
1. AWS Enviroment 만 설정 한다면 Function 코드를 직접 웹에서 수정할 수 있다.

---


---

### 참고

[서버리스 이해하기](https://thebook.io/080334/0548/)