createsuperuser
ID : iceboat
password : 1234

## 가상 환경 켜기
python3 -m venv env
source env/Scripts/activate  # On Windows use `env\Scripts\activate`

## restframework 다운
pip install django
pip install djangorestframework
# yolo_server


# keras 로 darknet 바꾸기 (참고 https://github.com/qqwweee/keras-yolo3)
curl -o yolo.weights https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
- 이때 convert.py랑 yolov3.cfg 필요

python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]


# git branch
 생성 : git checkout -b <branch이름>
 푸시 : git push origin <branch이름>
 연동 : git branch --set-upstream-to origin/<branch 이름>
 main으로 이동후 삭제 : git checkout main
        git branch --delete <branch 이름>
