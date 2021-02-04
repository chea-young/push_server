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

### git branch
 - 생성 : git checkout -b <branch이름>
 - 푸시 : git push origin <branch이름>
 - 연동 : git branch --set-upstream-to origin/<branch 이름>
 - main으로 이동후 삭제 : git checkout main
        git branch --delete <branch 이름>
- 합치기(main으로 이동한 후) : git merge <bracnh 이름>


### push alarm 참고 링크
- https://github.com/firebase/quickstart-js/blob/master/messaging/README.md
- https://djangoworld.tistory.com/7
- https://firebase.google.com/docs/cloud-messaging/js/topic-messaging
- https://eunjin3786.tistory.com/m/281


