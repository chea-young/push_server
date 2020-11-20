# FCM_push_server

createsuperuser
ID : iceboat
password : 1234

### 가상 환경 켜기
python3 -m venv env
source push_venv/Scripts/activate  # On Windows use 

```
env\Scripts\activate
```

### restframework 다운
pip install django
pip install djangorestframework

### 파이썬 버전 낮추기
commend 에서 virtualenv 자기 가상환경이른 --python=python버전 하기


### keras 로 darknet 바꾸기 (참고 https://github.com/qqwweee/keras-yolo3)
curl -o yolo.weights https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
- 이때 convert.py랑 yolov3.cfg 필요

python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]

yolo_anchor -  임이의 박스 크기 (여기서 정한)

python yolo_video.py --image : 사진 입력을 받음 -> BMP으로 결과 나옴 -> .save 저장하게 만듦 -> result에 결과 저장 (날짜, 시간순으로)
- yolo.h5 model, anchors and classes loaded 필요

#yolo 서버의 restframework 
https://medium.com/@chamakhabdallah8/how-to-deploy-a-keras-model-to-production-with-django-drf-celery-and-redis-df4901014355 

### git branch
 - 생성 : git checkout -b <branch이름>
 - 푸시 : git push origin <branch이름>
 - 연동 : git branch --set-upstream-to origin/<branch 이름>
 - main으로 이동후 삭제 : git checkout main
        git branch --delete <branch 이름>
- 합치기(main으로 이동한 후) : git merge <bracnh 이름>

### 푸시
npm install -g firebase-tools

### push alarm 참고 링크
- https://github.com/firebase/quickstart-js/blob/master/messaging/README.md
- https://djangoworld.tistory.com/7
- https://firebase.google.com/docs/cloud-messaging/js/topic-messaging
- https://eunjin3786.tistory.com/m/281
- https://www.youtube.com/watch?v=BsCBCudx58g&feature=youtu.be  => firebase 사이트 웹 기반 파이어베이스 클라우드 메시징 시작하기 영상

### restful 참고 링크
- https://lsjsj92.tistory.com/503

## azure 링크 map 이용하는

- https://docs.microsoft.com/ko-kr/azure/azure-maps/how-to-manage-authentication#view-authentication-details

## 크롬에서 로그보기 
- ctrl+shif+j

## 카카오 API 사용하기
- 기초설명 : https://apis.map.kakao.com/web/guide/#ready
        - 틀린 부분 
        $ python -m SimpleHTTPServer 8080 -> python -m http.server 8080
        => http://localhost:8080/
- 샘플 API 설명들 : https://apis.map.kakao.com/web/sample/

### 카카오톡 지도 Javascript API
#### 라이브러리 설명
- clusterer: 마커를 클러스터링 할 수 있는 클러스터러 라이브러리 입니다.
- services: 장소 검색 과 주소-좌표 변환 을 할 수 있는 services 라이브러리 입니다.
- drawing: 지도 위에 마커와 그래픽스 객체를 쉽게 그릴 수 있게 그리기 모드를 지원하는 drawing 라이브러리 입니다.
#### 길찾기 바로 가기
- /link/to/이름,위도,경도  = https://map.kakao.com/link/to/카카오판교오피스,37.402056,127.108212
- /link/to/장소ID = https://map.kakao.com/link/to/18577297
- http://map.daum.net/?sName=출발지&eName=목적지


### Google 지도
- 참고 URL : https://m.blog.naver.com/codbs0703/221445387798
- 예시들과 라이브러리 설명 : https://developers.google.com/maps/documentation/javascript/overview
- URLs
        - 경로 https://www.google.com/maps/embed/v1/
        - 지도를 찾는 API 함수search?
        - 문자열 인자q=Moscow& (모스크바를 찾는 다는 가능)
        - API 키 key=API-KEY

- 길찾기 URLs
        - 경로 https://www.google.com/maps/embed/v1/
        - 지도를 찾는 API 함수 directions?
        - 출발지 origin=GorkyPark.=,Moscow&
        - 도착지 destination=StBasil,Moscow&
        - API 키 key=API-KEY

https://docs.vendhq.com/tutorials/guides/products/image-upload/image_uploads_code_samples/python_requests 이미지 전송 링크