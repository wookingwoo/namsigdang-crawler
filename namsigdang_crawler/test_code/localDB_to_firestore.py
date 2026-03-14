# -*- coding: utf-8 -*-

from tqdm import tqdm
import pickle

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

fb_cred = credentials.Certificate(
    "../data/account/namsigdang-crawler-firebase-adminsdk-fbsvc-c3f9e3e036_namsigdang-crawler.json"
)
firebase_admin.initialize_app(
    fb_cred,
    {
        "projectId": "namsigdang-crawler",
    },
)

fb_db = firestore.client()

# 전체 파일리스트
all_file_list = [
    "../data/crawling_menu/year_2018/month_02/2018_02_menu.dat",
    "../data/crawling_menu/year_2018/month_03/2018_03_menu.dat",
    "../data/crawling_menu/year_2018/month_04/2018_04_menu.dat",
    "../data/crawling_menu/year_2018/month_05/2018_05_menu.dat",
    "../data/crawling_menu/year_2018/month_06/2018_06_menu.dat",
    "../data/crawling_menu/year_2018/month_07/2018_07_menu.dat",
    "../data/crawling_menu/year_2018/month_08/2018_08_menu.dat",
    "../data/crawling_menu/year_2018/month_09/2018_09_menu.dat",
    "../data/crawling_menu/year_2018/month_10/2018_10_menu.dat",
    "../data/crawling_menu/year_2018/month_11/2018_11_menu.dat",
    "../data/crawling_menu/year_2018/month_12/2018_12_menu.dat",
    "../data/crawling_menu/year_2019/month_01/2019_01_menu.dat",
    "../data/crawling_menu/year_2019/month_02/2019_02_menu.dat",
    "../data/crawling_menu/year_2019/month_03/2019_03_menu.dat",
    "../data/crawling_menu/year_2019/month_04/2019_04_menu.dat",
    "../data/crawling_menu/year_2019/month_05/2019_05_menu.dat",
    "../data/crawling_menu/year_2019/month_06/2019_06_menu.dat",
    "../data/crawling_menu/year_2019/month_07/2019_07_menu.dat",
    "../data/crawling_menu/year_2019/month_08/2019_08_menu.dat",
    "../data/crawling_menu/year_2019/month_09/2019_09_menu.dat",
    "../data/crawling_menu/year_2019/month_10/2019_10_menu.dat",
    "../data/crawling_menu/year_2019/month_11/2019_11_menu.dat",
    "../data/crawling_menu/year_2019/month_12/2019_12_menu.dat",
    "../data/crawling_menu/year_2020/month_01/2020_01_menu.dat",
    "../data/crawling_menu/year_2020/month_02/2020_02_menu.dat",
    "../data/crawling_menu/year_2020/month_03/2020_03_menu.dat",
    "../data/crawling_menu/year_2020/month_04/2020_04_menu.dat",
    "../data/crawling_menu/year_2020/month_05/2020_05_menu.dat",
    "../data/crawling_menu/year_2020/month_06/2020_06_menu.dat",
    "../data/crawling_menu/year_2020/month_07/2020_07_menu.dat",
    "../data/crawling_menu/year_2020/month_08/2020_08_menu.dat",
    "../data/crawling_menu/year_2020/month_09/2020_09_menu.dat",
    "../data/crawling_menu/year_2020/month_10/2020_10_menu.dat",
    "../data/crawling_menu/year_2020/month_11/2020_11_menu.dat",
    "../data/crawling_menu/year_2020/month_12/2020_12_menu.dat",
    "../data/crawling_menu/year_2021/month_01/2021_01_menu.dat",
    "../data/crawling_menu/year_2021/month_02/2021_02_menu.dat",
    "../data/crawling_menu/year_2021/month_03/2021_03_menu.dat",
    "../data/crawling_menu/year_2021/month_04/2021_04_menu.dat",
    "../data/crawling_menu/year_2021/month_05/2021_05_menu.dat",
    "../data/crawling_menu/year_2021/month_06/2021_06_menu.dat",
    "../data/crawling_menu/year_2021/month_07/2021_07_menu.dat",
    "../data/crawling_menu/year_2021/month_08/2021_08_menu.dat",
    "../data/crawling_menu/year_2021/month_09/2021_09_menu.dat",
    "../data/crawling_menu/year_2021/month_10/2021_10_menu.dat",
    "../data/crawling_menu/year_2021/month_11/2021_11_menu.dat",
    "../data/crawling_menu/year_2021/month_12/2021_12_menu.dat",
    "../data/crawling_menu/year_2022/month_01/2022_01_menu.dat",
    "../data/crawling_menu/year_2022/month_02/2022_02_menu.dat",
    "../data/crawling_menu/year_2022/month_03/2022_03_menu.dat",
]

test_list = ["../data/crawling_menu/year_2021/month_12/2021_12_menu.dat"]

for i in tqdm(all_file_list):
    file_all_menu_dat = open(i, "rb")
    dic_month_menu = pickle.load(file_all_menu_dat)
    file_all_menu_dat.close()
    print(dic_month_menu)

    for y in sorted(dic_month_menu):
        # print("\"" + y + "\": \"" + dic_month_menu[y] + "\",")

        # firestore에 메뉴 저장
        try:
            fb_ref_eun_menu = (
                fb_db.collection("menu")
                .document("Eunpyeong")
                .collection(f"year_{y[2:6]}")
                .document(f"month_{y[6:8]}")
            )
            fb_ref_eun_menu.set({y: dic_month_menu[y]}, merge=True)

        except Exception as e:
            error = str(e)
            print("\n\n\t***firestore에 메뉴 저장 중 에러 발생")
            print(error + "\n")
