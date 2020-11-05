createsuperuser
ID : iceboat
password : 1234

### 가상 환경 켜기
python3 -m venv env
source env/Scripts/activate  # On Windows use `env\Scripts\activate`

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


