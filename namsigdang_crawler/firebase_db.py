import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from constants.data_path import project_path

fb_cred = credentials.Certificate(
    project_path
    + "/data/account/namsigdang-crawler-firebase-adminsdk-fbsvc-c3f9e3e036_namsigdang-crawler.json"
)
firebase_admin.initialize_app(
    fb_cred,
    {
        "projectId": "namsigdang-crawler",
    },
)

fb_db = firestore.client()

## 데이터 추가: .set
## 데이터 업데이트: .update (document가 존재하지 않을경우 오류)
## 데이터 추가 + merge: 업데이트 가능
# fb_ref_test = fb_db.collection('test1-1').document('test1-2').collection('test1-3').document('test1-4')
# fb_ref_test.set({
#     'test1': 1,
#     'test2': 2,
#     'test3': "test3"
# }, merge=True)
