## 🍷 3  Python Chalice

---

### AWS Chalice란?
AWS Chalice는 AWS의 오픈 소스 서버리스 프레임워크로 빠르고 쉽게 서버리스 어플리케이션을 구축할 수 있습니다. Flask 스타일의 마이크로 웹 프레임워크를 기반으로 하고 있으며, **자동으로 AWS Lambda 함수를 생성**하고 **API Gateway 엔드포인트를 구성**해 줍니다. 또한 **Amazon DynamoDB, Amazon S3, SQS, SNS 등과 같은 서비스의 통합**도 지원합니다.

Chalice는 간단한 웹 애플리케이션 및 마이크로 서비스와 같은 작은 규모의 빠른 프로토타이핑 및 서버리스 애플리케이션 개발에 유용하며, 데이터 과학자가 Lambda 및 API Gateway와 같은 AWS 서비스에 대한 지식이 없더라도 쉽게 사용할 수 있습니다. 또한 Chalice는 일부 내장된 보안 기능, 로깅 및 오류 처리 기능을 제공하므로 개발자는 이러한 작업을 직접 처리할 필요가 없습니다.


#### 1). Chalice 설치
```bash
pip install chalice
chalice --help
```
#### 2). 프로젝트 생성
```shell
PROJECT = "hello-world"
chalice new-project $PROJECT
```

#### 3). 로컬 서버 
```bash
chalice local --port=8100
# curl(client url) 명령어는 프로토콜들을 이용해 
# URL로 데이터를 전송해 서버에 데이터를 보내거나 
# 가져올 때 사용하기 위한 명령줄 도구 및 라이브러리입니다.
# curl <url> : url에 request를 할 수 있는 명령어
curl localhost:8100
```

#### 4). 서버 배포
REST API URL : 생성하기
```bash
chalice deploy
```

#### 5). 챌리스 삭제
```bash
chalice delete
```

### Quick Start
[AWS Chalice Examples](https://github.com/daekeun-ml/aws-chalice-examples/tree/main)
[Chalice Doc](https://aws.github.io/chalice/)
[Chalice Quickstart](https://aws.github.io/chalice/quickstart.html)
[Introduction to AWS Chalice](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/00-intro-chalice.html)
[파이선(Python) 개발자를 위한 AWS 활용 - Youtube ](https://www.youtube.com/watch?v=0rkRvEr9RMk)
[파이선(Python) 개발자를 위한 AWS 활용 - slideshare](https://www.slideshare.net/awskorea/recap2016-1pythononaws)
