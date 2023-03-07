# BentoML-test


## 기본 개념

### 용어 정리

- Bento: 패킹된 머신러닝 모델 (도시락)
- Yatai: 머신러닝 모델을 관리함 (일본식 포장마차)
- Pack: 머신러닝 모델을 저장하는 과정 (음식 포장)
- 전체적인 과정: 
  - Bento에 들어갈 음식 (Artifact 및 코드)을 만들고 BentoML에 패킹(포장)을 요청, Deploy(배달)을 자동으로 해줌.
  - Bento를 확인하고 싶으면 Yatai가서 패킹되거나 deploy된 Bento를 확인하면 됨 
  
### 사용법

- 1. 모델 학습
- 2. Prediction Service Class 생성
  - BentoML에서 제공하는 Artifact를 사용해 생성
  - 서빙 로직 코드가 저장된 인퍼런스 API와 모델이 정의되어야함
3. Prediction Service에 학습한 모델 저장
  - 별도로 BENTOML_HOME을 설정하지 않으면 다음 경로에 저장됨: ~/bentoml/repository/{service_name}/{service_version}
4. Serving (Local)
5. Prediction Request (Inference Job 등, Local)
6. 모델 API 서버 컨테이너화
  - 컨테이너를 클라우드 서비스에 배포

### Serving

```bash
bentoml serve IrisClassifier:latest
```

### Prediction Request

```bash
curl -i --header "Content-Type: application/json" --request POST --data "[[5.1, 3.5, 1.4, 0.2]]" localhost:8898/predict
```

- Note that you should use "", instead of ''

## Reference

### BentoML
- https://engineering.linecorp.com/ko/blog/mlops-bentoml-1
- https://zzsza.github.io/mlops/2021/04/18/bentoml-basic/
- https://velog.io/@perfitt/BentoML-%EC%82%BD%EC%A7%88%EA%B8%B0

### Github deploy key
- https://stackoverflow.com/questions/11656134/github-deploy-keys-how-do-i-authorize-more-than-one-repository-for-a-single-mac
- https://wiki.terzeron.com/ko/%EA%B0%9C%EB%B0%9C_%EB%8F%84%EA%B5%AC/Git/Github_deploy_key%EB%A5%BC_%EC%9D%B4%EC%9A%A9%ED%95%9C_%EC%9E%90%EB%8F%99_%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0
