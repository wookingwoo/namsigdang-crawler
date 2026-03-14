# namsigdang crawler
- namsigdang-crawler: https://github.com/wookingwoo/namsigdang-crawler
- namsigdang-chatbot: https://github.com/wookingwoo/namsigdang-chatbot
- namsigdang-android-app: https://github.com/wookingwoo/namsigdang-android-app

## Get started with Docker

```bash
docker build --tag namsigdang-crawler:1.0 .
```

## File Information

- crawler_main.py: 크롤러 메인

- classify_data_in_date.py : namsigdang/namsigdang_crawler/data/crawling_menu/all_menu.dat으로부터 년, 월로 분류하여
  namsigdang/namsigdang_crawler/data/crawling_menu에 year_2020/month_08/2020_08_menu.dat와 같이 저장. (Django App API에서 해당
  Data 사용)

## Installing Browser

### Installing Chrome

- How to check your Chrome version

```bash
$ google-chrome --version
```

- Installing Chrome (stable_current_amd64)

```bash
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ apt -y install ./google-chrome_104.0.5112.79_amd64.deb
```

- Installing Chrome (Google Chrome 104.0.5112.79)

```bash
$ cd namsigdang_crawler/setup_files/Chrome_104.0.5112.79
$ sudo dpkg -i google-chrome_104.0.5112.79_amd64.deb
$ sudo apt-get install -f
```

- 참고 사이트

```
https://christopher.su/2015/selenium-chromedriver-ubuntu/
```

### Installing Chromium

- Installing Chromium

```bash
apt install chromium
```

- How to check your Chromium version

```bash
chromium --version
```
