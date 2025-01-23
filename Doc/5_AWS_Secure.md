## 🍷 5 AWS 보안

---

#### 1). Cognito & IAM 

이것을 사용해 REST API의 보안을 강화하자.

##### ① IAM Management Console
* Role설정 Permisson 설정

#### 2). 보안 엑세스 키

##### ① 보안 액세스 키 유출
* 예기치 않은 과금이 발생한다면 액세스 키 유출을 의심해봐야 합니다. 
* 따라서 실습이 끝난 뒤에는 사용하지 않는 액세스 키를 비활성화하거나 삭제하고, 
* `.env` 파일은 `.gitignore`에 추가해 깃허브 등에 올리지 말고 서버에서 직접 생성해 내용을 작성하는 것이 좋습니다.

```js
const s3 = new S3Client({
   credentials: {
   accessKeyId: process.env.S3_ACCESS_KEY_ID,
   secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
},
region: 'ap-northeast-2',
